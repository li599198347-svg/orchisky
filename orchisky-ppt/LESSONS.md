# LESSONS · 经验积累文档

> **注意：本文件不在运行时加载链路中，不会消耗token。**
> 本文件是供人类阅读的经验积累，包含方法论场景索引和工具链技术细节。

---

## 📍 必问探测类（场景 1-12）

| # | 场景 | Trigger Point |
|---|---|---|
| 1 | 规模语境校准 | 进入 Phase 1 调研前 |
| 2 | 受众心理动线建模 | Phase 2 Ghost Deck 前 |
| 3 | 第三章灵魂页开放性取向探测 | 设计方案 Part 核心框架前 |
| 7 | 成长带诚实性校验 | 方案涉及未来规划时 |

---

## 🎯 专业判断类（场景 13-14）

| # | 场景 | Trigger Point |
|---|---|---|
| 13 | “懂客户”的专业边界 | 涉及“延续 vs 重构”决策时 |
| 14 | 甲乙方责任边界判断 | 涉及“谁来做”的分工时 |

---

## 🎨 规范执行类（场景 15）

| # | 场景 | Trigger Point |
|---|---|---|
| 15 | 颜色使用必须从品牌规范读取 | 设计任何涉及颜色的页面 |

**四项强制纪律**：
1. 前置读取 orchisky.md §2/§3/§7
2. designer 阶段硬性查表
3. QC 阶段强制合规审计
4. Skill 文档内容严禁具体色值

---

## 🔧 工程教训类（场景 19-23）

| # | 场景 | Trigger Point |
|---|---|---|
| 19 | 大规模 QC 工具预算规划 | 50+ 页 SVG/PPT 的视觉 QC |
| 20 | SVG 为真源原则 | 任何需要输出多种格式的交付任务 |
| 21 | EMF 嵌入不可用于"可编辑"承诺 | 用户要求"可编辑 PPT" |
| 22 | 通用 SVG→PPT 转换器的坑 | 想自己写简单转换器时 |
| 23 | 深度调研再动手 | 遇到反复踩坑的技术问题 |

---

## 工具链技术细节（供调试参考）

ppt-master 工具链的核心创新（在 `assets/svg_to_pptx/drawingml_elements.py`）：

```python
# baseline 偏移系数（经验值）
box_y = svg_y - font_size * 0.85

# 字符级精确宽度估算
def estimate_text_width(text, size, weight):
    width = 0
    for ch in text:
        if is_cjk_char(ch):
            width += size          # 中文 = 1em
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
