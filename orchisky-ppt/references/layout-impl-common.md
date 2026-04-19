# Layout Impl · 通用规范（画布/Chrome/卡片/字数表/版式选择参考）

> Phase 5 选版式时读取本文件的版式选择参考表。
> Phase 7 设计时读取本文件的Chrome/卡片规范和字数限制。

---

## 画布与Chrome规范

```
画布：960×540px
Action Title 区：
  左竖线 x=40, y=48, height=48, width=3, fill=brand-primary
  文字 x=52, y=72, font-size=22px, Bold
内容区：y=112 到 y=492，宽 880px（x=40到x=920）
底带：y=492, height=48, fill=brand-primary
  页码：x=880, y=514, font-size=12px, fill=white
  公司名：x=48, y=514, font-size=13px, fill=white
```

---

## 卡片组件规范

```
卡片圆角：rx=4
卡片背景：#F8F8F8 或 white
卡片边框：stroke=#E2E2E2, stroke-width=1
卡片内边距：20px
```

---

## 版式选择参考表

| 内容类型 | 首选版式 | 备选 |
|---------|----------|------|
| 封面页 | A1 | - |
| 过渡页 | A2 | T1 |
| 总结页 | A3 | - |
| 数据图表 | G1 | G2/G3 |
| 对比分析 | E2 | E3 |
| 文字论述 | I1/I3 | S2/S3 |
| 流程步骤 | S1/S3 | I4 |
| 价值展示 | V1/V2 | - |

---

## 单页内容字数限制

| 交付模式 | 要点数 | 单要点最大字数 |
|---------|--------|----------------|
| Presenting | ≤3 | 20字 |
| Hybrid | 3-5 | 30字 |
| Reading | 5-7 | 50字 |
