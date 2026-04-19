# Layout Impl · T系版式实现（过渡（Transition））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。

---

## T1 · 节动封面

```
背景色块：x=0, y=0, width=960, height=540
  fill=brand-primary, opacity=0.08

左侧竖边块：x=0, y=0, width=8, height=540
  fill=brand-primary

章节编号（大号水印）：
  x=480, y=220, text-anchor=middle
  font-size=64px, Bold, fill=brand-primary, opacity=0.15

章节标题：
  x=480, y=290, text-anchor=middle
  font-size=28px, Bold, near-black

章节副题（可选）：
  x=480, y=330, text-anchor=middle
  font-size=15px, gray
```

## T2 · 章节目录

```
标题区：
  x=40, y=150, font-size=24px Bold, near-black
  "本章内容"

条目列表（y=210起，每条40px行高）：
  编号圈 cx=52, r=12, fill=brand-primary（当前章）/ #E0E0E0（其他）
  编号 12px Bold 白色 居中
  文字 x=76, 14px near-black
  当前章文字加粗 + fill=brand-primary
```
