# 原力战略三部曲 · Yuanli Strategy Trilogy

> **三部曲内容工程工作仓。**  
> 本仓负责把 `yuanli-strategy-soul` 的正典龙骨，外显为三本书、课程、章节正文、概念地图、样章、HTML 页面与内容工程资产。

---

## 0. 仓库定位

本仓不再作为原力战略三部曲的最高 SSOT。  
最高正典、龙骨、模块、术语、接口、任务治理与递归回写，统一归属：

```text
yuanli-strategy-soul
```

本仓的新定位是：

```text
yuanli-strategy-trilogy
= 三部曲内容工程工作仓
= 书稿与课程孵化仓
= 概念地图与外显表达仓
= 样章与章节生产仓
```

一句话：

```text
soul 负责定法，trilogy 负责写书、做课、外显和孵化内容资产。
```

---

## 1. 主从关系

```text
yuanli-strategy-soul
= 正典根仓 / 龙骨仓 / 基石概念体系 / 任务入口 / 递归回写中心

↓ 裁决 / 分发 / 模板 / 回写

yuanli-strategy-trilogy
= 内容工程工作仓 / 书稿孵化 / 课程孵化 / 概念地图外显

↓ 执行 / 产出 / 样章 / 工具 / 案例

yuanli-strategy-soul
= 回写模块 / 术语 / 接口 / 模板 / 索引
```

所有重要结构变化，必须先进入 `soul` 的 Issue 与模块裁决，再回到本仓执行。

当前吸收工程：

```text
yuanli-strategy-soul Issue #206
[治理] trilogy 原子级拆解并吸收回 soul
```

---

## 2. 三部十二模块

本仓所有书稿、课程、章节、地图、样章，必须服从 `soul` 中的 A1-C4 龙骨：

```text
原力战略三部曲
│
├─ 第一部：原力资产 · 向内 · 人
│   ├─ A1 发现母体
│   ├─ A2 回到母体
│   ├─ A3 获得原力
│   └─ A4 显化原力
│
├─ 第二部：原力创业 · 向外 · 事
│   ├─ B1 原力借势
│   ├─ B2 品类独创
│   ├─ B3 模式升维
│   └─ B4 壁垒锁定
│
└─ 第三部：原力 OS · 向上 · 法
    ├─ C1 一纸文脉
    ├─ C2 一个大脑
    ├─ C3 一张地图
    └─ C4 一条链路
```

旧表达“一条公理、两条腿、三本书、一张图”保留为证明模型与历史表达，不再作为本仓最高目录模型。

---

## 3. 各书当前状态

| 书 | 本仓进度 | 已成稿样章 | 对应 soul 模块 | 完整正典源仓 |
|---|---|---|---|---|
| **① 原力资产**（向内·人） | 骨架 + 1/6 章 | [第一章·觉察](books/01-原力资产/第一章-觉察.md) ✅ | A1-A4 | [strategy-playbook](https://github.com/moonstachain/yuanli-strategy-playbook) |
| **② 原力创业**（向外·事） | 骨架 · 0 章 | — | B1-B4 | [startup-map-site](https://github.com/moonstachain/yuanli-startup-map-site)、[startup-map-book](https://github.com/moonstachain/yuanli-startup-map-book) |
| **③ 原力 OS**（向上·法） | 骨架 + 教学样章 | [最小闭环](books/03-原力OS/最小闭环.md) ✅ | C1-C4 | [os-greenbook](https://github.com/moonstachain/yuanli-os-greenbook) |

---

## 4. 仓里有什么

```text
trilogy/
├── 原力三部曲-概念地图.html          概念地图外显
├── 原力三部曲-文脉骨架座舱.html       体系关系图
├── 原力三部曲-文脉总纲.md             历史文脉总纲 / 参考
├── 原力战略三部曲-重构骨架设计稿.md    结构重构稿 / 已回写 soul 部分
├── 原力三部曲-基石与关键概念-全谱.md    字典层全谱 / 已回写 soul 术语词典
├── 原力资产-基石与关键概念-全谱.md      资产分册全谱 / 已回写 A 轴术语与模板
├── 原力OS-信雅达双轨改名表.md           OS 术语与四件套 / 已回写 C 轴术语与模板
├── _atlas/atlas-v2-*.json              知识地图数据层
└── build_atlas.py                      渲染层：读 _atlas/*.json → 生成知识地图.html

books/
├── 01-原力资产/
├── 02-原力创业/
└── 03-原力OS/

review/
└── 写作复盘看板
```

判断 / 渲染分离：

```text
内容数据在 _atlas/*.json
样式与页面生成在 build_*.py
HTML 是构建产物
```

---

## 5. 与 soul 的回写关系

本仓中以下内容已被吸收或正在吸收回 `soul`：

```text
知识总纲 → source/indexes/trilogy-source-index.md
A1-C4 模块 → modules/A-B-C/*
术语全谱 → glossary/*
去重三缝 → interfaces/去重三缝.md
资产样章动作 → templates/asset/算力活-原力活清算卡.md
OS 最小闭环动作 → templates/os/闭环检查卡.md、templates/os/收口句模板.md
模块映射 → source/indexes/module-to-file-map.md
```

后续所有新增样章、课程节、工具卡、概念地图节点，完成后都必须回写 `soul` 的：

```text
modules/
glossary/
interfaces/
templates/
source/indexes/
source/extracts/
project/backwrite-log.md
```

---

## 6. 本仓写作与内容工程规则

任何新章节 / 新课程节 / 新样章，必须先回答：

```text
1. 它归属 A1-C4 哪个模块？
2. 它服务哪条共享脊骨？
3. 它是否触碰去重三缝？
4. 它的输入材料是什么？
5. 它的输出资产是什么？
6. 它回写到 soul 的哪里？
```

推荐使用 `soul` 模板：

```text
yuanli-strategy-soul/templates/chapter-template.md
```

---

## 7. 本地构建（零依赖）

**环境**：Python ≥ 3.8，纯标准库（`json` / `html` / `pathlib` / `glob`），**无第三方依赖，无需 `pip install`**。

| 脚本 | 产出 |
|---|---|
| `trilogy/build_atlas.py` | `trilogy/原力三部曲-概念地图.html` |
| `trilogy/build_master_outline.py` | `trilogy/原力战略三部曲-总纲.html` |
| `trilogy/build_outline.py` | `trilogy/原力三部曲-提纲架构.html` |
| `trilogy/build_zichan_outline.py` | `trilogy/原力资产-四级目录.html` |
| `trilogy/build_book_outline.py <outline>.json` | 创业 / OS 四级目录 |
| `review/build_review.py` | `review/index.html` |
| `build_portal.py` | `index.html` |
| `apply_nav.py` | 给各页注入统一 sticky 导航 |

全量重建：

```bash
cd trilogy
python3 build_atlas.py && python3 build_master_outline.py && python3 build_outline.py
python3 build_zichan_outline.py
python3 build_book_outline.py chuangye-outline.json && python3 build_book_outline.py os-outline.json
cd .. && python3 review/build_review.py && python3 build_portal.py && python3 apply_nav.py
```

---

## 8. 正典与出处

各书既有正典正文仍保留在源仓：

- **原力战略·白皮书 + 绿皮书六册** → [moonstachain/yuanli-strategy-playbook](https://github.com/moonstachain/yuanli-strategy-playbook)
- **原力创业·通关地图六卷 + 交互网站** → [moonstachain/yuanli-startup-map-site](https://github.com/moonstachain/yuanli-startup-map-site)
- **借势合力·通关地图绿皮书 v1.0** → [moonstachain/yuanli-startup-map-book](https://github.com/moonstachain/yuanli-startup-map-book)
- **原力OS·绿皮书** → [moonstachain/yuanli-os-greenbook](https://github.com/moonstachain/yuanli-os-greenbook)

白皮书是**公理 umbrella**；`soul` 是当前统一的正典根仓；本仓是三部曲内容工程外显仓。

---

## 9. 怎么用本仓写书

知识地图与样章是内容工程素材，写作时遵循：

```text
soul 龙骨裁决
→ 选择 A1-C4 模块
→ 使用 chapter-template
→ 写章节 / 课程 / 脚本
→ 沉淀工具卡 / 术语 / 案例
→ 回写 soul
```

每章都要输出至少一种可复用资产：

```text
概念原子
工具卡
案例
术语
模板
SOP / 链路
回写记录
```

---

## 10. 当前状态

- `v0.4`：本仓正式转型为三部曲内容工程工作仓。
- 已有：概念地图、总纲、四级提纲、三本书骨架、样章、构建脚本、复盘看板。
- 已回写：A1-C4 模块、术语、接口、模板、源文件映射到 `yuanli-strategy-soul`。
- 下一步：按 `soul/templates/chapter-template.md` 继续孵化章节正文与课程内容，并持续回写。

视觉：qishi 翡翠墨绿 × 鎏金（`#0d2018 × #c9a961`）。
