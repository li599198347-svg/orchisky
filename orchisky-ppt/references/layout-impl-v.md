# Layout Impl · V系版式实现（证据（Evidence））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。

---

## V1 · 证据清单

```
内容区 x=40, y=120, width=880
每条证据60px行高：
  勾符号 x=48, font-size=16px, fill=brand-primary, Bold
  证据文字 x=72, y+20, 13px near-black
  来源 x=72, y+38, 11px gray
  分隔线 x=40, y+56, width=880, stroke=#F0F0F0
```

## V2 · 引用卡

```
卡片 x=120, y=140, width=720, height=260
  fill=#F8F8F8, rx=4, stroke=#E2E2E2

左竖线：x=120, y=160, width=4, height=220
  fill=brand-primary

引号装饰（可选）：
  x=148, y=180, font-size=48px, fill=brand-primary, opacity=0.2
  内容："

引用文字：
  x=148, y=210, width=660
  font-size=18px, 引用字体（Songti SC）
  fill=near-black, line-height=28px

作者署名：
  x=148, y=370, font-size=13px, gray
  格式：—姓名，职务
```
