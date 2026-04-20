---
name: orchisky-demo-design-mobile
description: >
  兰之天 Orchisky 现场工业端（PDA / 工业 Pad）原型设计技能。严格遵循《兰之天 Orchisky Design V2.0》品牌规范与《兰之天 · 现场工业端设计规范 Orchisky Field Design System V1.0》双上游规范。当用户说「做个 PDA 原型」「做个 Pad 原型」「PDA 扫码界面」「Pad 点检页面」「工人端界面」「仓管员扫码」「移库拣货」「设备点检」「维修工单」「巡检任务」「一线操作员用的 App」「按兰之天规范做现场端」「Orchisky 移动端现场版」，或者上传了需求文档要求生成 PDA/Pad 界面时，立即触发此技能。覆盖 PDA 竖屏（480×800 / 720×1280）与工业 Pad 横屏（1280×800）两种场景，输出严格遵循 V2.0 品牌蓝 #1070F0 + Field V1.0 触控与户外规范的单文件 HTML 原型。
---

# Orchisky Demo Design Mobile 技能

## 适用场景

本技能专做 **工业一线现场设备** 的原型——不是给老板看的管理后台，不是给消费者用的 C 端 App，而是：

| 人群 | 设备 | 典型场景 |
|------|------|----------|
| 仓管员 · 叉车工 | **PDA 手持终端**（优博讯 / iData / 海康）竖屏 | 入库扫码、上架、拣货、盘点、组托、打印标签 |
| 班组长 · 线长 · 设备员 · 技术员 | **工业 Pad** 10 寸横屏 | 点检计划下发、点检执行、维修申请、维修确认、任务派工 |

> **场景区分铁律**：1440×900 管理后台 → `orchisky-demo-design-platform`；1920×1080 大屏 → `orchisky-demo-design`；手机端消费类 App（C 端）→ `orchisky-demo-design` 的 B.x 模板。**本技能只做现场工业机上运行的 B 端界面**。

---

## 上游规范（双源对齐）

```
 Orchisky Design V2.0（全公司品牌规范）
    │  主色 --blue-500 #1070F0
    │  中性色 --ink-0 ~ --ink-800
    │  语义色 success/warning/danger
    │  字体 Source Han Sans + Roboto Mono
    │  图标 Lucide 线性 24×24 2px
    │  禁用清单（17 条）
    ▼
 Orchisky Field Design System V1.0（现场扩展，本技能直接依据）
    │  PDA/Pad 尺寸与布局
    │  触控 ≥48px、户外 ≥4.5:1 对比
    │  四色 CTA 按钮仅用于底部 CTA 条
    │  Pad 内页严禁 Hero
    ▼
 本技能（生成单文件 HTML 原型）
```

冲突原则：当 V2.0 与现场需求冲突时，以 Field V1.0 为准；但颜色 token 永远继承 V2.0，不得自创。

---

## 执行流程（严格顺序）

### Step 1 · 读取规范

**强制**：生成任何原型前，必须先读取 references 目录下的文件：

```
references/design-tokens.md    ← 令牌（颜色 / 字号 / 圆角 / 间距 / 高度）
references/components.md       ← 组件库（16 个核心组件 HTML 片段）
references/page-patterns.md    ← 页面模式库（12 个高频页面）
```

完整规范文档（深度参考）：
- `/sessions/beautiful-lucid-ramanujan/mnt/outputs/Orchisky-Field-Design-System-V1.0.md`
- `/sessions/beautiful-lucid-ramanujan/mnt/.claude/skills/orchisky-design/references/orchisky.md`（V2.0）

生成前至少完整读一遍 `design-tokens.md` 和 `components.md`，不要凭记忆。

### Step 2 · 识别设备形态与业务场景

判断优先级：**设备形态 > 业务场景 > 页面类型**。

| 信号词 | 判定 | 画布 |
|--------|------|------|
| "PDA"、"手持"、"扫码枪"、"出库扫码"、"入库扫码"、"上架"、"拣货"、"盘点采集" | PDA 竖屏 | 480×800（默认）或 720×1280 |
| "Pad"、"平板"、"班组长"、"线长"、"点检"、"工单"、"维修派工" | Pad 横屏 | 1280×800 |
| 模糊不清 | 智能判断见 Step 3 | — |

### Step 3 · 澄清策略

默认**不问问题**，遇以下任一必须问（一次最多 1 个）：

| 情况 | 问什么 |
|------|--------|
| 没说 PDA 还是 Pad | "PDA 竖屏（扫码采集）还是 Pad 横屏（点检工单）？" |
| 业务名词歧义（例：盘点=PDA 盘点采集？还是 Pad 盘点进度？） | 二选一 |
| 核心字段不清楚 | **不问**，按假数据字典给行业通用字段 + 注释说明 |
| 交互流程不清楚 | **不问**，画当前单屏 + 右下角"后续步骤提示浮层" |

### Step 4 · 生成 HTML

严格按设备对应的骨架、组件规格、数据字典生成单文件 HTML。

**输出要求**：
- 单文件 HTML + 内联 CSS（无外部框架）
- 唯一允许的外部依赖：Google Fonts（Source Han Sans SC + Roboto Mono）+ Lucide Icons CDN
- **禁止** Bootstrap / Ant Design / Tailwind / shadcn 等框架
- **必须包含** `design-tokens.md § 9` 中的完整 `:root` 变量块
- 文件保存到 `/sessions/beautiful-lucid-ramanujan/mnt/outputs/` 目录
- 保存完毕调用 `present_files` 呈现给用户
- 文件名规则：`orchisky-mobile-[设备]-[业务].html`，例：`orchisky-mobile-pda-rksqd.html` / `orchisky-mobile-pad-djjh.html`

---

## 视觉 DNA · 10 条铁律（违反任意一条 = 不合格，必须重做）

这 10 条是「一眼识别是兰之天 Orchisky 现场端」的硬指标。全部来自 V2.0 + Field V1.0 两份上游规范。

| # | 铁律 | 关键值 / 说明 |
|---|---|---|
| 01 | **唯一主色** | `--blue-500 #1070F0`（V2.0 主色）。历史源码 `#3072FC` **废弃** |
| 02 | **冷中性底** | 页面底 `--ink-50 #FAFAFA`，卡片底 `--ink-0 #FFFFFF`。历史 `#F4F1EF` 暖米灰 **废弃** |
| 03 | **四色 CTA 仅限底部** | 主蓝 / 次白 / 危红 / 取消幽灵——只能并排出现在 **底部 CTA 条**；列表内联按钮只允许 secondary/ghost |
| 04 | **圆角三档** | 2 / 4 / 6。严禁 0 / 8 / 12 / 胶囊（999） |
| 05 | **表头浅墨灰** | `--ink-100 #F5F5F5` + `--ink-600` 字。**禁止** 表头填蓝色 |
| 06 | **选中态浅蓝** | `--blue-50 #EAF2FE` 底 + `--blue-500` 左边条 4px。历史浅绿 **废弃** |
| 07 | **必填红星** | `--danger-600 #B01C1C` 星号，label 后置 2px |
| 08 | **Sans-Only + Mono** | 中文/UI 用 Source Han Sans，数字/SN/条码/量值用 Roboto Mono。**不引入** Serif |
| 09 | **双通道状态** | 状态 Chip 必须同时用颜色 + 文字表达，色弱可读 |
| 10 | **Pad 内页严禁 Hero** | AppBar 56px 即可；首页 Hero ≤110px，且只能用 `--blue-50` 浅底 |

---

## 页面结构骨架

```
PDA（480×800）：      StatusBar 24 + Topbar 56 + 内容 + 底 CTA 48
Pad 内页（1280×800）：AppBar 56 + 内容(≥87%) + 可选底 CTA 48
Pad 首页：            AppBar 56 + Hero ≤110 + 内容 + 可选底 CTA 48
```

**Hero 使用规则**（硬约束）：

| 场景 | Hero 是否允许 | 高度上限 | 背景色 |
|---|---|---|---|
| PDA 任意页 | ❌ 严禁 | — | — |
| Pad 首页 | ✅ 可选 | 110px | `--blue-50` 浅蓝 |
| Pad 登录 | ✅ 可选 | 160px | `--blue-50` 浅蓝 |
| Pad 内页（列表/详情/表单/看板/抽屉） | ❌ **严禁** | — | — |

---

## AI-slop 禁用清单（每次生成完自查，出现任意一条 = 重做）

| # | 禁用特征 | 替代方案 |
|---|---|---|
| 01 | 紫/粉/彩虹/多色渐变 | 单 `--blue-500` 平铺 |
| 02 | Glassmorphism / `backdrop-filter: blur` | 不透明白底 + 1px 边 |
| 03 | 卡片阴影（任何强度） | 0 阴影 + 1px `--ink-200` 边；仅 Drawer 允许 `--shadow-overlay` |
| 04 | Emoji 🚀🔥✨ / 3D 拟物图标 / 吉祥物 | Lucide 线性 24px 2px 单色 |
| 05 | 圆角 > 6px 或胶囊 | 2 / 4 / 6 三档 |
| 06 | 斑马条纹表格 | 白底 + 1px 分割 + 选中浅蓝 |
| 07 | 按钮 < 44px / 胶囊形 | 主 ≥48px 次 ≥38px 矩形 |
| 08 | 纯字按钮（看不出可点） | 描边或填充，与背景有 3:1 对比 |
| 09 | PDA 字号 < 12，Pad 字号 < 14 | 按 `--fs-*` 变量 |
| 10 | 假数据 test / 张三 / ABC / $999 / Lorem | 按假数据字典 |
| 11 | 过度动画（数字跳动 / 粒子 / >200ms 延迟） | 最多 150ms ease |
| 12 | **Pad 蓝色 Hero 大通栏** | AppBar 56 即可，Hero 仅首页且 ≤110 用浅蓝 |
| 13 | **废弃色**出现 | #3072FC → `--blue-500`；#F4F1EF → `--ink-50`；#DDF7FD → `--blue-50`；#D7F3D2/#68D279 → `--success-*`；#F14E4F → `--danger-600`；#ABCCFF → `--blue-200` |
| 14 | Serif 字体（Source Han Serif） | 仅 Sans |
| 15 | 饼图 / 3D 图表 / 渐变柱 | 横柱 / 折线，单蓝色阶 |
| 16 | 中英文混排无空格 | 中英文数字之间用半角空格 |

---

## 假数据字典（制造业 / 仓储场景专用）

| 字段 | 示例 | 禁止 |
|------|------|------|
| 公司 | 兰之天精密（苏州）· 华瑞机电 · 东方重工 | 阿里/华为/某某科技 |
| 车间 | 电机装配一车间 · 绕线车间 · SMT 车间 | 车间A/车间1 |
| 产线 | 装配-A 线 · 绕线-02 · SMT-03 | 产线1 |
| 设备编码 | CNC-02-05 · 绕线机-A02 · 贴片机 SMT-01 | machine1 |
| 工单号 | RK-20260420-0038 · DJ-20260420-012 · WX-20260419-007 | 12345 |
| 物料编码 | M-BRG-A2024-02 · R-1024-05-B · 电机-50W-A 型 | ABC-001 |
| 批号 | LOT-20260418-01 | 批1 |
| 人名 | 王建国 · 李文静 · 赵伟明 · 陈志强 | 张三/李四/test |
| 工号 | ORC-2019-0847 | 001 |
| 数量 | 1,280 件 / 520 台 / 8,400 pcs | 99999 |
| 仓位 | A-02-03-05（库区-货架-层-位） | 位置1 |
| 日期 | 2026-04-20 08:32:15 · 04-20 08:32 | 混格式 |
| 点检项 | 主轴温度 / 皮带张紧度 / 润滑油位 / 急停按钮功能 | 检查1 |
| 点检值 | 62°C / 合格 / 0.35MPa / 正常 | OK |
| 状态 | 待执行 · 执行中 · 已完成 · 异常 · 待确认 | status1 |
| 故障类别 | 机械故障 · 电气故障 · 气路故障 · 软件异常 | 故障1 |

---

## 关键组件速查（完整版见 `components.md`）

**按钮系**（`--h-btn: 48px`）
- Primary：`--blue-500` 底 + `--ink-0` 字
- Secondary：`--ink-0` 底 + `--ink-300` 边 + `--ink-700` 字
- Danger：`--ink-0` 底 + `--danger-600` 边字
- Ghost：透明 + `--ink-600` 字（取消）
- 四色同屏：**仅底部 CTA 条**，列表行内联只用 Secondary / Ghost

**输入框** `--h-field: 40px`
- 白底 + `--ink-300` 1px 边 + `--radius-md`
- 必填 label 后 `--danger-600` 红星
- 焦点：`--blue-500` 边 + `--focus-ring`

**表格**
- 表头 `--ink-100` 底 + `--ink-600` 字 + 400 字重
- 行高 `--h-row: 44px`，**无竖线**
- 数字列右对齐 mono

**Chip**（双通道）
- `chip-success/warning/danger/info/neutral`
- 浅底 50 + 深字 600 + 文字语义

**Pad AppBar**（`--h-appbar: 56px`）
- 左：品牌 + 面包屑
- 右：用户信息 + 退出
- **严禁**延伸成 Hero

---

## Golden Samples（范本）

生成复杂原型前，**强烈推荐** 先读一遍对应设备形态的范本：

```
references/golden-samples/pda-wms-rksqd.html   ← PDA 入库申请单扫码采集
references/golden-samples/pad-eam-djjh.html    ← Pad 点检计划 + 点检执行
```

这两份是 V2.0 + Field V1.0 对齐版本，按钮位置、颜色、间距、Hero 控制全对齐。

---

## 输出流程 Checklist

生成完之后按以下 8 条自查，全部过了才交付：

- [ ] `:root` 包含完整 V2.0 + Field V1.0 变量块（blue-*、ink-*、success/warning/danger-*、ff-*、fs-*、sp-*、radius-*、h-*）
- [ ] 不出现废弃色：#3072FC / #F4F1EF / #DDF7FD / #D7F3D2 / #68D279 / #F14E4F / #ABCCFF
- [ ] **Pad 内页不出现 Hero**；Pad 首页 Hero ≤110px 且用 `--blue-50`
- [ ] PDA 字号 ≥12，Pad 字号 ≥14，无 13 / 15 / 17 / 19 非规范值
- [ ] 圆角只用 2 / 4 / 6
- [ ] 按钮主操作 ≥48px，次 ≥38px，无胶囊
- [ ] 数字全部 Roboto Mono；中文 Source Han Sans；无 Serif
- [ ] 假数据符合制造业字典（无 张三 / test / ABC）

全过 → `present_files` 呈现 → 告诉用户："已按《兰之天 Orchisky Design V2.0》+《Orchisky Field Design System V1.0》双规范生成 [业务] 的 [PDA/Pad] 原型，可点区域：[列举]。"

---

## 参考资源

- `references/design-tokens.md` — 颜色/字号/间距/圆角/高度 全量 Design Token
- `references/components.md` — 16 个核心组件 HTML 代码片段
- `references/page-patterns.md` — 12 个高频页面模式
- `references/templates/pda-portrait.html` — PDA 空白骨架
- `references/templates/pad-landscape.html` — Pad 空白骨架
- `references/golden-samples/` — 两个完整范本原型

**规范血缘**：《兰之天 Orchisky Design V2.0》品牌主规范 + 《兰之天 · 现场工业端设计规范（Orchisky Field Design System）V1.0》现场扩展。
