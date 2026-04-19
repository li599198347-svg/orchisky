---
name: orchisky-ppt
version: V5.0
description: >-
  全流程AI制作PPT演示文稿技能，对标麦肯锡/德勤顶级咨询公司标准。
  当用户说"帮我做PPT""做演示文稿""做一个汇报""根据这份资料做PPT"
  "做客户方案PPT""制作幻灯片"时立即触发。即使只有一句话需求也触发。
  八阶段模块化流程：规范加载→材料解析→论点提炼→叙事骨架→大纲版式→样稿确认→逐页设计→质检交付。
  内置能力自适应教练机制，无论用户专业水平高低，均引导至及格以上输出。
  品牌规范自动检测：有orchisky.md则品牌模式，无则降级通用商务模式。
compatibility: >-
  品牌规范文件（可选）：/mnt/skills/user/orchisky-design/references/orchisky.md
  Phase模块：/mnt/skills/user/orchisky-ppt/references/phase-01.md 至 phase-08.md
  教练机制：/mnt/skills/user/orchisky-ppt/references/coach-engine.md
  版式库：/mnt/skills/user/orchisky-ppt/references/layout-library.md
  工具链：/mnt/skills/user/orchisky-ppt/assets/（含svg_to_pptx工具链）
---

# Orchisky PPT V5.0 · 主调度文件

> 本文件是调度层，负责按顺序启动各Phase模块、执行入场条件检查、管理完成卡放行。
> 每个Phase是独立的可插拔模块，定义在对应的 references/phase-0X.md 中。
> 升级单个Phase不影响其他Phase。

---

## 文件架构

```
SKILL.md                              ← 本文件（调度层）
references/
├── phase-01.md                       ← Phase 1：规范与受众定义
├── phase-02.md                       ← Phase 2：材料解析与信息结构化
├── phase-03.md                       ← Phase 3：核心论点提炼
├── phase-04.md                       ← Phase 4：叙事骨架构建
├── phase-05.md                       ← Phase 5：大纲内容与版式规划
├── phase-06.md                       ← Phase 6：视觉样稿确认
├── phase-07.md                       ← Phase 7：逐页SVG设计
├── phase-08.md                       ← Phase 8：质检与交付
├── coach-engine.md                   ← 教练机制（跨Phase复用）
├── grid-system.md                    ← 画布坐标体系（坐标唯一来源）
├── svg-skeleton-common.md            ← 通用SVG骨架（Chrome/卡片/箭头）
├── svg-skeleton-[i/s/e/v/t/a/g].md  ← 各系版式骨架（按系按需读取）
├── layout-impl-common.md             ← 版式选择参考表+通用规范
├── layout-impl-[i/s/e/v/t/a].md     ← 各系版式实现细节（按系按需读取）
├── layout-library.md                 ← 版式库定义（Phase 5选版式）
├── designer-rules.md                 ← SVG设计规范+品牌纪律+PPTX约束
├── chart-impl.md                     ← 图表实现规范（有图表时读取）
├── pptx-native-rules.md              ← SVG转PPTX工具链规范和排查指南
└── quality-audit-protocol.md        ← 三级Gate质量审计规程
assets/
├── svg_to_pptx_wrapper.py            ← 工具链入口（唯一调用方式）
└── svg_to_pptx/                      ← 底层转换算法库
```

**关键规范文件快速索引：**
- 坐标 → `grid-system.md`
- SVG骨架代码 → `svg-skeleton-[系].md`（按版式ID选对应系文件）
- 通用骨架（Chrome/卡片） → `svg-skeleton-common.md`
- 版式实现细节 → `layout-impl-[系].md`
- PPTX兼容约束+品牌纪律 → `designer-rules.md`
- 工具链使用和排查 → `pptx-native-rules.md`
- 质量审计三级Gate → `quality-audit-protocol.md`

---

## 触发后立即执行

输出欢迎卡，然后立即读取并执行 `references/phase-01.md`：

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Orchisky PPT V5.0 · 已启动
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
我会带你完成8个阶段，把你的材料和想法
转化为一份能驱动受众决策的专业演示文稿。

每个阶段开始时我会告诉你：
  要做什么 / 用什么方法 / 你需要做的

每个阶段结束时你需要确认输出，
才会进入下一阶段。

现在进入第一步 →
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 全局调度规则

### 规则 1：严格串行，不可跳步

Phase 必须按 1→2→3→4→5→6→7→8 顺序执行。

**用户要求跳过某个Phase时：**
不得直接跳过。先读取对应Phase文件的"跳过风险"说明，向用户明确告知风险，
让用户二次确认：「了解风险后，你确认要跳过 Phase X 吗？」
用户明确确认后，记录跳过原因，继续执行下一Phase。
跳过记录写入工作区，Phase 8 质检时会再次提示。

### 规则 2：入场条件检查

每个Phase开始前检查前置条件（见各Phase文件的"入场条件"部分）。
不满足时拒绝进入并说明原因，引导用户完成前置步骤。

### 规则 3：阶段提示卡（强制）

每个Phase开始时，必须先输出该Phase的提示卡，再执行内容。
提示卡统一使用 `┌──` 方框样式，包含以下四项：
- 这一步要做什么
- 用什么方法（首次出现的专业术语在括号内附中文说明）
- 你需要做的
- 注意事项（有重要风险时才显示）

### 规则 4：教练机制检查（每Phase入口执行）

每个Phase开始时，读取 `references/coach-engine.md` 的入口检查规则：
- 检测当前Phase是否需要激活教练模式
- 根据当前能力档位调整交互方式
- 档位可随时降级（发现用户在当前Phase表现不如预期时自动降级）

### 规则 5：完成卡放行（强制）

每个Phase执行完毕后输出完成卡。
AI 根据用户回应的语义判断是否放行，无需固定触发词。
用户未明确确认时，不得自动进入下一Phase。

**完成卡统一格式：**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Phase [X] · [阶段名称] 完成
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
入场条件    [前置Phase确认情况]
本阶段输出  [核心产出物]
关键结论    [最重要的1-2条结论]
待确认      [需要用户判断的事项]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
以上内容确认无误后进入 Phase [X+1]。
如需修改请直接说明。
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 八阶段执行索引

| Phase | 名称 | 核心产出 | 关键确认点 |
|-------|------|---------|----------|
| 1 | 规范与受众定义 | BRAND_RULES + 受众卡 + 能力档位 | 受众画像和汇报目标是否准确 |
| 2 | 材料解析与信息结构化 | 信息清单（四类标注） | 信息空缺的处理方式 |
| 3 ★ | 核心论点提炼 | 灵魂句（≤30字） | 灵魂句是否准确反映你的判断 |
| 4 | 叙事骨架构建 | Ghost Deck标题序列 | 标题序列逻辑是否自洽 |
| 5 | 大纲内容与版式规划 | 逐页布局规划卡 | 版式和内容要点是否符合预期 |
| 6 | 视觉样稿确认 | 3页SVG样稿 | 视觉基调是否满意 |
| 7 | 逐页SVG设计 | 全部SVG文件 | 每3页确认 + 整体预览 |
| 8 | 质检与交付 | 交付物包 + QC报告 | 最终质检结果确认 |

每个Phase的完整执行规则见对应的 `references/phase-0X.md` 文件。

---

## 品牌规范自动同步

品牌规范的唯一来源是 `/mnt/skills/user/orchisky-design/references/orchisky.md`。
修改规范文件后，下次运行技能自动生效，无需修改本技能任何文件。

本文件及所有Phase文件中禁止出现具体色值，只能引用规范条款编号。
技能是规范的执行者，不是共同作者。

---

## 工具链概要

### SVG → PPTX 转换

唯一调用方式（通过wrapper，不直接调底层）：
```python
from svg_to_pptx_wrapper import svg_to_native_pptx
success = svg_to_native_pptx(svg_files=svg_files, output_path=output, canvas_format='ppt169')
```

**中文字体处理：**
- 工具链内置字体映射表，`Songti SC` 自动映射 `SimSun`（Windows），`PingFang SC` 自动映射 `Microsoft YaHei`
- SVG中字体声明必须包含fallback链：`"Songti SC,SimSun,serif"` 或 `"Microsoft YaHei,sans-serif"`
- 详见 `pptx-native-rules.md` §字体显示异常

**批量生成错误处理：**
- 单页解析失败 → 该页输出空白页，不中断整批转换，控制台打印 `Error: Failed to parse SVG [filename]`
- XML特殊字符（`&`）自动修复，`<`、`>`、`"` 需手动转义
- 转换后检查：`verbose=True` 输出每页转换状态，ERROR数量 > 0 时建议回到 Phase 7 修复后重转
- 完整排查指南见 `pptx-native-rules.md` §常见问题排查

**质量审计三级Gate（自动在转换前执行）：**
- Gate 1：空内容检测 → WARNING
- Gate 2：单行字数超限 → WARNING
- Gate 3：XML合法性修复 + rgb()颜色警告 → 自动修复/WARNING
- 详见 `quality-audit-protocol.md`
