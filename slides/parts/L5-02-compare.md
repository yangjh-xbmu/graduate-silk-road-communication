---
layout: default
---

<div class="h-full flex flex-col justify-center" style="background:#1C2B4B;margin:-6rem;padding:6rem;">
  <div class="section-num">01</div>
  <div style="color:white;font-size:2rem;font-weight:700;margin-top:0.5rem;">对比分析</div>
  <div class="gold-line" style="width:80px;margin-top:1rem;"></div>
  <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.75rem;">视频大模型 vs 程序化框架：两种完全不同的能力</div>
</div>

---

## 素材有了，然后呢？

<div class="mt-4" style="font-size:0.88rem;color:#78716C;">上节课你们手里已经有了：5张AI海报 + 2条AI短视频 + 校准后的英文文案</div>

<div class="mt-5 card" style="border-color:#B8860B;">
  <div style="font-weight:700;font-size:1rem;color:#1C2B4B;margin-bottom:.8rem;">场景：制作"丝路城市巡礼"系列视频</div>
  <div class="grid grid-cols-3 gap-3" style="font-size:0.82rem;">
    <div style="text-align:center;padding:.6rem;background:rgba(184,134,11,.1);border-radius:6px;">
      <div class="stat-num" style="font-size:2rem;">10</div>
      <div style="font-size:0.72rem;color:#78716C;margin-top:.2rem;">座丝路城市</div>
    </div>
    <div style="text-align:center;padding:.6rem;background:rgba(184,134,11,.1);border-radius:6px;">
      <div class="stat-num" style="font-size:2rem;">×3</div>
      <div style="font-size:0.72rem;color:#78716C;margin-top:.2rem;">种语言版本</div>
    </div>
    <div style="text-align:center;padding:.6rem;background:rgba(184,134,11,.1);border-radius:6px;">
      <div class="stat-num" style="font-size:2rem;">= 30</div>
      <div style="font-size:0.72rem;color:#78716C;margin-top:.2rem;">条视频</div>
    </div>
  </div>
</div>

<div class="mt-4 l-border" style="font-size:0.85rem;color:#1C2B4B;">
  用剪映手工剪辑，每条30分钟 → 总共 <strong>15小时</strong>。<br>
  甲方说"Logo换个位置" → 改 <strong>30次</strong>。
</div>

---

## 画家 vs 流水线

<div class="mt-4 grid grid-cols-2 gap-5">

<div class="card" style="text-align:center;border-color:#B8860B;">
  <div style="font-size:2.5rem;margin-bottom:.5rem;">🎨</div>
  <div style="font-weight:700;font-size:1.1rem;color:#B8860B;margin-bottom:.5rem;">视频大模型</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.6;">
    海螺 · 即梦 · 可灵 · Runway<br><br>
    你说"画一幅沙漠驼队"<br>
    它挥笔而就<br>
    每次画出来都<strong>不一样</strong>
  </div>
  <div class="mt-3 badge">生成器</div>
</div>

<div class="card" style="text-align:center;border-color:#B8860B;">
  <div style="font-size:2.5rem;margin-bottom:.5rem;">🏭</div>
  <div style="font-weight:700;font-size:1.1rem;color:#B8860B;margin-bottom:.5rem;">程序化框架</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.6;">
    Remotion · Motion Canvas<br><br>
    你设计好模板<br>
    放进100份不同数据<br>
    出来100份格式<strong>完全统一</strong>的成品
  </div>
  <div class="mt-3 badge">组装线</div>
</div>

</div>

<div class="mt-5 card-dark" style="color:white;text-align:center;">
  <div style="font-size:1.1rem;color:#D4A843;font-weight:700;">
    画家和流水线不是竞争关系，是上下游关系
  </div>
</div>

---

## 核心差异对比

<table class="mt-4" style="font-size:0.78rem;">
  <thead>
    <tr>
      <th style="width:110px;">维度</th>
      <th>视频大模型（海螺/即梦/可灵）</th>
      <th>程序化框架（Remotion）</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>底层逻辑</strong></td>
      <td>AI概率预测（每次结果不同）</td>
      <td>代码逻辑（每次结果完全一致）</td>
    </tr>
    <tr>
      <td><strong>核心能力</strong></td>
      <td>无中生有，生成视觉素材</td>
      <td>精确组装，批量输出成品</td>
    </tr>
    <tr>
      <td><strong>文字处理</strong></td>
      <td>经常乱码、变形</td>
      <td>完美支持所有字体和排版</td>
    </tr>
    <tr>
      <td><strong>多语言扩展</strong></td>
      <td>很难保持画面一致</td>
      <td>换JSON文件，画面100%一致</td>
    </tr>
    <tr>
      <td><strong>精确控制</strong></td>
      <td>模糊控制（"大概这个感觉"）</td>
      <td>像素级、帧级精确控制</td>
    </tr>
    <tr>
      <td><strong>学习门槛</strong></td>
      <td>低（会写提示词就行）</td>
      <td>高（需要懂React代码）</td>
    </tr>
    <tr>
      <td><strong>修改成本</strong></td>
      <td>高（改一点就要重新生成）</td>
      <td>极低（改一行代码，全部同步更新）</td>
    </tr>
  </tbody>
</table>

<div class="mt-3 l-border" style="font-size:0.85rem;color:#1C2B4B;">
  做 <strong>1条</strong> 视频 → 大模型更快。做 <strong>30条</strong> 格式统一的视频 → Remotion 碾压。<br>
  丝路文化国际传播需要的恰好是后者。
</div>

---

## 互补关系：AI产"肉"，Remotion搭"骨骼"

<div class="mt-5 grid grid-cols-2 gap-4">

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.8rem;">AI大模型负责</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.8;">
    生成背景视频片段<br>
    生成配音（多语种）<br>
    生成背景音乐<br>
    生成风格化图片素材
  </div>
  <div class="mt-3 badge">原材料从哪来</div>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.8rem;">Remotion负责</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.8;">
    组装所有素材到时间线<br>
    叠加精确的标题和字幕<br>
    添加品牌Logo和片头片尾<br>
    批量输出多语言版本
  </div>
  <div class="mt-3 badge">怎么批量组装成产品</div>
</div>

</div>

<div class="mt-5 card-dark" style="color:white;text-align:center;">
  <div style="font-size:1.1rem;color:#D4A843;font-weight:700;">
    AI 解决"原材料从哪来"，Remotion 解决"怎么批量组装成产品"
  </div>
  <div style="font-size:0.82rem;color:#94A3B8;margin-top:.4rem;">
    上节课学了素材生成，今天补上最后一块拼图
  </div>
</div>
