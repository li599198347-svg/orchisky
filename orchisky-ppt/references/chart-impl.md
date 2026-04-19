# 图表 SVG 实现模板

对应 orchisky.md 第7.5节的图表规范，提供各图表类型的精确SVG绘制代码。

## 图表通用規则

- 禁用：饼图 / 环形图 / 3D图表
- 数据直接标注在图表旁边，无独立图例
- 主色 `var(--brand-primary)` = 品牌主色
- 分层色 2: `var(--brand-secondary)` = 品牌辅色
- 所有数字标注使用 Songti SC,SimSun,serif 字体

## 柱状图 SVG 模板

```svg
<!-- 柱状图（单组，最多5个数据点）-->
<g id="bar-chart">
  <!-- 坐标轴 -->
  <line x1="60" y1="320" x2="680" y2="320" stroke="#E2E2E2" stroke-width="1"/>
  <line x1="60" y1="80" x2="60" y2="320" stroke="#E2E2E2" stroke-width="1"/>
  
  <!-- 横向网格 -->
  <line x1="60" y1="200" x2="680" y2="200" stroke="#F0F0F0" stroke-width="0.5" stroke-dasharray="4,4"/>
  <line x1="60" y1="140" x2="680" y2="140" stroke="#F0F0F0" stroke-width="0.5" stroke-dasharray="4,4"/>
  
  <!-- 柱子 -->
  <rect x="100" y="160" width="60" height="160" fill="var(--brand-primary)" opacity="1"/>
  <rect x="220" y="120" width="60" height="200" fill="var(--brand-primary)" opacity="1"/>
  <rect x="340" y="200" width="60" height="120" fill="var(--brand-primary)" opacity="0.7"/>
  <rect x="460" y="100" width="60" height="220" fill="var(--brand-primary)" opacity="1"/>
  <rect x="580" y="180" width="60" height="140" fill="var(--brand-primary)" opacity="0.7"/>
  
  <!-- 数据标注 -->
  <text x="130" y="150" font-family="JetBrains Mono,monospace" font-size="11" fill="#1A1A1A" text-anchor="middle">42%</text>
  <text x="250" y="110" font-family="JetBrains Mono,monospace" font-size="11" fill="#1A1A1A" text-anchor="middle">58%</text>
  <text x="370" y="190" font-family="JetBrains Mono,monospace" font-size="11" fill="#1A1A1A" text-anchor="middle">31%</text>
  <text x="490" y="90" font-family="JetBrains Mono,monospace" font-size="11" fill="#1A1A1A" text-anchor="middle">63%</text>
  <text x="610" y="170" font-family="JetBrains Mono,monospace" font-size="11" fill="#1A1A1A" text-anchor="middle">38%</text>
  
  <!-- X轴标签 -->
  <text x="130" y="340" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#555" text-anchor="middle">一季度</text>
  <text x="250" y="340" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#555" text-anchor="middle">二季度</text>
  <text x="370" y="340" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#555" text-anchor="middle">三季度</text>
  <text x="490" y="340" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#555" text-anchor="middle">四季度</text>
  <text x="610" y="340" font-family="Microsoft YaHei,sans-serif" font-size="10" fill="#555" text-anchor="middle">全年</text>
</g>
```

## 折线图 SVG 模板

```svg
<!-- 折线图（时序趋势）-->
<g id="line-chart">
  <!-- 坐标轴 -->
  <line x1="60" y1="320" x2="680" y2="320" stroke="#E2E2E2" stroke-width="1"/>
  
  <!-- 网格线 -->
  <line x1="60" y1="240" x2="680" y2="240" stroke="#F0F0F0" stroke-width="0.5" stroke-dasharray="4,4"/>
  <line x1="60" y1="180" x2="680" y2="180" stroke="#F0F0F0" stroke-width="0.5" stroke-dasharray="4,4"/>
  <line x1="60" y1="120" x2="680" y2="120" stroke="#F0F0F0" stroke-width="0.5" stroke-dasharray="4,4"/>
  
  <!-- 折线 -->
  <polyline points="100,280 220,220 340,240 460,160 580,140 660,100" 
            fill="none" stroke="var(--brand-primary)" stroke-width="2"/>
  
  <!-- 数据点 -->
  <circle cx="100" cy="280" r="4" fill="var(--brand-primary)"/>
  <circle cx="220" cy="220" r="4" fill="var(--brand-primary)"/>
  <circle cx="340" cy="240" r="4" fill="var(--brand-primary)"/>
  <circle cx="460" cy="160" r="4" fill="var(--brand-primary)"/>
  <circle cx="580" cy="140" r="4" fill="var(--brand-primary)"/>
  <circle cx="660" cy="100" r="4" fill="var(--brand-primary)"/>
  
  <!-- 数据标注 -->
  <text x="100" y="270" font-family="JetBrains Mono,monospace" font-size="10" fill="#1A1A1A" text-anchor="middle">1.2M</text>
  <text x="660" y="90" font-family="JetBrains Mono,monospace" font-size="10" fill="var(--brand-primary)" text-anchor="middle">3.8M</text>
</g>
```

## 水平进度条 SVG 模板

```svg
<!-- 水平进度条（达成率）-->
<g id="progress-bars">
  <!-- 条目1 -->
  <text x="60" y="110" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#1A1A1A">市场占有率</text>
  <rect x="200" y="95" width="400" height="14" rx="2" fill="#F0F0F0"/>
  <rect x="200" y="95" width="268" height="14" rx="2" fill="var(--brand-primary)"/>
  <text x="615" y="108" font-family="JetBrains Mono,monospace" font-size="12" fill="var(--brand-primary)">67%</text>
  
  <!-- 条目2 -->
  <text x="60" y="150" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#1A1A1A">客户满意度</text>
  <rect x="200" y="135" width="400" height="14" rx="2" fill="#F0F0F0"/>
  <rect x="200" y="135" width="340" height="14" rx="2" fill="var(--brand-primary)"/>
  <text x="615" y="148" font-family="JetBrains Mono,monospace" font-size="12" fill="var(--brand-primary)">85%</text>
  
  <!-- 条目3 -->
  <text x="60" y="190" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#1A1A1A">项目达成率</text>
  <rect x="200" y="175" width="400" height="14" rx="2" fill="#F0F0F0"/>
  <rect x="200" y="175" width="308" height="14" rx="2" fill="var(--brand-primary)"/>
  <text x="615" y="188" font-family="JetBrains Mono,monospace" font-size="12" fill="var(--brand-primary)">77%</text>
</g>
```

## 他表规范总则

1. 所有图表必须在SVG内直接标注数据值，不得出现独立图例
2. Y轴标签用简化单位（M=百万, K=千）
3. 颜色只用主色和其透明度变化（禁用第二装饰色）
4. 柱状图柱子宽度：数据点间距的 50-60%
5. 折线图线宽 2px，数据点半径 4px
6. 进度条高度 14px，圆角 2px
