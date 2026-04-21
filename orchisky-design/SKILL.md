---
name: orchisky-design
description: Use this skill to enforce Orchisky brand/design rules before generating any visual deliverable. Read references/orchisky.md then the appropriate sub-spec.
triggers:
  - Orchisky规范
  - 兰之天规范
  - 品牌规范
  - 按公司规范
---

# orchisky-design 技能

## 触发后必须执行

Step 1: 读取 `references/orchisky.md`（公司级主规范 V2.0，必读）

Step 2: 根据输出轨道读取对应补充文档：
- Word/Excel/PPT → 仅需 `references/orchisky.md`
- PDA/Pad HTML → `references/Orchisky-Field-Design-System-V1.0.md`
- 平台版 Demo → `references/原型设计规范-Orchisky平台版-V1.0.md`
- 品牌版 Demo → `references/原型设计规范-V1.0.md`

Step 3: 生成内容，所有视觉输出必须 100% 符合规范。

## 核心约束

- 主色：`#1070F0`（平台版除外，该用 `#1677FF`）
- 禁止：渐变、阴影、饮图、独立图例、纯黑 #000、Emoji（正式内容）
- 语义色：必须符号+颜色双通道

完整规范见 `references/orchisky.md`。
