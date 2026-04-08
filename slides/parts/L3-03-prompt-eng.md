---
layout: default
---

<div class="h-full flex flex-col justify-center" style="background:#1C2B4B;margin:-6rem;padding:6rem;">
  <div class="section-num">02</div>
  <div style="color:white;font-size:2rem;font-weight:700;margin-top:0.5rem;">提示词工程</div>
  <div class="gold-line" style="width:80px;margin-top:1rem;"></div>
  <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.75rem;">从"抽卡"到"工业级"的跨越</div>
</div>

---

## 为什么你的AI出图总是"差一点"

<div class="mt-5 grid grid-cols-2 gap-6">

<div>
  <div style="font-size:0.82rem;color:#78716C;margin-bottom:.5rem;">❌ 抽卡模式</div>
  <div class="card" style="border-color:#ef4444;">
    <div style="font-size:0.9rem;">输入"敦煌壁画海报"</div>
    <div style="font-size:0.82rem;color:#78716C;margin-top:.5rem;">→ 出4张图，1张还行，3张离谱</div>
    <div style="font-size:0.82rem;color:#78716C;">→ 点重新生成，又是随机的</div>
    <div style="font-size:0.82rem;color:#78716C;">→ 靠运气，效率极低</div>
  </div>
</div>

<div>
  <div style="font-size:0.82rem;color:#78716C;margin-bottom:.5rem;">✅ 工程化模式</div>
  <div class="card" style="border-color:#22c55e;">
    <div style="font-size:0.9rem;">用结构化提示词精确描述</div>
    <div style="font-size:0.82rem;color:#78716C;margin-top:.5rem;">→ 每次生成结果都在预期范围内</div>
    <div style="font-size:0.82rem;color:#78716C;">→ 一次调一个变量，快速逼近目标</div>
    <div style="font-size:0.82rem;color:#78716C;">→ 可复用、可批量、可协作</div>
  </div>
</div>

</div>

<div class="mt-5 l-border" style="font-size:0.9rem;">
  专业做法不是抽卡，是<strong>工程化</strong>。把模糊想法变成精确指令。
</div>

---

## 提示词六要素框架

<div class="mt-4 grid grid-cols-3 gap-3">

<div class="card" style="text-align:center;">
  <div style="font-size:1.5rem;font-weight:700;color:#B8860B;">主体</div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.3rem;">画面核心对象</div>
  <div style="font-size:0.75rem;margin-top:.5rem;background:rgba(184,134,11,.08);padding:.3rem .5rem;border-radius:4px;">丝路商人牵着骆驼</div>
</div>

<div class="card" style="text-align:center;">
  <div style="font-size:1.5rem;font-weight:700;color:#B8860B;">场景</div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.3rem;">在哪里、什么环境</div>
  <div style="font-size:0.75rem;margin-top:.5rem;background:rgba(184,134,11,.08);padding:.3rem .5rem;border-radius:4px;">塔克拉玛干沙漠日落</div>
</div>

<div class="card" style="text-align:center;">
  <div style="font-size:1.5rem;font-weight:700;color:#B8860B;">风格</div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.3rem;">什么艺术风格</div>
  <div style="font-size:0.75rem;margin-top:.5rem;background:rgba(184,134,11,.08);padding:.3rem .5rem;border-radius:4px;">敦煌壁画工笔重彩</div>
</div>

<div class="card" style="text-align:center;">
  <div style="font-size:1.5rem;font-weight:700;color:#B8860B;">光影</div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.3rem;">光照和氛围</div>
  <div style="font-size:0.75rem;margin-top:.5rem;background:rgba(184,134,11,.08);padding:.3rem .5rem;border-radius:4px;">金色逆光、暖色调</div>
</div>

<div class="card" style="text-align:center;">
  <div style="font-size:1.5rem;font-weight:700;color:#B8860B;">构图</div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.3rem;">镜头角度和布局</div>
  <div style="font-size:0.75rem;margin-top:.5rem;background:rgba(184,134,11,.08);padding:.3rem .5rem;border-radius:4px;">低角度仰拍、广角</div>
</div>

<div class="card" style="text-align:center;">
  <div style="font-size:1.5rem;font-weight:700;color:#B8860B;">品质</div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.3rem;">技术参数和排除项</div>
  <div style="font-size:0.75rem;margin-top:.5rem;background:rgba(184,134,11,.08);padding:.3rem .5rem;border-radius:4px;">超高清、无文字</div>
</div>

</div>

<div class="mt-4" style="text-align:center;font-size:0.85rem;color:#78716C;">
  像填表一样把六个格子填满，出图质量立刻上一个台阶
</div>

---

## 坏提示词 vs 好提示词

<div class="mt-4 grid grid-cols-2 gap-5">

<div>
  <div style="font-size:0.82rem;color:#ef4444;font-weight:600;margin-bottom:.5rem;">❌ 坏提示词</div>
  <div style="font-family:monospace;font-size:0.82rem;background:rgba(30,30,46,.95);color:#E2E8F0;padding:1rem;border-radius:6px;">
    敦煌壁画海报
  </div>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.5rem;">
    AI不知道要什么主体、构图、用途<br>生成结果模糊、杂乱、不可用
  </div>
</div>

<div>
  <div style="font-size:0.82rem;color:#22c55e;font-weight:600;margin-bottom:.5rem;">✅ 好提示词（六要素版）</div>
  <div style="font-family:monospace;font-size:0.72rem;background:rgba(30,30,46,.95);color:#E2E8F0;padding:1rem;border-radius:6px;line-height:1.6;">
    <span style="color:#D4A843;">[主体]</span> 飞天仙女，手持琵琶，飘带飞扬<br>
    <span style="color:#D4A843;">[场景]</span> 莫高窟藻井图案背景，星空祥云<br>
    <span style="color:#D4A843;">[风格]</span> 敦煌壁画工笔重彩，矿物颜料质感<br>
    <span style="color:#D4A843;">[光影]</span> 金色光晕背后散射，温暖神圣<br>
    <span style="color:#D4A843;">[构图]</span> 居中对称，竖版海报比例<br>
    <span style="color:#D4A843;">[品质]</span> 超高清，细节精致，无文字
  </div>
</div>

</div>

<div class="mt-3 l-border" style="font-size:0.9rem;">
  六要素不是让你写更多字，是让你<strong>把模糊的想法变成精确的指令</strong>。右图即为六要素提示词生成的效果 →
</div>

<img src="/images/L3/demo-poster.png" style="position:absolute;right:2rem;bottom:2rem;height:200px;border-radius:6px;box-shadow:0 2px 12px rgba(0,0,0,.2);opacity:.9;" alt="六要素提示词生成效果" />

---

## 丝路文化提示词速查表

<div class="mt-3 grid grid-cols-2 gap-4">

<div>
<table style="font-size:0.78rem;">
  <thead><tr><th style="width:70px;">类别</th><th>常用词库</th></tr></thead>
  <tbody>
    <tr><td><strong>人物</strong></td><td>丝路商人、飞天仙女、骆驼队、僧侣、工匠、乐师</td></tr>
    <tr><td><strong>器物</strong></td><td>琵琶、丝绸、瓷器、香料、铜镜、经卷</td></tr>
    <tr><td><strong>建筑</strong></td><td>莫高窟、交河故城、大雁塔、撒马尔罕清真寺</td></tr>
    <tr><td><strong>自然</strong></td><td>塔克拉玛干沙漠、河西走廊、天山雪峰、绿洲</td></tr>
    <tr><td><strong>人文</strong></td><td>丝路驿站、巴扎集市、石窟寺、烽火台</td></tr>
  </tbody>
</table>
</div>

<div>
<table style="font-size:0.78rem;">
  <thead><tr><th style="width:70px;">类别</th><th>常用词库</th></tr></thead>
  <tbody>
    <tr><td><strong>传统风格</strong></td><td>敦煌壁画、唐三彩配色、波斯细密画、水墨写意</td></tr>
    <tr><td><strong>现代风格</strong></td><td>赛博朋克丝路、极简主义、扁平插画、3D渲染</td></tr>
    <tr><td><strong>光影</strong></td><td>沙漠金光、烛火暖光、月光冷调、洞窟体积光</td></tr>
    <tr><td><strong>构图</strong></td><td>鸟瞰全景、特写手部工艺、对称藻井、骆驼剪影</td></tr>
  </tbody>
</table>
</div>

</div>

<div class="mt-4" style="text-align:center;font-size:0.82rem;color:#78716C;">
  存好这张表，后面做海报和短视频都用得上。需要时翻出来组合即可。
</div>
