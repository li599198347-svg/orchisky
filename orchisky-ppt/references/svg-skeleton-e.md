# SVG Skeleton · E系版式骨架（说明（Explain））

> Phase 7 按版式ID读取本文件。使用规则：复制骨架→替换[占位符]→不改坐标。
> 通用骨架（Chrome框架/卡片/箭头）见 svg-skeleton-common.md。

---

## E-01 左图右文（55:45）
```svg
<!-- 内容区 -->

<!-- 图形区：x=40 y=140 w=660 h=480 -->
<rect x="40" y="140" width="660" height="480" rx="4" fill="#F5F5F5" stroke="#E2E2E2" stroke-width="0.5"/>
<text x="370" y="388" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#AAAAAA">[此处替换为实际图形SVG代码]</text>

<!-- 右侧文字区：x=740 y=140 w=500 h=480 -->
<text x="740" y="172" font-family="Microsoft YaHei,sans-serif" font-size="11" fill="#003D7A" letter-spacing="2">[right_tag]</text>
<line x1="740" y1="182" x2="880" y2="182" stroke="#003D7A" stroke-width="1.5"/>
<text x="740" y="224" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[right_title]</text>
<line x1="740" y1="250" x2="1224" y2="250" stroke="#E2E2E2" stroke-width="0.5"/>
<rect x="740" y="270" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="752" y="280" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[bullet1]</text>
<rect x="740" y="294" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="752" y="304" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[bullet2]</text>
<rect x="740" y="318" width="3" height="14" rx="1" fill="#003D7A"/>
<text x="752" y="328" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#333333">[bullet3]</text>
```

---

## E-02 概念曲线图
```svg
<!-- 坐标轴 -->
<line x1="140" y1="560" x2="140" y2="180" stroke="#1A1A1A" stroke-width="2"/>
<line x1="140" y1="560" x2="820" y2="560" stroke="#1A1A1A" stroke-width="2"/>
<text x="60" y="178" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[y_label]</text>
<text x="830" y="566" font-family="Microsoft YaHei,sans-serif" font-size="12" fill="#555555">[x_label]</text>

<!-- 三段曲线 -->
<path d="M 160 540 Q 220 520, 280 460 T 380 390" stroke="#1A7A42" stroke-width="4.5" fill="none"/>
<path d="M 380 390 Q 450 360, 510 352 T 580 370" stroke="#9A5200" stroke-width="4.5" fill="none"/>
<path d="M 580 370 Q 650 330, 720 280" stroke="#003D7A" stroke-width="4.5" fill="none" stroke-dasharray="6,4"/>

<!-- 当前位置标记 -->
<circle cx="580" cy="370" r="11" fill="#B01C1C"/>
<text x="558" y="252" font-family="Microsoft YaHei,sans-serif" font-size="12" font-weight="bold" fill="#B01C1C">[current_label]</text>

<!-- 三阶段标签 -->
<text x="270" y="592" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A7A42">[stage1]</text>
<text x="460" y="592" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#9A5200">[stage2]</text>
<text x="650" y="592" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#003D7A">[stage3]</text>

<!-- 右侧结论 -->
<text x="900" y="290" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[conclusion_line1]</text>
<text x="900" y="326" font-family="Songti SC,SimSun,serif" font-size="24" font-weight="bold" fill="#1A1A1A">[conclusion_line2]</text>
<text x="900" y="372" font-family="Microsoft YaHei,sans-serif" font-size="13" fill="#555555">[desc]</text>
```

---

## E-03 流程示意图（箭头用polygon）
```svg
<!-- 阶段1：x=80 y=260 w=200 h=100 -->
<rect x="80" y="260" width="200" height="100" rx="4" fill="#F5F5F5" stroke="#003D7A" stroke-width="1.5"/>
<text x="180" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="#003D7A" letter-spacing="2">STAGE 01</text>
<text x="180" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[stage1_name]</text>

<!-- 箭头：阶段1→9阶段2 -->
<line x1="280" y1="310" x2="330" y2="310" stroke="#003D7A" stroke-width="2"/>
<polygon points="330,304 342,310 330,316" fill="#003D7A"/>

<!-- 阶段2：x=342 y=260 w=200 h=100 -->
<rect x="342" y="260" width="200" height="100" rx="4" fill="#F5F5F5" stroke="#003D7A" stroke-width="1.5"/>
<text x="442" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="#003D7A" letter-spacing="2">STAGE 02</text>
<text x="442" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#1A1A1A">[stage2_name]</text>

<!-- 箭头 -->
<line x1="542" y1="310" x2="592" y2="310" stroke="#003D7A" stroke-width="2"/>
<polygon points="592,304 604,310 592,316" fill="#003D7A"/>

<!-- 阶段3（激活）：x=604 y=260 w=200 h=100 -->
<rect x="604" y="260" width="200" height="100" rx="4" fill="#003D7A"/>
<text x="704" y="296" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="11" font-weight="bold" fill="#8AAED0" letter-spacing="2">STAGE 03</text>
<text x="704" y="326" text-anchor="middle" font-family="Microsoft YaHei,sans-serif" font-size="14" font-weight="bold" fill="#FFFFFF">[stage3_name]</text>
```
