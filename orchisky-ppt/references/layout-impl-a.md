# Layout Impl · A系版式实现（动作（Action））

> Phase 7 按版式ID读取本文件获取坐标和实现细节。
> 坐标权威来源：grid-system.md。
> SVG骨架代码：svg-skeleton-a.md。

---

# A 系 · 动作类（Action）

共同特征：推动决策和行动，信息密度 50-70%。

## A-01 下一步三步决策

```svg
<!-- 三步行动卡 x=40/456/872, y=200, w=400, h=360 -->
<rect x="40" y="200" width="400" height="360" fill="#F5F5F5"/>
<rect x="40" y="200" width="4" height="360" fill="#003D7A"/>
<text x="60" y="232" font-size="11" fill="#003D7A" letter-spacing="3">STEP 01 · 本周</text>
<text x="60" y="272" font-family="Songti SC,SimSun,serif" font-size="22" font-weight="bold" fill="#1A1A1A">[step_1_action]</text>
<text x="60" y="300" font-size="13" fill="#555">[step_1_detail]</text>
```

信息密度：60%

## A-02 是/否选择矩阵

```svg
<!-- 上半：选择 A -->
<rect x="40" y="140" width="1200" height="240" fill="#E8F0FA"/>
<rect x="40" y="140" width="4" height="240" fill="#003D7A"/>
<text x="60" y="172" font-size="11" fill="#003D7A" letter-spacing="3">OPTION A · 推荐</text>
<text x="60" y="220" font-family="Songti SC,SimSun,serif" font-size="28" font-weight="bold" fill="#1A1A1A">[option_a]</text>
<!-- 下半：选择 B -->
<rect x="40" y="420" width="1200" height="240" fill="#F5F5F5"/>
<rect x="40" y="420" width="4" height="240" fill="#888"/>
```

信息密度：55%

## A-03 责任矩阵

```svg
<!-- 表头 -->
<rect x="40" y="140" width="1200" height="44" fill="#1A1A1A"/>
<text x="60" y="168" font-size="12" font-weight="bold" fill="#FFF">行动</text>
<text x="660" y="168" font-size="12" font-weight="bold" fill="#FFF">责任方</text>
<text x="960" y="168" font-size="12" font-weight="bold" fill="#FFF">截止时间</text>
<!-- N 行（每行 y 递增 60） -->
<rect x="40" y="184" width="1200" height="60" fill="#FAFAFA"/>
<text x="60" y="212" font-size="14" font-weight="bold" fill="#1A1A1A">[action_1]</text>
<text x="660" y="218" font-size="13" fill="#333">[owner_1]</text>
<text x="960" y="218" font-size="13" font-weight="bold" fill="#B01C1C">[deadline_1]</text>
```

信息密度：65%
