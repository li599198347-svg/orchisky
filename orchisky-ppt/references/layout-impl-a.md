# Layout Impl · A系版式实现（动作（Action））

> Phase 7 按版式ID读取本文件获取坐标和设计要求。

---

## A1 · 封面页

```
封面标题：
  x=40, y=200, width=600
  font-size: 36px, Bold
  fill: var(--brand-near-black)

副标题：
  x=40, y=260, width=600
  font-size: 18px, Regular
  fill: var(--brand-gray-medium)

汇报日期和报告人：
  x=40, y=340
  font-size: 13px
  fill: var(--brand-gray-light)

装饰条：
  x=40, y=380, width=120, height=3
  fill: var(--brand-primary)
```

## A2 · 过渡页

```
大标题：
  x=40, y=220, width=880
  font-size: 28px, Bold, 居中对齐
  fill: var(--brand-near-black)

左侧竖线（常规 Chrome）已包含 Action Title 竖线
内容区居中显示
```

## A3 · 总结页

```
结论标题：
  x=40, y=160, width=880, text-anchor=middle
  font-size: 24px, Bold
  fill: var(--brand-near-black)

核心行动号召：
  x=40, y=240
  font-size: 16px
  fill: var(--brand-primary)

联系方式区：
  x=40, y=380
  font-size: 12px
  fill: var(--brand-gray-medium)
```
