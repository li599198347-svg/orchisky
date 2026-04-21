# 兰之天 · 现场工业端设计规范
**Orchisky Field Design System**

**版本** V1.0 · 2026-04
**文档类型** 公司级设计规范分册
**适用范围** PDA 手持终端、工业 Pad 等现场作业类移动端软件
**资产归属** 江苏兰之天软件技术有限公司（Orchisky）
**与 Orchisky Design V2.0 关系** 平行分册，共享品牌基础层，独立规定现场场景特殊条款

---

本规范是基于 Orchisky Design V2.0 针对**制造业一线现场移动端**单独建立的子规范。

现场工业端面向：人在车间、戴着手套、200 lx 照度下、被设备噪音干扰、需要 3 秒内完成扫码。

**共享层**（直接引用 V2.0）：品牌主色 `#1070F0`、中性色阶、语义色、Lucide 图标库、双通道原则、禁用清单

**独立层**：字号梯度、按钮尺寸（≥48px）、圆角（2/4/6px）、组件集、页面模式

---

## 设备形态

| 人群 | 设备 | 画布 |
|------|------|------|
| 仓管员·叉车工·配料员 | PDA 手持竖屏 | 480×800（默认） |
| 班组长·点检员·维修工 | 工业 Pad 横屏 | 1280×800（默认） |

---

## 核心原则

**① 操作区为王**：操作区 ≥ 85%，Hero 不进内页

**② 触控可靠**：可点元素最小 44×44px，相邻间距 ≥ 8px

**③ 强光可识读**：对比度 ≥ 4.5:1（WCAG AA），正文 ≥ 14px

**④ 三秒原则**：单次任务 ≤ 3步完成

**⑤ 双通道传达**：状态必须颜色 + 符号/文字

---

## 视觉 DNA 八条铁律

1. 唯一彩色 `#1070F0`
2. 白底干净 `#FFFFFF`/`#FAFAFA`，禁暖灰
3. 无渐变
4. 无 emoji，全部 Lucide 线性图标
5. 无装饰圆形/光晕
6. 圆角仅 2/4/6px
7. 数字等宽 Roboto Mono
8. 状态双通道

---

## 色彩体系（继承 V2.0）

主品牌色：`blue-500 #1070F0`（唯一彩色）

中性色：`ink-0 #FFFFFF` → `ink-800 #1A1A1A`（禁用 `#000000`）

语义色：
- 正常/合格：`#1A7A42` / `#EAF5EF`（符号 ●）
- 警告/隐患：`#9A5200` / `#FEF4E8`（符号 ▲）
- 异常/失败：`#B01C1C` / `#FDEDED`（符号 ✕）
- 进行中：`#0A5AC8` / `#EAF2FE`（符号 →）
- 待定：`#888888` / `#F5F5F5`（符号 ○）

**废弃色值**：`#3072FC`、`#F4F1EF`、`#DDF7FD`、`#D7F3D2`、`#68D279`、`#F14E4F`、`#ABCCFF`

---

## 字体体系

| 角色 | 首选 | 备选 |
|------|------|------|
| 全部 UI 文字 | 思源黑体 Source Han Sans SC | Microsoft YaHei / PingFang SC |
| 数字/编号/时间 | Roboto Mono | JetBrains Mono |

> 现场端**不用 Serif**（无段落正文，小屏低DPI识读率低）

### 字号梯度

| 层级 | PDA | Pad | 字重 |
|------|-----|-----|------|
| 超大数字（KPI） | 24px | 28px | Bold |
| 页面标题 | 18px | 20px | Bold |
| 卡片标题 | 16px | 16px | Bold |
| 正文/按钮 | 14px | 16px | Regular |
| 说明/辅助 | 12px | 14px | Regular |

---

## PDA 屏幕分区（480×800）

```
┌─────────────────────────┐
│ StatusBar 24px           │  系统状态栏（blue-500底）
├─────────────────────────┤
│ Topbar 56px              │  顶栏（blue-500底，白字）
├─────────────────────────┤
│                          │
│  Main Area               │  主操作区（≥612px，≥76.5%）
│  (可滚动)                 │
│                          │
├─────────────────────────┤
│ BottomBar 48px / TabBar 56px │
└─────────────────────────┘
```

---

## Pad 屏幕分区（1280×800）

```
┌─────────────────────────────────────────┐
│ AppBar 56px  [返回] 标题  用户/时间 操作 │  ≤7%
├─────────────────────────────────────────┤
│                                          │
│  Main Area (1280×~696)                   │  ≥87%
│  布局：单栏 / 左1:3右 / 上下分区          │
│                                          │
├─────────────────────────────────────────┤
│ BottomBar 48px  [汇总]   [次操作] [主CTA] │  6%
└─────────────────────────────────────────┘
```

**核心规则**：
- ❌ 取消 Hero 横幅（内页严禁）
- ✅ AppBar 统一 56px
- ✅ Hero 仅限首页菜单页，且高度 ≤ 110px

---

## 按钮规范

| 类型 | 高度 | 字号 | 圆角 |
|------|------|------|------|
| 标准主操作 | **48px** | 16px | 4px |
| 次级辅助 | **38px** | 14px | 4px |
| 表内迷你（Pad） | 30px | 12px | 2px |

### 四色语义按钮（仅限底部CTA条）

| 类型 | 背景 | 含义 |
|------|------|------|
| Primary | `blue-500 #1070F0` | 主流程下一步 |
| Success | `#1A7A42` | 终态确认（提交/入库/保存）|
| Warning | `#9A5200` | 需要注意的次操作 |
| Danger | `#B01C1C` | 取消/删除/撤销 |

---

## 状态徽标

高度 24px，内边距 0 8px，字号 12px，圆角 2px

**必须符号+文字双通道**，仅色块不合规。

---

## 表格规范

- 表头：`blue-50` 底 + `blue-600` 字 Bold 14px
- 数据行：14/16px `ink-700`；Roboto Mono 数字
- 行高：≥ 44px
- 选中行：`blue-50` 底 + 左 4px `blue-500` 竖条
- **禁止竖线**

---

## 页面模式索引

### PDA 九大页面模式

P01 登录 / P02 首页TabBar / P03 单据列表 / P04 筛选-表格 / P05 扫码采集 / P06 表单录入 / P07 详情查看 / P08 选择器 / P09 设置

### Pad 八大页面模式

Q01 登录 / Q02 首页九宫格 / Q03 列表-详情主从 / Q04 筛选-列表 / Q05 主从+表单 / Q06 点检执行 / Q07 看板 / Q08 详情多分区

---

## CSS 变量块（完整）

```css
:root {
  --blue-50: #EAF2FE; --blue-100: #D0E1FC; --blue-200: #A8C8F9;
  --blue-300: #6FA3F5; --blue-400: #3A85F3; --blue-500: #1070F0;
  --blue-600: #0A5AC8; --blue-700: #074499; --blue-800: #052E6E; --blue-900: #041D48;
  --ink-0: #FFFFFF; --ink-50: #FAFAFA; --ink-100: #F5F5F5; --ink-200: #E2E2E2;
  --ink-300: #CCCCCC; --ink-400: #BBBBBB; --ink-500: #888888;
  --ink-600: #555555; --ink-700: #333333; --ink-800: #1A1A1A;
  --success-50: #EAF5EF; --success-600: #1A7A42;
  --warning-50: #FEF4E8; --warning-600: #9A5200;
  --danger-50: #FDEDED; --danger-600: #B01C1C;
  --ff-sans: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
  --ff-mono: "Roboto Mono", "JetBrains Mono", "Courier New", monospace;
  --fs-pda-micro: 12px; --fs-pda-small: 12px; --fs-pda-body: 14px;
  --fs-pda-title: 16px; --fs-pda-page: 18px; --fs-pda-kpi: 24px;
  --fs-pad-small: 14px; --fs-pad-body: 16px; --fs-pad-title: 16px;
  --fs-pad-page: 20px; --fs-pad-kpi: 28px;
  --sp-1: 4px; --sp-2: 8px; --sp-3: 12px; --sp-4: 16px; --sp-5: 24px;
  --radius-sm: 2px; --radius-md: 4px; --radius-lg: 6px;
  --h-statusbar: 24px; --h-topbar: 56px; --h-appbar: 56px; --h-tabbar: 56px;
  --h-bottombar: 48px; --h-btn: 48px; --h-btn-sm: 38px; --h-field: 40px; --h-row: 44px;
  --shadow-sheet: 0 2px 8px rgba(0,0,0,.08);
  --shadow-dialog: 0 4px 16px rgba(0,0,0,.12);
  --mask: rgba(0,0,0,.5);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--ff-sans); color: var(--ink-700); background: var(--ink-0); }
.num, .mono { font-family: var(--ff-mono); }
```

---

## 交付前质检清单

**视觉**：唯一彩色 `#1070F0` / 白底无暖色渐变 / 圆角仅2/4/6px / 图标全 Lucide / 状态双通道 / 数字 Roboto Mono

**尺寸**：可点元素 ≥ 44×44px / 按钮 48px / 字段 40px / 正文PDA≥14px/Pad≥16px / 行高≥44px

**布局**：PDA顶栏80px，操作区≥612px / Pad顶栏56px，操作区≥696px / **Pad内页未使用Hero** / 底部CTA 48px

---

*Orchisky 江苏兰之天软件技术有限公司 · 现场工业端设计规范分册 · V1.0 · 2026-04*
