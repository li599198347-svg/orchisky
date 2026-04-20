# LESSONS · 经验积累文档

> **注意：本文件不在运行时加载链路中，不会消耗token。**
> 本文件是供人类阅读的经验积累，包含方法论场景索引和工具链技术细节。
> AI执行时不需要读取本文件，所有执行规则已分散到对应的Phase文件和references中。

---

> 本文件是技能的**方法论索引**。24 个场景来源于多次项目实战,每个配 Trigger Point 和跳转链接。
> **使用方式**:在对应阶段或遇到对应信号时,跳转到具体 reference 读完整内容。

---

## 📍 必问探测类(场景 1-12)

**文件**:`references/probing-scenarios.md`

### 强制 4 场景(Phase 0.5 必问)

| # | 场景 | Trigger Point |
|---|---|---|
| 1 | 规模语境校准 | 进入 Phase 1 调研前 |
| 2 | 受众心理动线建模 | Phase 2 Ghost Deck 前 |
| 3 | ★ 第三章灵魂页开放性取向探测 | 设计方案 Part 核心框架前(最重要) |
| 7 | 成长带诚实性校验 | 方案涉及未来规划/远景时 |

### 可选 8 场景(按需触发)

| # | 场景 | Trigger Point |
|---|---|---|
| 4 | 诊断页问题定性校准 | 设计"现状诊断"类内容页前 |
| 5 | 多概念并列结构辨识 | 出现"XX+YY"并列时 |
| 6 | 数字/承诺诚实度校验 | 方案里出现任何具体数字时 |
| 8 | 节奏类型确认 | Phase 4 策划版式前 |
| 9 | 战略轴心页上下和合 | 设计轴心页时 |
| 10 | 跨 Part 呼应锁点埋设 | Phase 4 策划跨 Part 呼应时 |
| 11 | bullets 风格场景匹配 | Phase 3 填充 bullets 时 |
| 12 | ★ 矛盾一致性全扫描 | Phase 6 QC 交付前最后一关 |

---

## 🎯 专业判断类(场景 13-14)

**文件**:`references/professional-judgment.md`

| # | 场景 | Trigger Point |
|---|---|---|
| 13 | ★ "懂客户"的专业边界(极易滑向讨好) | 涉及"延续 vs 重构"决策时 |
| 14 | ★ 甲乙方责任边界判断(不揃活也是专业) | 涉及"谁来做"的分工时 |

**核心原则**:专业判断不搬家。知道哪些事不该做,和知道哪些事该做,同等重要。

---

## 🎨 规范执行类(场景 15 + 架构修正)

**文件**:`references/brand-discipline.md`

| # | 场景 | Trigger Point |
|---|---|---|
| 15 | ★★ 颜色使用必须从品牌规范读取,不得自定义 | 设计任何涉及颜色的页面 |
| — | 架构级修正:orchisky.md 作为唯一真源 | 全技能生命周期 |

**四项强制纪律**:
1. 前置读取 orchisky.md §2/§3/§7
2. designer 阶段硬性查表
3. QC 阶段强制合规审计
4. Skill 文档内容严禁具体色值

---

## 🔧 工程教训类(场景 19-23)

**文件**:`references/engineering-lessons.md`

| # | 场景 | Trigger Point |
|---|---|---|
| 19 | ★ 大规模 QC 工具预算规划 | 50+ 页 SVG/PPT 的视觉 QC |
| 20 | ★★★ SVG 为真源原则 | 任何需要输出多种格式的交付任务 |
| 21 | ★ EMF 嵌入不可用于"可编辑"承诺 | 用户要求"可编辑 PPT""原生形状" |
| 22 | ★★ 通用 SVG→PPT 转换器的坑 | 想自己写简单 SVG→PPT 转换器时 |
| 23 | ★★ 深度调研再动手 | 遇到反复踩坑的技术问题 |

---

## 📖 使用索引

### 按执行阶段查找

| 阶段 | 必读场景 |
|---|---|
| Phase 0.5 | 1, 2, 3, 7(强制 4 场景) |
| Phase 0.5b | 15(规范真源) |
| Phase 1 调研 | 13(继承/重构判断) |
| Phase 2 叙事 | 10(跨 Part 呼应) |
| Phase 3 大纲 | 4(诊断定性)、8(bullets 风格)、14(甲乙方分工) |
| Phase 4 策划 | 5(多概念辨识)、8(节奏类型)、9(轴心和合) |
| Phase 5 SVG | 15(颜色真源) |
| Phase 5.5 PPT | 20, 21, 22(SVG 真源/可编辑纪律/不要自己写转换器) |
| Phase 6 QC | 6(数字诚实)、12(矛盾扫描)、19(QC 预算) |

---

## 工具链技术细节（供调试参考）

ppt-master 工具链的核心创新(`assets/svg_to_pptx/drawingml_elements.py`):

```python
# baseline 偏移系数(经验值)
box_y = svg_y - font_size * 0.85

# 字符级精确宽度估算
def estimate_text_width(text, size, weight):
    width = 0
    for ch in text:
        if is_cjk_char(ch):
            width += size
        elif ch == ' ':
            width += size * 0.3
        elif ch in 'mMwWOQ':
            width += size * 0.75
        elif ch in 'iIlj1!|':
            width += size * 0.3
        else:
            width += size * 0.55
    if weight in ('bold', '600', '700', '800', '900'):
        width *= 1.05
    return width
```

详细实现见 `assets/svg_to_pptx/` 源码。
