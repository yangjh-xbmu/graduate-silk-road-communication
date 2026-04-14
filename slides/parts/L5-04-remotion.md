---
layout: default
---

<div class="h-full flex flex-col justify-center" style="background:#1C2B4B;margin:-6rem;padding:6rem;">
  <div class="section-num">03</div>
  <div style="color:white;font-size:2rem;font-weight:700;margin-top:0.5rem;">Remotion 核心概念</div>
  <div class="gold-line" style="width:80px;margin-top:1rem;"></div>
  <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.75rem;">用代码描述时间线 · 当前版本 v4.x</div>
</div>

---

## 什么是 Remotion

<div class="mt-3" style="font-size:0.88rem;color:#78716C;">基于 React 的程序化视频框架。核心理念：用写代码的方式制作视频。</div>

<div class="mt-4 card" style="text-align:center;font-size:0.9rem;font-weight:600;color:#1C2B4B;padding:1rem;">
  React 组件 → 浏览器逐帧渲染 → FFmpeg 编码 → MP4 视频
</div>

<div class="mt-5 grid grid-cols-4 gap-3">

<div class="card" style="text-align:center;padding:.8rem;">
  <div style="font-weight:700;color:#B8860B;font-size:0.85rem;">可复用</div>
  <div style="font-size:0.72rem;color:#78716C;margin-top:.3rem;">换数据生成新视频</div>
</div>

<div class="card" style="text-align:center;padding:.8rem;">
  <div style="font-weight:700;color:#B8860B;font-size:0.85rem;">可批量</div>
  <div style="font-size:0.72rem;color:#78716C;margin-top:.3rem;">一次写，100个版本</div>
</div>

<div class="card" style="text-align:center;padding:.8rem;">
  <div style="font-weight:700;color:#B8860B;font-size:0.85rem;">可版本控制</div>
  <div style="font-size:0.72rem;color:#78716C;margin-top:.3rem;">Git管理视频逻辑</div>
</div>

<div class="card" style="text-align:center;padding:.8rem;">
  <div style="font-weight:700;color:#B8860B;font-size:0.85rem;">可自动化</div>
  <div style="font-size:0.72rem;color:#78716C;margin-top:.3rem;">AI素材无缝对接</div>
</div>

</div>

---

## 概念一 · Composition（合成）

<div class="mt-2" style="font-size:0.82rem;color:#78716C;">视频的"身份证"：声明尺寸、帧率、总时长</div>

```jsx
<Composition
  id="SilkRoadCities"
  component={SilkRoadCities}
  durationInFrames={300}  // 10秒 × 30帧
  fps={30}
  width={1920}
  height={1080}
/>
```

<div class="mt-4 grid grid-cols-4 gap-3" style="font-size:0.82rem;">
  <div style="text-align:center;padding:.5rem;background:rgba(184,134,11,.1);border-radius:6px;">
    <strong>id</strong><br><span style="color:#78716C;">视频名称</span>
  </div>
  <div style="text-align:center;padding:.5rem;background:rgba(184,134,11,.1);border-radius:6px;">
    <strong>fps={30}</strong><br><span style="color:#78716C;">每秒30帧</span>
  </div>
  <div style="text-align:center;padding:.5rem;background:rgba(184,134,11,.1);border-radius:6px;">
    <strong>300帧</strong><br><span style="color:#78716C;">÷30fps = 10秒</span>
  </div>
  <div style="text-align:center;padding:.5rem;background:rgba(184,134,11,.1);border-radius:6px;">
    <strong>1920×1080</strong><br><span style="color:#78716C;">全高清</span>
  </div>
</div>

---

## 概念二 · Sequence（序列）

<div class="mt-2" style="font-size:0.82rem;color:#78716C;">控制谁在什么时候出场、显示多久</div>

```jsx
<Sequence from={0} durationInFrames={90}>
  <TitleCard text="丝路城市巡礼" />
</Sequence>
<Sequence from={90} durationInFrames={120}>
  <CityCard name="长安" description="丝绸之路的东方起点" />
</Sequence>
<Sequence from={210} durationInFrames={90}>
  <CityCard name="敦煌" description="河西走廊的艺术宝库" />
</Sequence>
```

<div class="mt-4" style="font-size:0.82rem;">

| 时间段 | 帧范围 | 内容 |
|--------|--------|------|
| 0-3秒 | 0-90帧 | 标题卡片 |
| 3-7秒 | 90-210帧 | 长安城市介绍 |
| 7-10秒 | 210-300帧 | 敦煌城市介绍 |

</div>

<div class="mt-2 l-border" style="font-size:0.82rem;color:#1C2B4B;">
  像写剧本一样编排时间线，只不过用代码写。添加新城市？多加一个 Sequence 就行。
</div>

---

## 概念三 · interpolate（插值）

<div class="mt-2" style="font-size:0.82rem;color:#78716C;">把"当前第几帧"翻译成"透明度/位置/大小应该是多少"</div>

```jsx
const frame = useCurrentFrame();

// 前30帧（1秒）：透明度从0渐变到1
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateRight: 'clamp',
});

// 地图路线动画：随帧数推进，路线逐渐延伸
const progress = interpolate(frame, [0, 150], [0, 1], {
  extrapolateRight: 'clamp',
});
```

<div class="mt-4 card" style="text-align:center;font-size:0.9rem;padding:.8rem;">
  <code>interpolate(frame, [起始帧, 结束帧], [起始值, 结束值])</code>
  <div style="font-size:0.78rem;color:#78716C;margin-top:.4rem;">就这一个函数，能做渐显、移动、缩放、路线延伸等各种动画</div>
</div>

---

## 类比：传统剪辑 vs Remotion

<table class="mt-5" style="font-size:0.82rem;">
  <thead>
    <tr>
      <th style="width:140px;">操作</th>
      <th>传统剪辑（剪映/Premiere）</th>
      <th>Remotion</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>时间线</strong></td>
      <td>手动拖拽</td>
      <td>Sequence 代码</td>
    </tr>
    <tr>
      <td><strong>关键帧</strong></td>
      <td>手动设置</td>
      <td>interpolate 函数</td>
    </tr>
    <tr>
      <td><strong>项目文件</strong></td>
      <td>.prproj 二进制文件</td>
      <td>React 代码 + JSON 数据</td>
    </tr>
    <tr>
      <td><strong>导出</strong></td>
      <td>点"导出"按钮</td>
      <td><code>npx remotion render</code></td>
    </tr>
    <tr>
      <td><strong>批量</strong></td>
      <td>不支持</td>
      <td>循环 + 数据库</td>
    </tr>
  </tbody>
</table>

<div class="mt-4 l-border" style="font-size:0.85rem;color:#1C2B4B;">
  不需要现在就会写React。今天的目标：<strong>理解三个概念</strong>，实操环节在模板上改数据就行。
</div>
