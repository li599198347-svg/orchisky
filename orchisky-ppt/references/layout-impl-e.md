# Layout Impl · E系版式实现（说明（Explain））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。SVG骨架代码：svg-skeleton-e.md。

---

# E 系 · 说明类（Explain）

**共同特征**：用图示承担主要信息，文字为辅，信息密度 50-75%

## E-01 左图右文（55:45）

```
图：x=40  y=140 w=660 h=480
文：x=740 y=140 w=500 h=480
```

**信息密度**：55%

## E-02 概念曲线图

```svg
<line x1="140" y1="540" x2="140" y2="220" stroke="#1A1A1A" stroke-width="2"/>
<line x1="140" y1="540" x2="800" y2="540" stroke="#1A1A1A" stroke-width="2"/>
<path d="M 160 520 Q 220 500, 280 440 T 360 370"
      stroke="#1A7A42" stroke-width="4.5" fill="none"/>
<path d="M 360 370 Q 440 340, 500 335 T 580 360"
      stroke="#9A5200" stroke-width="4.5" fill="none"/>
<path d="M 580 360 Q 650 320, 720 270"
      stroke="#003D7A" stroke-width="4.5" fill="none" stroke-dasharray="6,4"/>
<circle cx="580" cy="360" r="11" fill="#B01C1C"/>
<text x="560" y="244" font-size="12" font-weight="bold" fill="#B01C1C">★ 当前位置</text>
```

**信息密度**：60%

## E-03 流程示意图

```svg
<rect x="80" y="280" width="180" height="80" fill="#F5F5F5" stroke="#003D7A" stroke-width="1.5"/>
<text x="170" y="308" text-anchor="middle" font-size="12" font-weight="bold" fill="#003D7A">STAGE 1</text>
<text x="170" y="332" text-anchor="middle" font-size="14" font-weight="bold" fill="#1A1A1A">[\u9636\u6bb51]</text>
<line x1="260" y1="320" x2="330" y2="320" stroke="#003D7A" stroke-width="2"/>
<polygon points="330,320 322,316 322,324" fill="#003D7A"/>
```

**信息密度**：60%

## E-04 架构层次图

```svg
<rect x="240" y="140" width="800" height="110" fill="#003D7A"/>
<text x="640" y="212" text-anchor="middle" font-family="Songti SC,SimSun,serif"
      font-size="22" font-weight="bold" fill="#FFF">[顶层]</text>
<line x1="640" y1="250" x2="640" y2="310" stroke="#003D7A" stroke-width="2"/>
<rect x="240" y="310" width="800" height="110" fill="#B01C1C"/>
<rect x="240" y="480" width="800" height="110" fill="#3A7FC1"/>
```

**信息密度**：65%

---
