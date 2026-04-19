# Layout Impl · T系版式实现（过渡（Transition））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。

---

## T系总览

T系 = 过渡型版式。用于章节间隔、议题切换、过渡页。

| 版式ID | 名称 | 适用场景 |
|--------|------|----------|
| T-1 | 章节过渡 | 章节开头页 |
| T-2 | 议题切换 | 议题过渡页 |
| T-3 | 全号提问 | 以问题引入新议题 |

---

## T-1 章节过渡

```svg
<!-- 左侧蓝色块 -->
<rect x="0" y="0" width="480" height="720" fill="#003D7A"/>

<!-- 章节序号 -->
<text x="60" y="240" font-size="80" font-weight="bold"
      fill="rgba(255,255,255,.15)">[N]</text>

<!-- 章节标题 -->
<text x="60" y="340" font-family="Songti SC,SimSun,serif"
      font-size="36" font-weight="bold" fill="#FFFFFF">[chapter_title]</text>

<!-- 右侧内容预览 -->
<text x="540" y="320" font-size="14" fill="#888">本章要点</text>
<text x="540" y="360" font-size="14" fill="#333">• [point_1]</text>
<text x="540" y="390" font-size="14" fill="#333">• [point_2]</text>
<text x="540" y="420" font-size="14" fill="#333">• [point_3]</text>
```

**信息密度**：35%

## T-2 议题切换

```svg
<!-- 项目名称 -->
<text x="640" y="300" text-anchor="middle"
      font-family="Songti SC,SimSun,serif"
      font-size="48" font-weight="bold" fill="#1A1A1A">[topic_title]</text>

<!-- 进度指示 -->
<text x="640" y="380" text-anchor="middle"
      font-size="13" fill="#888" letter-spacing="4">[current] / [total]</text>
```

**信息密度**：20%

---

*坐标权威来源：grid-system.md · SVG骨架：svg-skeleton-t.md*
