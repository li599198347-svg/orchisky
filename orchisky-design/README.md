# Orchisky Design System

> **🔒 V2.0 — 已锁定基线** · 2026-04 · 主色 `#1070F0` (blue-500)

本仓库是**兰之天 Orchisky 公司级设计系统**的唯一真源。所有 AI 技能、手工交付物、客户项目 Demo、品牌物料均以本仓库文件为最终依据。

---

## 目录结构

```
orchisky-design/
├── README.md                         ← 导航和使用指南
├── SKILL.md                          ← AI 技能条引定义
├── CONFLICTS_AND_UNIFIED_RULES.md   ← 四份文档分流规则与冲突解除
├── ICONOGRAPHY.md                   ← Lucide 图标系统规范
├── colors_and_type.css              ← CSS 变量完整定义
├── references/
│   ├── orchisky.md                   ← ★ 公司级品牌与设计规范 V2.0（唯一真源）
│   ├── Orchisky-Field-Design-System-V1.0.md  ← 现场工业端规范
│   ├── 原型设计规范-Orchisky平台版-V1.0.md  ← Ant5 平台版规范
│   └── 原型设计规范-V1.0.md              ← 品牌版独立 Demo 规范
├── preview/                         ← 规范组件可视化预览 HTML
└── ui_kits/
    ├── brand/                        ← 品牌网站/营销页组件
    ├── field-pda/                    ← PDA 工业现场端组件
    └── platform/                    ← Orchisky 平台 PC 后台组件
```

---

## 哪种场景用哪份文档？

| 我在做… | 优先读这份文件 | 主色 |
|---------|-------------|------|
| Word 报告 / Excel / PPT | `references/orchisky.md` | `#1070F0` |
| PDA 扫码 / Pad 点检 原型 | `references/Orchisky-Field-Design-System-V1.0.md` | `#1070F0` |
| Orchisky 平台二开 Demo | `references/原型设计规范-Orchisky平台版-V1.0.md` | `#1677FF` |
| 独立品牌 Demo | `references/原型设计规范-V1.0.md` | `#1070F0` |

详细分流逻辑见 `CONFLICTS_AND_UNIFIED_RULES.md`。

---

## CSS 变量快速使用

```html
<!-- 将 colors_and_type.css 内容复制到 <style> 或外部 CSS -->
<div style="background: var(--blue-50); color: var(--blue-600);">Callout</div>
<button style="background: var(--blue-500); color: #fff; border-radius: var(--radius-btn);">Primary</button>
```

主要变量：

```css
--blue-500: #1070F0;   /* ★ 主品牌色 */
--ink-800:  #1A1A1A;   /* 标题最深色 */
--ink-0:    #FFFFFF;   /* 白底 */
--ink-50:   #FAFAFA;   /* 页面背景 */
--radius-tag: 2px;     /* Tag/Badge */
--radius-btn: 4px;     /* 按钮/输入框 */
--radius-card: 6px;    /* 卡片/Modal */
```

---

## AI 技能引用规则

每个 AI 技能触发时应按以下顺序读取规范：
1. `references/orchisky.md`（所有场景必读）
2. 对应轨道的补充文档（平台版 / 现场端 / 品牌版）

---

## 版本历史

| 版本 | 日期 | 主要变更 |
|------|------|----------|
| V1.0 | 2026-04 | 建立基线：色板 / 字体 / PPT/Word/Excel 规范 |
| V2.0 | 2026-04 | 主色 → `#1070F0`，9 阶色梯，字体升级，新增 Logo/图标/插画/音调/合同/AI Prompt |

---

*Orchisky 江苏兰之天软件技术有限公司 · Design System Repository · V2.0 · 2026-04*
