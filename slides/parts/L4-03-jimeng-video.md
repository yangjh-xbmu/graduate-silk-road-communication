---
layout: default
---

<div class="h-full flex flex-col justify-center" style="background:#1C2B4B;margin:-6rem;padding:6rem;">
  <div class="section-num">02</div>
  <div style="color:white;font-size:2rem;font-weight:700;margin-top:0.5rem;">即梦视频功能详解</div>
  <div class="gold-line" style="width:80px;margin-top:1rem;"></div>
  <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.75rem;">文生视频 · 图生视频 · 运镜控制</div>
</div>

---

## 视频提示词 vs 图片提示词：关键差异

<div class="mt-5 grid grid-cols-2 gap-6">

<div>
  <div style="font-size:0.82rem;color:#78716C;margin-bottom:.5rem;">图片提示词 = 六要素</div>
  <div class="card" style="border-color:#94A3B8;">
    <div style="font-size:0.85rem;">主体 / 场景 / 风格</div>
    <div style="font-size:0.85rem;">光影 / 构图 / 品质</div>
    <div style="font-size:0.75rem;color:#78716C;margin-top:.8rem;">描述一个静态画面</div>
  </div>
</div>

<div>
  <div style="font-size:0.82rem;color:#78716C;margin-bottom:.5rem;">视频提示词 = 六要素 + 时间轴 + 运镜</div>
  <div class="card" style="border-color:#B8860B;">
    <div style="font-size:0.85rem;">主体 / 场景 / 风格</div>
    <div style="font-size:0.85rem;">光影 / 构图 / 品质</div>
    <div style="font-size:0.85rem;color:#B8860B;margin-top:.5rem;">+ <strong>时间轴</strong>：画面如何变化</div>
    <div style="font-size:0.85rem;color:#B8860B;">+ <strong>运镜词</strong>：镜头如何运动</div>
  </div>
</div>

</div>

---

## 运镜词速查表

<div class="mt-4 grid grid-cols-2 gap-3">

<div class="card">
  <div style="font-weight:700;margin-bottom:.5rem;color:#B8860B;">镜头运动</div>
  <div style="font-size:0.82rem;line-height:1.8;">
    推镜头 / 拉镜头 / 摇镜头 / 移镜头<br>
    环绕镜头 / 航拍俯冲 / 缓慢上升 / 推进特写
  </div>
</div>

<div class="card">
  <div style="font-weight:700;margin-bottom:.5rem;color:#B8860B;">镜头角度</div>
  <div style="font-size:0.82rem;line-height:1.8;">
    低角度仰拍 / 高角度俯拍 / 平视 / 鸟瞰全景
  </div>
</div>

<div class="card">
  <div style="font-weight:700;margin-bottom:.5rem;color:#B8860B;">速度描述</div>
  <div style="font-size:0.82rem;line-height:1.8;">
    缓慢移动 / 快速穿过 / 静止凝视 / 渐变过渡
  </div>
</div>

<div class="card">
  <div style="font-weight:700;margin-bottom:.5rem;color:#B8860B;">组合示例</div>
  <div style="font-size:0.75rem;line-height:1.8;color:#78716C;">
    "低角度仰拍，镜头缓慢推进，聚焦于飞天仙女的飘带"<br>
    "全景俯视，镜头环绕一圈，展示敦煌洞窟全貌"
  </div>
</div>

</div>

---

## 时间轴描述质量对比

<table class="mt-4" style="font-size:0.85rem;">
  <thead>
    <tr>
      <th style="width:80px;">质量</th>
      <th>描述</th>
      <th>效果</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong style="color:#ef4444;">差</strong></td>
      <td>丝绸之路商队</td>
      <td style="color:#78716C;">AI不知道要表现什么运动，生成结果随机</td>
    </tr>
    <tr>
      <td><strong style="color:#f59e0b;">良</strong></td>
      <td>丝绸之路上，一只骆驼商队缓缓前行</td>
      <td style="color:#78716C;">有基本运动，但镜头和节奏不明确</td>
    </tr>
    <tr>
      <td><strong style="color:#22c55e;">优</strong></td>
      <td>丝绸之路上，一只骆驼商队从远处缓缓走来，越过镜头前景，消失在远方的沙丘尽头</td>
      <td style="color:#78716C;">有景别变化、有节奏感，生成结果可控</td>
    </tr>
  </tbody>
</table>

---

## 文生视频完整提示词示例

<div class="mt-4 card" style="font-size:0.75rem;font-family:monospace;background:rgba(30,30,46,.95);color:#E2E8F0;padding:.8rem 1.2rem;line-height:1.8;">
<div style="color:#B8860B;">【主体】</div>一位身着唐代丝绸长裙的飞天仙女，手持琵琶，飘带飞扬<br><br>
<div style="color:#B8860B;">【场景】</div>敦煌莫高窟九层楼作为背景，蓝天白云<br><br>
<div style="color:#B8860B;">【风格】</div>敦煌壁画工笔重彩风格，矿物颜料质感<br><br>
<div style="color:#B8860B;">【光影】</div>金色阳光从侧面照射，温暖而神圣<br><br>
<div style="color:#B8860B;">【时间轴】</div>仙女在空中缓缓旋转，飘带随风轻轻飘动<br><br>
<div style="color:#B8860B;">【运镜】</div>低角度仰拍，镜头缓慢向上推进
</div>

<div class="mt-3 l-border" style="font-size:0.82rem;color:#1C2B4B;">
  参数设置：模型 4.5 / 比例 16:9 / 时长 6秒
</div>
