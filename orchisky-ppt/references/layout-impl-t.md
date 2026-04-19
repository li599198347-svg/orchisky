# Layout Impl · T系版式实现（过渡（Transition））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码：svg-skeleton-t.md。

---

# T 系 · 过渡类（Transition）

共同特征：极少信息，多留白，情绪承接，信息密度 10-25%。

## T-01 深色引言页

**适用**：章节间过渡、情绪承接、关键观点引言

```svg
<rect width="1280" height="720" fill="#0A1F3A"/>
<text x="120" y="320" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#FFFFFF">[quote_line_1]</text>
<text x="120" y="370" font-family="Songti SC,SimSun,serif" font-size="36" font-weight="bold" fill="#FFFFFF">[quote_line_2]</text>
<text x="120" y="450" font-family="Songti SC,SimSun,serif" font-size="24" fill="#B8C8D8">[sub_line]</text>
<text x="1200" y="640" text-anchor="end" font-size="13" fill="#6B86A8">—— [source]</text>
```

信息密度：15%

## T-02 白底大字宣言

**适用**：战略宣言、核心观点、一句话承诺

```svg
<text x="640" y="340" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="#1A1A1A">[declaration_line_1]</text>
<text x="640" y="394" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="44" font-weight="bold" fill="#1A1A1A">[declaration_line_2]</text>
<line x1="580" y1="440" x2="700" y2="440" stroke="#003D7A" stroke-width="2.5"/>
<text x="640" y="490" text-anchor="middle" font-size="16" fill="#666">[sub_note]</text>
```

信息密度：15%

## T-03 章节承接页

**适用**：Part 之间的过渡，明确“刚才讲了什么，接下来讲什么”

```svg
<!-- 左侧：已完成的部分 -->
<text x="100" y="260" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#888">[Part 1 · 回顾]</text>
<text x="100" y="300" font-size="14" fill="#555">[summary_of_previous]</text>
<!-- 中间：即将开始的部分 -->
<text x="640" y="470" text-anchor="middle" font-family="Songti SC,SimSun,serif" font-size="40" font-weight="bold" fill="#003D7A">[Part 2 标题]</text>
<line x1="540" y1="510" x2="740" y2="510" stroke="#003D7A" stroke-width="2"/>
```

信息密度：25%
