---
name: orchisky-demo-design-platform
description: >
  Orchisky demo Design 平台版技能。专门生成基于 Orchisky 平台（Ant Design 5 定制）的 PC 后台管理系统原型 Demo，仅覆盖 PC 宽屏（1440px）场景；移动端 / 大屏场景请用 orchisky-demo-design 技能。
  当用户说「做列表页」「做详情页」「做新增页」「做采购入库单」「做物料管理页面」「做 WMS/ERP 后台页面」「生成平台 Demo」「做带筛选和表格的页面」「做单据页面」「主表+子表」「做 LIST 页面」「做 DETAIL 页面」「做 CREATE 页面」「带抽屉 Drawer」「Modal 新增」「做一个管理后台」「做后台表单」时，立即触发此技能。即使用户只说「做个后台管理页面」或「给客户看的 PC Demo」也应触发。输出严格遵循 Orchisky 平台视觉约束（Ant Design 5 Token），生成完整可交付的单文件 HTML 原型。
---

# Orchisky Demo Design — 平台版

## 适用范围

**仅覆盖 PC 后台管理系统（1440px 宽屏）**。移动端 / 大屏场景请使用 `orchisky-demo-design` 技能。

三种核心页面类型 + 常见组合：

| 类型 | 场景举例 |
|------|---------|
| **LIST** | 物料列表、采购入库单列表、出库单列表、库存查询、供应商管理 |
| **DETAIL** | 物料详情、单据详情、客户档案详情、工单详情 |
| **CREATE** | 新增物料、新增采购入库单、新增其他出库单、编辑客户档案 |
| **LIST + Drawer** | 列表页 + 右侧 720px 抽屉详情 |
| **LIST + Modal** | 列表页 + 弹窗新增 |
| **主表 + 子表** | 有明细的单据（采购单 / 销售单 / 生产工单 / 出库单） |

---

## 执行流程（每次严格按此顺序）

### Step 1：读取规范（强制）

生成任何原型前，**必须先读取**以下两个文件：

```
references/design-spec.md       ← 完整视觉规范（10条铁律 / 组件规格 / Token / 禁用规则）
references/prompt-templates.md  ← LIST / DETAIL / CREATE 完整 Prompt 骨架 + 假数据字典
```

### Step 2：识别页面类型

| 用户提到 | 对应模板 |
|---------|---------|
| 列表、查询、单据列表、物料清单、库存查询、供应商列表 | LIST 列表页 |
| 详情、档案、单据详情、查看记录 | DETAIL 详情页 |
| 新增、编辑、填写、创建单据 | CREATE 新增/编辑页 |
| 列表 + 点查看、带抽屉、Drawer | LIST + Drawer 组合 |
| 列表 + 弹窗新增、Modal | LIST + Modal 组合 |
| 有明细的单据、主表子表 | 主表 + 子表场景 |

**若场景模糊，只问一个问题**：「是列表页、详情页还是新增页？」不问第二个。

### Step 3：生成 HTML

按 `references/prompt-templates.md` 中对应模板的骨架结构生成，严格遵循所有视觉约束。

**输出格式要求**：
- 单文件 HTML + 内联 CSS（CSS 变量实现 Ant token）
- **不引入**外部 React / Ant Design 库（便于 Demo 快速预览）
- 可引用 Google Fonts（Noto Sans SC / JetBrains Mono）
- 保存到 `/mnt/user-data/outputs/orchisky-platform-[页面名].html`
- 调用 `present_files` 呈现给用户
- 简要说明：「已按 Orchisky 平台规范生成 [场景] 原型，可点区域包括：[列出]」

---

## 10 条视觉铁律速查（违反任意一条 = 不合格）

| # | 铁律 | 关键值 |
|---|------|--------|
| 01 | 基于 Ant Design 5 | 所有 token、组件、圆角、间距继承 Ant 5 默认值 |
| 02 | 主色 | `#1677FF`，禁改 |
| 03 | 顶栏 | 高 48px，深色 `#001529`，白字，激活 Tab 白底蓝字 |
| 04 | 侧栏 | 白底（非彩色），宽 200–240px，激活项 `#E6F4FF` 药丸 + 蓝字 + 500 字重 |
| 05 | 圆角 | 默认 6px，Tag 4px，Modal 8px |
| 06 | 按钮 | 高 32px，主蓝实填，次按钮白底灰边，危险按钮红填或红描边 |
| 07 | 表格 | 表头 `#FAFAFA`，主键列 `#1677FF` 等宽链接，行高 44px，hover `#F5F5F5` |
| 08 | 状态标签 | 实色填充小药丸（已审核=蓝填 · 已同步=绿填 · 已驳回=红填 · 冻结=灰填）；分类 Tag 才用淡底描边 |
| 09 | 字体 | 中文 `Noto Sans SC / PingFang SC`；数字/编码 `JetBrains Mono` |
| 10 | 禁止 | 卡片阴影 / 彩色表头 / 侧栏彩色 / 渐变按钮 / emoji / 3D 图标 / 圆角 12px+ |

---

## 微调纠错速查（AI 有偏差时用）

| 症状 | 纠正指令 |
|------|---------|
| 主色偏紫/偏深 | 「主色精确使用 #1677FF，不要自创」 |
| 侧栏变成深色渐变 | 「侧栏必须白底，激活项用 #E6F4FF 浅蓝背景 + #1677FF 字」 |
| 按钮太圆（胶囊状） | 「按钮圆角严格 6px，控件高度 32px」 |
| 标签变成圆点+淡底 | 「状态标签使用 Ant Tag 实色填充样式（已审核=蓝填 已同步=绿填）」 |
| 表单标签在输入框上方 | 「表单标签必须右对齐在输入框左侧，加凒号；必填红 * 在标签前」 |
| 段标题加了左竖线 | 「段标题仅加粗 600 15px，不加任何装饰图标或色条」 |
| 表头变彩色 | 「表头背景必须 #FAFAFA，字重 600 深色」 |
| 卡片浮起来带阴影 | 「白卡用 1px #F0F0F0 描边，绝不加阴影」 |
| 数字列左对齐 | 「数字列右对齐，等宽字体，加千分位」 |
| 出现 emoji 或 3D 图标 | 「图标使用 @ant-design/icons 线性描边 1.5px」 |

---

## 参考资源

完整骨架结构、字段清单、Prompt 模板、假数据字典详见：

- `references/design-spec.md` — 原型设计规范全文（Orchisky 平台版 V1.0，含10条铁律 / 全部组件规格 / 禁用规则 / 检查清单）
- `references/prompt-templates.md` — LIST / DETAIL / CREATE 完整 Prompt 骨架 + 4种组合场景 + 微调速查 + 假数据字典

**生成任何原型时，必须重新读取 references 文件，不依赖记忆。**
