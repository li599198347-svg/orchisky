# Layout Impl · S系版式实现（结构（Structure））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。

---

## S1 · 水平流程（最多5步）

```
步骤块（最多5个）水平排列，行内居中 y=252：
  块宽=160px, 块高=100px
  间距=20px（含箭头区）
  左对齐起点 x=40

  块背景：
    激活步骤 fill=brand-primary
    其他步骤 fill=#F0F0F0
  块圆角：rx=4
  步骤编号：14px Bold 白色（激活）/ 灰色（非激活）
  步骤文字：12px 居中，白色（激活）/ near-black（非激活）

  箭头（块间）：三角形 fill=#E2E2E2, width=16px
```

## S2 · 垂直列表

```
每条48px行高，从 y=120 开始：
  编号圈 cx=56, cy=y+24, r=16, fill=brand-primary
  编号 14px Bold 白色 居中
  标题 x=84, y+20, 14px Bold near-black
  说明 x=84, y+38, 12px gray
  分隔线 x=40, y+46, width=880, stroke=#F0F0F0
```

## S3 · 模块卡片组（2×2或1×3）

```
2×2布局：
  卡片宽=416px, 高=176px
  左上：x=40, y=112
  右上：x=504, y=112
  左下：x=40, y=304
  右下：x=504, y=304

1×3布局：
  卡片宽=272px, 高=276px
  间距=32px
  卡1：x=40, y=166
  卡2：x=344, y=166
  卡3：x=648, y=166

卡内顶色条：height=3, fill=brand-primary
卡内图标区：40×40px
卡内标题：14px Bold
卡内内容：12px gray, line-height=20px
```
