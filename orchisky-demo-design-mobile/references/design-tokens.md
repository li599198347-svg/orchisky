# Design Tokens · 兰之天 现场工业端 V1.0

> 本文件是**代码级真理**。所有值来自两份上游规范：
> 1. 《兰之天 Orchisky Design V2.0》——品牌色彩 / 字体 / 图标 / 禁用清单（全公司统一）
> 2. 《兰之天 · 现场工业端设计规范（Orchisky Field Design System）V1.0》——现场移动端尺寸 / 触控 / 户外可读性扩展

---

## 1. 色彩 Tokens（严格对齐 V2.0）

### 1.1 蓝色阶（唯一彩色）

| Token | HEX | 使用场景 |
|---|---|---|
| `--blue-50` | `#EAF2FE` | 选中态浅背景 |
| `--blue-100` | `#D0E1FC` | Hover 浅背景 |
| `--blue-200` | `#A8C8F9` | Disabled 主按钮底 |
| `--blue-300` | `#6FA3F5` | Focus Ring |
| `--blue-400` | `#3A85F3` | 图表辅助 |
| `--blue-500` | `#1070F0` | **★ 主色**：主按钮 / 链接 / 选中 / 数据高亮 |
| `--blue-600` | `#0A5AC8` | Hover / Active 主按钮 |
| `--blue-700` | `#074499` | 深色背景顶栏 |
| `--blue-800` | `#052E6E` | 大屏背景 |
| `--blue-900` | `#041D48` | 对比阴影 |

### 1.2 墨色阶（中性色）

| Token | HEX | 使用场景 |
|---|---|---|
| `--ink-0`   | `#FFFFFF` | 卡片底 / 内容区 |
| `--ink-50`  | `#FAFAFA` | 页面底 |
| `--ink-100` | `#F5F5F5` | 表头 / 斑马纹 |
| `--ink-200` | `#E2E2E2` | 分割线 / 边框 |
| `--ink-300` | `#CCCCCC` | Disabled 边框 |
| `--ink-400` | `#BBBBBB` | Placeholder |
| `--ink-500` | `#888888` | 辅助文字 |
| `--ink-600` | `#555555` | 次要正文 |
| `--ink-700` | `#333333` | **★ 正文标准色**（禁止 #000） |
| `--ink-800` | `#1A1A1A` | 强调正文 |

### 1.3 语义色（仅三色）

| Token | HEX | 使用场景 |
|---|---|---|
| `--success-50`  | `#EAF5EF` | 成功底 |
| `--success-600` | `#1A7A42` | 成功文字 |
| `--warning-50`  | `#FEF4E8` | 警告底 |
| `--warning-600` | `#9A5200` | 警告文字 |
| `--danger-50`   | `#FDEDED` | 错误底 |
| `--danger-600`  | `#B01C1C` | 错误文字 / 危险按钮边 |

---

## 2. 字体 Tokens

```
--ff-sans: "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif;
--ff-mono: "Roboto Mono", "JetBrains Mono", "Courier New", monospace;
```

- 数字、SN、条码、量值、金额用 `--ff-mono`
- 字重只允许 **400 / 500 / 700** 三级

---

## 3. 字号 Tokens

### PDA（480×800）

| Token | px | 用途 |
|---|---|---|
| `--fs-pda-micro` | 12 | 单位、角标 |
| `--fs-pda-small` | 12 | 辅助信息 |
| `--fs-pda-body`  | 14 | **标准正文** |
| `--fs-pda-title` | 16 | 模块标题 |
| `--fs-pda-page`  | 18 | 页面标题 |
| `--fs-pda-kpi`   | 24 | KPI 数字 |

### Pad（1280×800）

| Token | px | 用途 |
|---|---|---|
| `--fs-pad-small` | 14 | 辅助信息 |
| `--fs-pad-body`  | 16 | **标准正文** |
| `--fs-pad-title` | 16 | 模块标题 |
| `--fs-pad-page`  | 20 | 页面标题 |
| `--fs-pad-kpi`   | 28 | KPI 数字 |

---

## 4. 间距、圆角、高度 Tokens

```css
/* 间距 */
--sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-5:24px;

/* 圆角（禁止 8/12/16/999） */
--radius-sm:2px; --radius-md:4px; --radius-lg:6px;

/* 高度 */
--h-statusbar:24px; --h-topbar:56px; --h-appbar:56px; --h-tabbar:56px;
--h-bottombar:48px; --h-btn:48px; --h-btn-sm:38px; --h-field:40px; --h-row:44px;
```

---

## 5. 阴影与叠加层

```css
--shadow-overlay: 0 2px 12px rgba(7,68,153,0.12);
--scrim: rgba(4,29,72,0.48);
--focus-ring: 0 0 0 2px var(--blue-300);
--selected-bg: var(--blue-50);
--selected-edge: var(--blue-500);
--disabled-bg: var(--ink-200);
--disabled-fg: var(--ink-400);
```

卡片禁用阴影。渐变背景 / 渐变文字 / 渐变按钮全部禁止。

---

## 6. 完整 `:root` 块

```css
:root{
  --blue-50:#EAF2FE;--blue-100:#D0E1FC;--blue-200:#A8C8F9;--blue-300:#6FA3F5;
  --blue-400:#3A85F3;--blue-500:#1070F0;--blue-600:#0A5AC8;--blue-700:#074499;
  --blue-800:#052E6E;--blue-900:#041D48;
  --ink-0:#FFFFFF;--ink-50:#FAFAFA;--ink-100:#F5F5F5;--ink-200:#E2E2E2;
  --ink-300:#CCCCCC;--ink-400:#BBBBBB;--ink-500:#888888;--ink-600:#555555;
  --ink-700:#333333;--ink-800:#1A1A1A;
  --success-50:#EAF5EF;--success-600:#1A7A42;
  --warning-50:#FEF4E8;--warning-600:#9A5200;
  --danger-50:#FDEDED;--danger-600:#B01C1C;
  --ff-sans:"Source Han Sans SC","PingFang SC","Microsoft YaHei",sans-serif;
  --ff-mono:"Roboto Mono","JetBrains Mono","Courier New",monospace;
  --fs-pda-micro:12px;--fs-pda-small:12px;--fs-pda-body:14px;
  --fs-pda-title:16px;--fs-pda-page:18px;--fs-pda-kpi:24px;
  --fs-pad-small:14px;--fs-pad-body:16px;--fs-pad-title:16px;
  --fs-pad-page:20px;--fs-pad-kpi:28px;
  --sp-1:4px;--sp-2:8px;--sp-3:12px;--sp-4:16px;--sp-5:24px;
  --radius-sm:2px;--radius-md:4px;--radius-lg:6px;
  --h-statusbar:24px;--h-topbar:56px;--h-appbar:56px;--h-tabbar:56px;
  --h-bottombar:48px;--h-btn:48px;--h-btn-sm:38px;--h-field:40px;--h-row:44px;
  --shadow-overlay:0 2px 12px rgba(7,68,153,0.12);
  --scrim:rgba(4,29,72,0.48);
  --focus-ring:0 0 0 2px var(--blue-300);
  --selected-bg:var(--blue-50);
  --selected-edge:var(--blue-500);
  --disabled-bg:var(--ink-200);
  --disabled-fg:var(--ink-400);
}
body{font-family:var(--ff-sans);color:var(--ink-700);background:var(--ink-0);}
.num,.mono{font-family:var(--ff-mono);}
```
