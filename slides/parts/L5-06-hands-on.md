---
layout: default
---

<div class="h-full flex flex-col justify-center" style="background:#1C2B4B;margin:-6rem;padding:6rem;">
  <div class="section-num">05</div>
  <div style="color:white;font-size:2rem;font-weight:700;margin-top:0.5rem;">课堂实操</div>
  <div class="gold-line" style="width:80px;margin-top:1rem;"></div>
  <div style="color:#94A3B8;font-size:0.9rem;margin-top:0.75rem;">搭建环境 · 制作丝路城市介绍视频</div>
</div>

---

## 环境准备

<div class="mt-4 grid grid-cols-2 gap-3" style="font-size:0.82rem;">

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">Step 1 · 检查 Node.js</div>
  <code>node -v</code> → 需要 18+<br>
  <span style="color:#78716C;">推荐 20 LTS 版本</span>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">Step 2 · 创建项目</div>
  <code>npx create-video@latest silk-road-video</code>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">Step 3 · 进入目录</div>
  <code>cd silk-road-video</code>
</div>

<div class="card">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.5rem;">Step 4 · 启动 Studio</div>
  <code>npx remotion studio</code><br>
  <span style="color:#78716C;">浏览器自动打开预览</span>
</div>

</div>

<div class="mt-3" style="font-size:0.78rem;padding:.5rem .8rem;background:rgba(184,134,11,.08);border-radius:4px;">
  <strong style="color:#B8860B;">网络问题备案</strong>：教师提前准备好已安装依赖的模板压缩包，学生解压后直接 <code>npx remotion studio</code>
</div>

---

## 教师演示：丝路城市介绍视频

<div class="mt-3" style="font-size:0.82rem;color:#78716C;">目标：30秒视频，介绍长安、敦煌、撒马尔罕三座城市</div>

<div class="mt-4 grid grid-cols-2 gap-4">

<div>
<div style="font-weight:700;color:#B8860B;margin-bottom:.8rem;">数据文件 cities.json</div>

```json
[
  {
    "name": "长安",
    "nameEn": "Chang'an",
    "description": "丝绸之路的东方起点",
    "year": "公元前138年"
  },
  {
    "name": "敦煌",
    "nameEn": "Dunhuang",
    "description": "东西方文明交汇的艺术宝库",
    "year": "公元前111年"
  }
]
```

</div>

<div>
<div style="font-weight:700;color:#B8860B;margin-bottom:.8rem;">制作步骤</div>
<div style="font-size:0.82rem;line-height:2;">
  <strong>1.</strong> 准备 cities.json 数据<br>
  <strong>2.</strong> 创建 CityCard 组件（渐显动画）<br>
  <strong>3.</strong> 用 Sequence 编排出场顺序<br>
  <strong>4.</strong> 在 Studio 中实时预览<br>
  <strong>5.</strong> <code>npx remotion render</code> 输出MP4
</div>
</div>

</div>

---

## 关键演示：修改的威力

<div class="mt-5 grid grid-cols-2 gap-5">

<div class="card" style="text-align:center;">
  <div style="font-weight:700;color:#78716C;margin-bottom:.8rem;">用剪映改一个字</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.8;">
    打开项目文件<br>
    找到文字层<br>
    修改文字<br>
    重新导出<br>
    <strong>× 30条视频 = 重复30次</strong>
  </div>
</div>

<div class="card" style="text-align:center;border-color:#B8860B;">
  <div style="font-weight:700;color:#B8860B;margin-bottom:.8rem;">用 Remotion 改一个字</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.8;">
    打开 JSON 文件<br>
    改一行文字<br>
    运行渲染命令<br>
    <strong>3秒出新视频</strong><br>
    <strong>30条视频自动同步</strong>
  </div>
</div>

</div>

<div class="mt-4 l-border" style="font-size:0.85rem;color:#1C2B4B;">
  出英文版？把 JSON 换成英文数据文件，运行同一行命令。<strong>零额外工作量。</strong>
</div>

---

## 学生练习

<div class="mt-3" style="font-size:0.82rem;color:#78716C;">基于教师模板修改，不要求从零编写代码</div>

<div class="mt-4 grid grid-cols-2 gap-4">

<div class="card" style="border-color:#B8860B;">
  <div style="font-size:0.72rem;color:#B8860B;font-weight:600;letter-spacing:.1em;margin-bottom:.5rem;">任务</div>
  <div style="font-weight:600;margin-bottom:.5rem;">修改数据，渲染丝路主题视频</div>
  <div style="font-size:0.78rem;color:#78716C;line-height:1.7;">
    1. 克隆模板 + <code>npm install</code><br>
    2. 修改 data.json 的内容<br>
    3. 调整样式（颜色、字号）<br>
    4. 修改 interpolate 参数看变化<br>
    5. <code>npx remotion render</code> 输出
  </div>
</div>

<div>
  <div style="font-weight:700;color:#B8860B;margin-bottom:.8rem;">可选主题</div>
  <div style="font-size:0.82rem;color:#78716C;line-height:1.8;">
    丝路上的三种商品（丝绸、香料、茶叶）<br>
    丝路上的三位历史人物<br>
    丝路上的三处世界遗产<br>
    丝路上的三种艺术形式
  </div>

  <div class="mt-4" style="font-size:0.78rem;padding:.5rem .8rem;background:rgba(184,134,11,.08);border-radius:4px;">
    <strong style="color:#B8860B;">加分</strong>：导入上节课的AI海报作背景，或做一个英文版
  </div>
</div>

</div>

---

## 生成失败怎么办？

<table class="mt-4" style="font-size:0.82rem;">
  <thead>
    <tr>
      <th>问题</th>
      <th>解决方案</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Node.js 版本不对</td>
      <td><code>node -v</code> 检查，需要 18+。两人共用一台电脑。</td>
    </tr>
    <tr>
      <td>npm install 超时</td>
      <td>使用教师准备的离线压缩包</td>
    </tr>
    <tr>
      <td>Studio 打不开</td>
      <td>检查端口占用，尝试 <code>npx remotion studio --port 3001</code></td>
    </tr>
    <tr>
      <td>渲染报错</td>
      <td>检查 JSON 格式（逗号、引号），确认图片路径正确</td>
    </tr>
  </tbody>
</table>
