---
layout: default
---

<div class="h-full flex flex-col justify-center" style="background:#1C2B4B;margin:-6rem;padding:6rem;">
  <div class="section-num">04</div>
  <div style="color:white;font-size:2rem;font-weight:700;margin-top:0.5rem;">工作流</div>
  <div class="gold-line" style="width:80px;margin-top:1rem;"></div>
  <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.75rem;">Remotion + AI 组装线怎么运转</div>
</div>

---

## 完整工作流

<div class="mt-3" style="font-size:0.82rem;line-height:2.2;">

<div style="display:flex;align-items:center;margin-bottom:.3rem;">
  <div style="width:28px;height:28px;background:#B8860B;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;">1</div>
  <div style="margin-left:.8rem;"><strong>课题策划</strong> → 脚本撰写（人工 / AI辅助）</div>
</div>

<div style="display:flex;align-items:flex-start;margin-bottom:.3rem;">
  <div style="width:28px;height:28px;background:#B8860B;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;">2</div>
  <div style="margin-left:.8rem;">
    <strong>AI素材生成</strong>（并行）<br>
    <span style="color:#78716C;font-size:0.78rem;">画面：可灵/海螺 · 配音：ElevenLabs/Fish Audio · 配乐：Suno AI · 字幕：AI翻译+人工校准</span>
  </div>
</div>

<div style="display:flex;align-items:flex-start;margin-bottom:.3rem;">
  <div style="width:28px;height:28px;background:#B8860B;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;">3</div>
  <div style="margin-left:.8rem;">
    <strong>Remotion 组装</strong><br>
    <span style="color:#78716C;font-size:0.78rem;">导入素材 · 编排Sequence · 添加interpolate动画 · 叠加标题/字幕/Logo · 参数化多语言</span>
  </div>
</div>

<div style="display:flex;align-items:center;margin-bottom:.3rem;">
  <div style="width:28px;height:28px;background:#B8860B;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;">4</div>
  <div style="margin-left:.8rem;"><strong>渲染输出</strong> → 本地 <code>npx remotion render</code> 或云端 Lambda 并行</div>
</div>

<div style="display:flex;align-items:center;">
  <div style="width:28px;height:28px;background:#B8860B;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;">5</div>
  <div style="margin-left:.8rem;"><strong>适配分发</strong> → YouTube 横版16:9 · TikTok 竖版9:16 · Instagram 方形1:1</div>
</div>

</div>

---

## AI视频工具全景

<table class="mt-4" style="font-size:0.8rem;">
  <thead>
    <tr>
      <th style="width:100px;">层次</th>
      <th>代表工具</th>
      <th>能力</th>
      <th style="width:80px;">进度</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>素材生成</strong></td>
      <td>可灵 · 海螺 · 即梦 · Runway</td>
      <td>文字/图片 → 视频片段</td>
      <td><span style="color:#22c55e;font-weight:600;">上节课 ✓</span></td>
    </tr>
    <tr>
      <td><strong>数字人</strong></td>
      <td>HeyGen · Synthesia · D-ID</td>
      <td>AI虚拟主播、多语种口播</td>
      <td><span style="color:#78716C;">了解</span></td>
    </tr>
    <tr>
      <td><strong>音频</strong></td>
      <td>ElevenLabs · Fish Audio · Suno</td>
      <td>AI配音、音乐生成</td>
      <td><span style="color:#78716C;">了解</span></td>
    </tr>
    <tr style="background:rgba(184,134,11,.12);">
      <td><strong>组装编排</strong></td>
      <td><strong>Remotion</strong> · Motion Canvas</td>
      <td><strong>程序化视频合成与批量输出</strong></td>
      <td><span style="color:#B8860B;font-weight:600;">今天</span></td>
    </tr>
  </tbody>
</table>

<div class="mt-4 card-dark" style="color:white;text-align:center;">
  <div style="font-size:1rem;color:#D4A843;font-weight:700;">
    前三层解决"原材料从哪来"，第四层解决"怎么组装成产品"
  </div>
</div>

---

## 为什么丝路项目特别适合

<div class="mt-5 grid grid-cols-2 gap-4">

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">数据驱动叙事</div>
  <div style="font-size:0.82rem;color:#78716C;">丝路城市、历史事件、贸易商品都是结构化数据，天然适合 JSON 驱动</div>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">多语言刚需</div>
  <div style="font-size:0.82rem;color:#78716C;">中文、英文、阿拉伯语、波斯语——换配置文件就能批量生成</div>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">地图动画</div>
  <div style="font-size:0.82rem;color:#78716C;">丝路路线天然适合可视化，interpolate 程序化绘制路线延伸动画</div>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">AI素材无缝集成</div>
  <div style="font-size:0.82rem;color:#78716C;">前几节课生成的海报、视频片段、配音，直接导入 Remotion 组件</div>
</div>

</div>
