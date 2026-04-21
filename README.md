# Orchisky 技能合集

> **兰之天 Orchisky · AI 技能库** · V2.0 · 2026-04
>
> 覆盖品牌规范执行、Demo 原型设计（品牌版 / 平台版 / 现场工业端）、PPT 制作四大场景。
> 所有技能共享统一品牌主色 `#1070F0`，依据《品牌与设计规范 V2.0》。

---

## 技能目录

| 技能 | 用途 | 主色 | 典型触发词 |
|------|------|------|-----------|
| [orchisky-design](./orchisky-design/) | 品牌视觉规范强制执行器 · 含完整 V2.0 规范文档 | `#1070F0` | "按兰之天规范" / "Orchisky风格" |
| [orchisky-demo-design](./orchisky-demo-design/) | 品牌独立 Demo 原型（官网/营销/方案展示） | `#1070F0` | "做个Demo" / "品牌版原型" |
| [orchisky-demo-design-platform](./orchisky-demo-design-platform/) | Orchisky 平台 PC 后台管理原型（Ant Design 5） | `#1677FF` | "列表页" / "详情页" / "平台Demo" |
| [orchisky-demo-design-mobile](./orchisky-demo-design-mobile/) | 工厂一线现场端原型（PDA 手持 / 工业 Pad） | `#1070F0` | "PDA原型" / "Pad点检" / "扫码界面" |
| [orchisky-ppt](./orchisky-ppt/) | 全流程 PPT 制作 · 对标麦肯锡/德勤标准（.pptx 输出） | `#1070F0` | "做PPT" / "做演示文稿" |
| [ppt-svg](./orchisky-ppt/) | 全流程 PPT 制作（SVG/HTML 输出路径） | `#1070F0` | "做PPT" / "SVG幻灯片" |

---

## 目录结构

```
orchisky/
├── README.md                          ← 本文件
│
├── orchisky-design/                   ← 品牌规范强制执行器
│   ├── SKILL.md
│   ├── CONFLICTS_AND_UNIFIED_RULES.md ← 四轨道分流判断树
│   ├── ICONOGRAPHY.md
│   ├── colors_and_type.css            ← CSS 变量完整定义（可直接复制）
│   ├── references/
│   │   ├── orchisky.md                ← ★ 品牌与设计规范 V2.0（唯一真源）
│   │   ├── Orchisky-Field-Design-System-V1.0.md
│   │   ├── 原型设计规范-Orchisky平台版-V1.0.md
│   │   └── 原型设计规范-V1.0.md
│   ├── preview/                       ← 18 个组件可视化预览 HTML
│   └── ui_kits/
│       ├── brand/                     ← 品牌官网组件（React JSX）
│       ├── field-pda/                 ← PDA 现场端组件（React JSX）
│       └── platform/                 ← PC 后台管理组件（React JSX）
│
├── orchisky-demo-design/
│   ├── SKILL.md
│   └── references/
│       ├── design-spec.md
│       └── prompt-templates.md
│
├── orchisky-demo-design-platform/
│   ├── SKILL.md
│   └── references/
│       ├── design-spec.md
│       └── prompt-templates.md
│
├── orchisky-demo-design-mobile/
│   ├── SKILL.md
│   └── references/
│       ├── design-tokens.md           ← 全量 Design Token
│       ├── components.md              ← 16 个核心组件 HTML 片段
│       ├── page-patterns.md           ← 12 个高频页面模式
│       ├── templates/
│       │   ├── pda-portrait.html      ← PDA 空白骨架
│       │   └── pad-landscape.html    ← Pad 空白骨架
│       └── golden-samples/
│           ├── pda-wms-rksqd.html    ← PDA 入库扫码采集范本
│           └── pad-eam-djjh.html     ← Pad 点检执行范本
│
└── orchisky-ppt/
    ├── SKILL.md
    ├── LESSONS.md
    ├── assets/                        ← Python 脚本 + 主题文件
    └── references/                    ← 28 个 PPT 制作参考文档
```

---

## 核心规范：四轨道分流

不同场景使用不同规范文档，详见 `orchisky-design/CONFLICTS_AND_UNIFIED_RULES.md`。

| 场景 | 使用规范 | 主色 |
|------|---------|------|
| Word / Excel / PPT 交付物 | `orchisky-design/references/orchisky.md` | `#1070F0` |
| PDA / 工业 Pad HTML 原型 | `Orchisky-Field-Design-System-V1.0.md` | `#1070F0` |
| 独立品牌 Demo HTML | `原型设计规范-V1.0.md` | `#1070F0` |
| Orchisky 平台二开 Demo HTML | `原型设计规范-Orchisky平台版-V1.0.md` | `#1677FF` |

---

## 禁用规则（全场景通用）

- ❌ 渐变 / 3D 效果 / 投影
- ❌ 纯黑 `#000000`（最深用 `#1A1A1A`）
- ❌ 第二个装饰彩色
- ❌ 表格竖线
- ❌ 饼图 / 独立图例
- ❌ Emoji 用于正式内容
- ❌ 仅凭颜色传达状态（必须符号+颜色双通道）

---

*Orchisky 江苏兰之天软件技术有限公司 · AI 技能库 · V2.0 · 2026-04*
