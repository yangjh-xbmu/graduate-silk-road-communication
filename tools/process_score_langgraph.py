from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, TypedDict

from langgraph.graph import END, START, StateGraph


REPO_ROOT = Path(__file__).resolve().parents[1]
PROMPT_DIR = REPO_ROOT / "prompts" / "process-score"


class WorkflowState(TypedDict, total=False):
    student_dir: str
    process_root: str
    timeout_seconds: int
    force: bool
    evidence_md: str
    evidence_json: dict[str, Any]
    skipped: bool
    kimi: dict[str, Any]
    agy: dict[str, Any]
    codex: dict[str, Any]
    final_json: dict[str, Any]
    started_at: float
    finished_at: float


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def resolve_tool(name: str) -> str:
    found = shutil.which(name)
    if not found:
        raise RuntimeError(f"Required CLI not found on PATH: {name}")
    return found


def run_cli(
    command: list[str],
    cwd: Path,
    timeout: int,
    output_path: Path,
    stdin_text: str | None = None,
) -> dict[str, Any]:
    env = os.environ.copy()
    env.update(
        {
            "PYTHONIOENCODING": "utf-8",
            "PYTHONUTF8": "1",
            "LC_ALL": "C.UTF-8",
            "LANG": "C.UTF-8",
            "NO_COLOR": "1",
        }
    )
    started = time.time()
    try:
        completed = subprocess.run(
            command,
            cwd=str(cwd),
            env=env,
            capture_output=True,
            input=stdin_text,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout,
        )
        raw = completed.stdout
        if completed.stderr:
            raw += "\n\n[stderr]\n" + completed.stderr
        write_text(output_path, raw)
        return {
            "command": command,
            "cwd": str(cwd),
            "output": str(output_path),
            "exit_code": completed.returncode,
            "timed_out": False,
            "duration_seconds": round(time.time() - started, 2),
            "bytes": output_path.stat().st_size if output_path.exists() else 0,
        }
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", errors="replace")
        raw = f"[CLI_TIMEOUT after {timeout}s]\n\n{stdout}"
        if stderr:
            raw += "\n\n[stderr]\n" + stderr
        write_text(output_path, raw)
        return {
            "command": command,
            "cwd": str(cwd),
            "output": str(output_path),
            "exit_code": None,
            "timed_out": True,
            "duration_seconds": round(time.time() - started, 2),
            "bytes": output_path.stat().st_size if output_path.exists() else 0,
        }


def extract_json_object(text: str) -> dict[str, Any] | None:
    decoder = json.JSONDecoder()
    starts = [m.start() for m in re.finditer(r"\{", text)]
    for start in starts:
        try:
            obj, _ = decoder.raw_decode(text[start:])
        except json.JSONDecodeError:
            continue
        if isinstance(obj, dict):
            return obj
    return None


def parse_score(text: str) -> int | None:
    obj = extract_json_object(text)
    if obj:
        for key in ("total", "score", "final_score", "process_score"):
            value = obj.get(key)
            if isinstance(value, (int, float)):
                return int(round(value))
    patterns = [
        r"total[^0-9]{0,20}([0-9]{1,3})",
        r"process[_ ]score[^0-9]{0,20}([0-9]{1,3})",
        r"score[^0-9]{0,20}([0-9]{1,3})",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = int(match.group(1))
            if 0 <= value <= 100:
                return value
    return None


def codex_prompt(kimi_status: dict[str, Any], agy_status: dict[str, Any]) -> str:
    template = read_text(PROMPT_DIR / "codex-arbitration.md")
    return (
        template.replace("{{KIMI_STATUS_JSON}}", json.dumps(kimi_status, ensure_ascii=False, indent=2))
        .replace("{{AGY_STATUS_JSON}}", json.dumps(agy_status, ensure_ascii=False, indent=2))
    )


def load_evidence(state: WorkflowState) -> WorkflowState:
    student_dir = Path(state["student_dir"])
    final_path = student_dir / "final-arbitration.langgraph.json"
    if final_path.exists() and not state.get("force", False):
        state["skipped"] = True
        state["final_json"] = json.loads(read_text(final_path))
        return state

    evidence_path = student_dir / "process-evidence.md"
    if not evidence_path.exists():
        raise FileNotFoundError(f"Missing process-evidence.md: {evidence_path}")
    state["evidence_md"] = read_text(evidence_path)
    json_path = student_dir / "process-evidence.json"
    if json_path.exists():
        try:
            state["evidence_json"] = json.loads(read_text(json_path))
        except json.JSONDecodeError:
            state["evidence_json"] = {"decode_error": str(json_path)}
    return state


def should_skip(state: WorkflowState) -> str:
    return "skip" if state.get("skipped") else "continue"


def write_prompts(state: WorkflowState) -> WorkflowState:
    student_dir = Path(state["student_dir"])
    write_text(student_dir / "langgraph-kimi-prompt.md", read_text(PROMPT_DIR / "kimi-review.md"))
    write_text(student_dir / "langgraph-agy-prompt.md", read_text(PROMPT_DIR / "agy-review.md"))
    return state


def run_kimi(state: WorkflowState) -> WorkflowState:
    student_dir = Path(state["student_dir"])
    process_root = Path(state["process_root"])
    kimi = resolve_tool("kimi")
    command = [
        kimi,
        "--work-dir",
        str(student_dir),
        "--add-dir",
        str(process_root),
        "--print",
        "--input-format",
        "text",
        "--output-format",
        "text",
    ]
    status = run_cli(
        command,
        student_dir,
        int(state["timeout_seconds"]),
        student_dir / "kimi-score.langgraph.md",
        read_text(student_dir / "langgraph-kimi-prompt.md"),
    )
    status["parsed_total"] = parse_score(read_text(student_dir / "kimi-score.langgraph.md"))
    state["kimi"] = status
    return state


def run_agy(state: WorkflowState) -> WorkflowState:
    student_dir = Path(state["student_dir"])
    process_root = Path(state["process_root"])
    agy = resolve_tool("agy")
    command = [
        agy,
        "--add-dir",
        str(student_dir),
        "--add-dir",
        str(process_root),
        "--print-timeout",
        f"{int(state['timeout_seconds'])}s",
        "--print",
        "Read langgraph-agy-prompt.md and follow it. Do not modify files.",
    ]
    status = run_cli(command, student_dir, int(state["timeout_seconds"]) + 20, student_dir / "agy-score.langgraph.md")
    status["parsed_total"] = parse_score(read_text(student_dir / "agy-score.langgraph.md"))
    state["agy"] = status
    return state


def run_codex(state: WorkflowState) -> WorkflowState:
    student_dir = Path(state["student_dir"])
    process_root = Path(state["process_root"])
    codex = resolve_tool("codex")
    prompt_path = student_dir / "langgraph-codex-prompt.md"
    output_path = student_dir / "codex-score.langgraph.md"
    log_path = student_dir / "codex-cli.langgraph.log"
    write_text(prompt_path, codex_prompt(state.get("kimi", {}), state.get("agy", {})))

    command = [
        codex,
        "exec",
        "-C",
        str(student_dir),
        "--add-dir",
        str(process_root),
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--ephemeral",
        "-o",
        str(output_path),
        "-",
    ]
    status = run_cli(
        command,
        student_dir,
        int(state["timeout_seconds"]) + 60,
        log_path,
        read_text(prompt_path),
    )
    if not output_path.exists():
        write_text(output_path, read_text(log_path))
    status["output"] = str(output_path)
    status["log"] = str(log_path)
    status["parsed_total"] = parse_score(read_text(output_path))
    state["codex"] = status
    return state


def persist_final(state: WorkflowState) -> WorkflowState:
    student_dir = Path(state["student_dir"])
    codex_text = read_text(student_dir / "codex-score.langgraph.md")
    final_obj = extract_json_object(codex_text) or {}
    if "total" not in final_obj and state.get("codex", {}).get("parsed_total") is not None:
        final_obj["total"] = state["codex"]["parsed_total"]
    final_obj.setdefault("completion_status", "complete" if "total" in final_obj else "incomplete")
    final_obj.setdefault("kimi_status", state.get("kimi", {}))
    final_obj.setdefault("agy_status", state.get("agy", {}))
    final_obj.setdefault("codex_status", state.get("codex", {}))
    final_obj["student_dir"] = str(student_dir)
    final_obj["finished_at"] = time.strftime("%Y-%m-%d %H:%M:%S")

    md = [
        "# LangGraph Process Score Arbitration",
        "",
        f"- Student directory: `{student_dir}`",
        f"- Completion status: `{final_obj.get('completion_status')}`",
        f"- Final total: `{final_obj.get('total', '')}`",
        f"- Kimi parsed total: `{state.get('kimi', {}).get('parsed_total')}`",
        f"- agy parsed total: `{state.get('agy', {}).get('parsed_total')}`",
        f"- Codex parsed total: `{state.get('codex', {}).get('parsed_total')}`",
        "",
        "## Final JSON",
        "",
        "```json",
        json.dumps(final_obj, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Codex Arbitration",
        "",
        codex_text,
        "",
    ]
    write_text(student_dir / "final-arbitration.langgraph.md", "\n".join(md))
    write_text(student_dir / "final-arbitration.langgraph.json", json.dumps(final_obj, ensure_ascii=False, indent=2))
    state["final_json"] = final_obj
    state["finished_at"] = time.time()
    return state


def skip_done(state: WorkflowState) -> WorkflowState:
    return state


def build_graph():
    graph = StateGraph(WorkflowState)
    graph.add_node("load_evidence", load_evidence)
    graph.add_node("write_prompts", write_prompts)
    graph.add_node("run_kimi", run_kimi)
    graph.add_node("run_agy", run_agy)
    graph.add_node("run_codex", run_codex)
    graph.add_node("persist_final", persist_final)
    graph.add_node("skip_done", skip_done)
    graph.add_edge(START, "load_evidence")
    graph.add_conditional_edges("load_evidence", should_skip, {"skip": "skip_done", "continue": "write_prompts"})
    graph.add_edge("write_prompts", "run_kimi")
    graph.add_edge("run_kimi", "run_agy")
    graph.add_edge("run_agy", "run_codex")
    graph.add_edge("run_codex", "persist_final")
    graph.add_edge("persist_final", END)
    graph.add_edge("skip_done", END)
    return graph.compile()


def find_default_process_root() -> Path | None:
    base = Path("D:/Users/yangjh/Desktop/Inbox/_processed")
    if not base.exists():
        return None
    matches = sorted(base.glob("*/grading/process-score"), key=lambda p: p.stat().st_mtime, reverse=True)
    return matches[0] if matches else None


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run LangGraph process-score grading for one student.")
    parser.add_argument("--student-dir", required=True, help="Prepared student process-score directory.")
    parser.add_argument("--process-root", help="Process-score root. Defaults to latest Inbox/_processed/*/grading/process-score.")
    parser.add_argument("--timeout-seconds", type=int, default=180, help="Per-reviewer timeout.")
    parser.add_argument("--force", action="store_true", help="Regenerate even if final arbitration exists.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    process_root = Path(args.process_root) if args.process_root else find_default_process_root()
    if not process_root:
        raise SystemExit("Could not locate process-score root. Pass --process-root.")
    student_dir = Path(args.student_dir)
    initial: WorkflowState = {
        "student_dir": str(student_dir.resolve()),
        "process_root": str(process_root.resolve()),
        "timeout_seconds": args.timeout_seconds,
        "force": args.force,
        "started_at": time.time(),
    }
    result = build_graph().invoke(initial)
    print(json.dumps(result.get("final_json", {}), ensure_ascii=False, indent=2))
    return 0 if result.get("final_json", {}).get("completion_status") == "complete" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
