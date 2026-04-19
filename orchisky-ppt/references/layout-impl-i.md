# Layout Impl · I系版式实现（震撼（Impact））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码来源：svg-skeleton-i.md。

---

## I1 · 大标题+小内容

```
大标题：
  x=40, y=180, width=560
  font-size=28px, Bold, near-black
  行高=40px

副标题/摘要：
  x=40, y=270, width=560
  font-size=15px, Regular, gray
  行高=24px

右侧装饰区：
  x=640, y=112, width=280, height=380
  fill=brand-primary, opacity=0.06, rx=4

关键数据标注：
  x=780 (居中), y=260
  font-size=40px, Bold, JetBrains Mono
  fill=brand-primary
单位说明：
  x=780, y=300, font-size=13px, gray
```

## I2 · 左大块+右要点

```
左侧主区：x=40, y=112, width=500
  大标题 y=190, 24px Bold
  副文字 y=240, 13px gray, line-height=22px

分隔线：x=564, y=130, height=340, stroke=#E2E2E2

右侧要点列：x=580, y=130
  每条要点行高48px：
    圆点 cx=590, r=3, fill=brand-primary
    文字 x=606, 13px near-black
```

## I3 · 全页文字强调

```
主语块：x=40, y=160, width=880, text-anchor=middle
  font-size=22px, Bold, near-black
  行高=32px
  关键词高亮：<tspan fill=brand-primary>关键词</tspan>

引用来源：
  x=480, y=440, text-anchor=middle
  font-size=11px, gray
  格式：—姓名，职务或来源
```

## I4 · 数据震撼卡（3个指标）

```
3个数据卡水平排列：
  卡宽=260px, 卡高=160px, 间距=30px
  卡1：x=40, y=196
  卡2：x=330, y=196
  卡3：x=620, y=196

  卡内大数字：text-anchor=middle, x=卡x+130, y=卡y+60
    font-size=36px, Bold, JetBrains Mono, fill=brand-primary
  卡内说明：text-anchor=middle, x=卡x+130, y=卡y+92
    font-size=12px, gray
  卡内顶色条：height=3, fill=brand-primary
```
