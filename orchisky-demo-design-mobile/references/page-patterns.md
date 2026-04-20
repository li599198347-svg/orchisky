# Page Patterns · 兰之天 现场工业端 V1.0

> **12 个高频页面模式**，PDA / Pad 各占一半。生成原型时，先匹配最接近的模式，再按字段需求调整。
>
> 本文件是 `components.md` 的「装配指南」——告诉你哪几个组件应该按什么顺序、什么比例拼成一个完整页面。

---

## 模式索引

| # | 模式名 | 设备 | 一句话 |
|---|---|---|---|
| P01 | PDA 启动登录 | PDA | 仓号 + 工号 + PIN，纯白底，蓝主按钮 |
| P02 | PDA 主菜单（功能宫格） | PDA | 2 列宫格，最多 8 个一级功能 |
| P03 | PDA 单据列表 | PDA | 顶部筛选 Chip + 列表，下拉刷新 |
| P04 | PDA 扫码采集 | PDA | 顶 56 + 扫码区 + 字段 + 底 CTA |
| P05 | PDA 表单提交 | PDA | 字段流 + 校验 + 底 CTA |
| P06 | PDA 结果反馈 | PDA | 全屏插画 + 主结论 + 下一步 |
| P07 | Pad 工作台首页 | Pad | KPI + 待办 + 快捷入口 |
| P08 | Pad 工单列表 | Pad | 左 Tabbar + 顶 AppBar + 主表 |
| P09 | Pad 工单详情 | Pad | 主信息卡 + Tab 分区 + 底 CTA |
| P10 | Pad 表单页（新增/编辑） | Pad | 双列字段 + 底 CTA |
| P11 | Pad 看板 / 报表 | Pad | KPI 行 + 图表 + 明细表 |
| P12 | Pad Drawer 子任务 | Pad | 右 480 抄屉 + 主表保留可见 |

---

## 通用骨架口诀

> **PDA**：StatusBar 24 + Topbar 56 + 内容区 + 底 CTA 48
> **Pad 内页**：AppBar 56 + 内容区（≥87%）+ 可选底 CTA 48
> **Pad 首页**：AppBar 56 + Hero ≤110 + 内容区 + 可选底 CTA 48

**核心硬约束**：
- **PDA 不允许 Hero**——Topbar 已是品牌出口
- **Pad 内页严禁 Hero**——AppBar 56px 即可承载用户/品牌/面包屑信息
- **Pad 首页 Hero 高度 ≤110px**，且只允许放：用户问候 + 当前班次 + 1~2 个 KPI

---

## P01 · PDA 启动登录

结构： StatusBar 24 + 白底内容区（Logo + 应用名 + 3个字段 + 主按钮）

禁用：渐变背景、蓝色大块铺底、emoji。

---

## P02 · PDA 主菜单（功能宫格）

结构： StatusBar 24 + Topbar 56 + 用户带 + 2列宫格

宫格规则：每格 `(480-3×16)/2` 宽，120px 高，弹框 1px ink-200，无阴影。

---

## P03 · PDA 单据列表

结构： StatusBar 24 + Topbar 56 + 顶部筛选 Chip行(40) + 列表

筛选 Chip：水平滚动，选中态 blue-500 底 + ink-0 字。

---

## P04 · PDA 扫码采集

结构： StatusBar 24 + Topbar 56 + 扫码区 + 字段 + 底 CTA 48

扫码区广度 64% 屏宽，4角 L 标记，背景第色半透明。

---

## P05 · PDA 表单提交

结构： StatusBar 24 + Topbar 56 + 字段流(单列) + 底 CTA 48

校验：必填项红 `*`，错误态 danger-600 边框 + 字段下 12字错误提示。

---

## P06 · PDA 结果反馈

结构： StatusBar 24 + Topbar 56 + 全屏结果（96圆环 + 主结论 + 单号 + 2个按钮）

禁止：产品风格彩色烟花、emoji、撤花插画。

---

## P07 · Pad 工作台首页（**唯一允许 Hero 的 Pad 页面**）

结构： AppBar 56 + 左Tabbar + [Hero ≤110] + KPI行 + 待办列表 + 快捷入口

Hero 限制：`background: var(--blue-50)`，高度≤110px，仅放用户问候+班次+1-2个KPI。

```css
.pad-hero{
  height: 110px; padding: var(--sp-4) var(--sp-5);
  background: var(--blue-50);
  border-bottom: 1px solid var(--ink-200);
}
.hero-greet{ font-size: var(--fs-pad-page); font-weight:500; color:var(--ink-800); }
.hero-meta{ margin-top:var(--sp-2); font-size:var(--fs-pad-small); color:var(--ink-600); }
```

---

## P08 · Pad 工单列表（无 Hero）

结构： AppBar 56 + 左Tabbar + [Filter工具栏] + 表格 + 分页

**关键**：AppBar 下面不要再叠一个大标题区，面包屑已说明位置。

---

## P09 · Pad 工单详情

结构： AppBar 56 + 左Tabbar + 二级Topbar 40 + 主信息卡+KPI + Tab分区内容 + 底CTA 48

二级 Topbar：高 40，左返回，中=单号+chip，右无操作按钮（操作全部下沉底部 CTA）。

---

## P10 · Pad 表单页（新增 / 编辑）

结构： AppBar 56 + 左Tabbar + 二级Topbar 40 + 双列字段 + 明细子表 + 底CTA 48

字段双列：每列 `(主区宽-24×3)/2`，行高 72（label 20 + field 40 + gap 12）。

---

## P11 · Pad 看板 / 报表

结构： AppBar 56 + 左Tabbar + [筛选工具栏] + KPI 4卡 + 图表卡 + 明细表

**严禁饮图**（V2.0 §17）。报表色彩：单蓝色不同色阶；多系列按 blue-700/500/300/100 排列。

---

## P12 · Pad Drawer 子任务

主表保持可见，右侧 480px 抄屉承载子任务。抄屉头 56 + 内容滚动 + 底 CTA 48。
逐层通过 `--scrim` 仅覆盖主区。

---

## 跨模式禁令清单

| ❌ 禁止 | ✅ 替代 |
|---|---|
| Pad 内页用 Hero | AppBar 右侧塞用户/班次信息 |
| 渐变 / 阴影 / 圆胶囊 | 平面 + 1px 边 + 4px 圆角 |
| 多色填充图标 | Lucide 单色描边 |
| emoji 表情代替图标 | SVG 线框 |
| 卡通插画做空状态 | 12-stroke 线框 |
| 列表行 + 卡片 + 阴影三件套 | 选其一：卡片**或**列表 |

完整版禁令见 `Orchisky-Field-Design-System-V1.0.md` §17。
