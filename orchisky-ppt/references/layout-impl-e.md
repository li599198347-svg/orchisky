# Layout Impl · E系版式实现（说明（Explain））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码来源：svg-skeleton-e.md。

---

## E1 · 单列信息流

```
内容列：x=40, y=120, width=880
每条要点（行高48px）：
  左侧小圆点 cx=52, cy=y+24, r=4, fill=brand-primary
  标题文字 x=68, y+32, font-size=14px, Bold, near-black
  说明文字 x=68, y+48, font-size=12px, gray
  分隔线 x=40, y+46, width=880, stroke=#F0F0F0
```

## E2 · 左右对比框

```
左框：x=40, y=112, width=416, height=380
  框标题 x=60, y=142, Bold 16px, brand-primary
  内容 x=60, y=170, 13px near-black, line-height=22px

分隔线：x=480, y=120, height=360, stroke=#E2E2E2

右框：x=496, y=112, width=424, height=380
  框标题 x=516, y=142, Bold 16px, brand-primary
  内容 x=516, y=170, 13px near-black
```

## E3 · 三列对比

```
列宽：272px，列间距：32px
列1：x=40
列2：x=344
列3：x=648

各列顶部色条：height=4, fill=brand-primary
列标题：y=132, Bold 15px, near-black
列内容：y=162, 12px, gray, line-height=20px
```

## E4 · 四展卡（2×2）

```
卡片宽：416px，卡片高：176px，间距：16px
左上：x=40, y=112
右上：x=504, y=112
左下：x=40, y=304
右下：x=504, y=304

卡内顶色条：height=3, fill=brand-primary
卡内标题：y+28, Bold 14px
卡内内容：y+52, 12px gray, line-height=20px
```
