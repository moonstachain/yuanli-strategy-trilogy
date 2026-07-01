# 原力战略三部曲 · Yuanli Strategy Trilogy

> 一条公理，两条腿，三本书，一张图。
> **资产**（找到你）→ **创业**（变现金流）→ **OS**（装涡轮）→ 飞轮回流。

原力战略三部曲的**知识结构中枢**：用一张「知识地图」（究极完备 MECE × 内生逻辑链）把整个体系拆成 总概念 → 基石概念 → 支撑关键词。本仓是三部曲**概念结构与逻辑链的单一真源（SSOT）**——三本书都顺着这张图来写；但三本书的**既有正典正文不在这里**（见下方「正典与出处」的源仓），本仓按通关链孵化**精炼重写版**，逐章成稿。

> **一句话摆正预期**——本仓是「地图 + 骨架 + 正在孵化的样章」，不是「三本书的完整正文仓」：
> - ✅ **这里有**：概念地图、总纲、四级提纲、三本书骨架、叙事纪律、写作复盘系统，外加**已成稿的样章**（资产《第一章·觉察》、OS《最小闭环》）。
> - ❌ **这里暂无**：三本书的完整正文——完整正典分布在下方三个源仓，本仓正逐章孵化精炼版。各书进度见下表。

### 各书当前状态（诚实进度）

| 书 | 本仓进度 | 已成稿样章 | 完整正典源仓 |
|---|---|---|---|
| **① 原力资产**（向内·人） | 骨架 + 1/6 章 | [第一章·觉察](books/01-原力资产/第一章-觉察.md) ✅ | 觉醒 + 守富 canon，见 [strategy-playbook](https://github.com/moonstachain/yuanli-strategy-playbook) |
| **② 原力创业**（向外·事·左腿） | 骨架 · 0 章 | — | [startup-map-site](https://github.com/moonstachain/yuanli-startup-map-site)（六卷通关地图 + 交互站 h5.odysseyinst.com/qishi） |
| **③ 原力OS**（向上·法·右腿） | 骨架 + 教学样章 | [最小闭环](books/03-原力OS/最小闭环.md) ✅ | [os-greenbook](https://github.com/moonstachain/yuanli-os-greenbook)（4 部 55 章） |

---

## 一公理 → 两条腿 → 三本书

母公理 **ʸx ＝ 做会自我繁殖的事**（药不是药渣，是药引；你睡觉时它还在长）。它是个动词，必须有主语和宾语，于是长出三本书：

| # | 书 | 它答的第一性问题 | 模型意象 | 量级 |
|---|---|---|---|---|
| 一 | **原力资产**（向内·人） | AI 时代你凭什么不可替代？怎么成为会复利的资产？ | **原力U**（U型理论·下潜到源头再上升） | 找到母体 · 1 |
| 二 | **原力创业**（向外·事·左腿） | 怎么把「你」变成一门跨得过鸿沟、守得住周期的生意？ | **跨越鸿沟**（四关：借势→独创→升维→锁定） | 1 → 万 |
| 三 | **原力OS**（向上·法·右腿） | 怎么让做事本身自我进化，不靠人力堆叠？ | **莫比乌斯环 · 复杂自适应系统**（四部：信念→图景→工具→身份） | x·y → ʸx · ×万倍 |

> **「财富」不是第三本书**——它是创业这条腿的产出度量（1→万是变现，万→亿的守富＝创业锁定关+资产复利尾）。专讲守富/资产配置/穿越周期的内容另拆未来《原力财富》spin-off，不属于本三部曲。
> **原力OS** 既是第三本书（右腿/工作投影），又同时是贯穿涡轮——给资产+创业的每个动作装上自我进化的引擎。

---

## 仓里有什么（知识层 SSOT）

```
trilogy/
├── 原力三部曲-概念地图.html        ⭐ 知识地图 v2（通关链：篇篇独立 MECE · 章章连贯因为→所以 · 层层递进）
│                                      = 三本绿皮书的「结构真源」（正文顺此图写·逐章孵化，非成书正文仓）
├── 原力三部曲-文脉骨架座舱.html     体系关系图（深空蓝·三本书怎么咬合）
├── 原力三部曲-文脉总纲.md           顶层文脉总纲
├── 原力战略三部曲-重构骨架设计稿.md  第一性重构骨架（究竟·完备·具体·递归）
├── 原力三部曲-基石与关键概念-全谱.md  字典层全谱
├── 原力资产-基石与关键概念-全谱.md    资产分册全谱（按原力U五阶）
├── 原力OS-信雅达双轨改名表.md         OS 术语双轨改名（专业名×白话副名）
├── _atlas/atlas-v2-*.json            知识地图数据层（macro/zichan/chuangye/os/mece）
└── build_atlas.py                    渲染层：读 _atlas/*.json → 生成知识地图.html

books/                                三本绿皮书正文（骨架·从知识地图通关链写进来）
├── 01-原力资产/  02-原力创业/  03-原力OS/
```

**判断/渲染分离**：所有 HTML 都是构建产物——内容在 `_atlas/*.json`（数据），样式在 `build_*.py`（渲染）。改数据重跑对应脚本即更新，改样式不碰数据。

---

## 本地构建（零依赖）

**环境**：Python ≥ 3.8，纯标准库（`json` / `html` / `pathlib` / `glob`），**无第三方依赖，无需 `pip install`**。

| 脚本 | 产出 |
|---|---|
| `trilogy/build_atlas.py` | `trilogy/原力三部曲-概念地图.html`（概念地图·通关链） |
| `trilogy/build_master_outline.py` | `trilogy/原力战略三部曲-总纲.html`（一体化四级总纲） |
| `trilogy/build_outline.py` | `trilogy/原力三部曲-提纲架构.html`（读 `_atlas/outline.json`） |
| `trilogy/build_zichan_outline.py` | `trilogy/原力资产-四级目录.html` |
| `trilogy/build_book_outline.py <outline>.json` | 创业/OS 四级目录（传参 `chuangye-outline.json` / `os-outline.json`） |
| `review/build_review.py` | `review/index.html`（写作复盘看板） |
| `build_portal.py`（仓根） | `index.html`（门户首页 · GitHub Pages 入口 · 自动扫 `books/` 统计各书已写章数） |
| `apply_nav.py`（仓根） | 给各页注入统一 sticky 导航（数据源 `_nav.py`；幂等，可重复跑） |

**全量重建**：

```bash
cd trilogy
python3 build_atlas.py && python3 build_master_outline.py && python3 build_outline.py
python3 build_zichan_outline.py
python3 build_book_outline.py chuangye-outline.json && python3 build_book_outline.py os-outline.json
cd .. && python3 review/build_review.py && python3 build_portal.py && python3 apply_nav.py
```

---

## 正典与出处（链回源仓·单一真源）

本仓是三部曲的**知识总纲**；各书的既有正典正文留在其原仓，不在此重复：

- **原力战略·白皮书 + 绿皮书六册**（道体法术器守）→ [moonstachain/yuanli-strategy-playbook](https://github.com/moonstachain/yuanli-strategy-playbook)　·　资产书的觉醒/守富底料由此册投影
- **原力创业·通关地图六卷 + 交互网站**（h5.odysseyinst.com/qishi）→ [moonstachain/yuanli-startup-map-site](https://github.com/moonstachain/yuanli-startup-map-site)
- **借势合力·通关地图绿皮书 v1.0** → [moonstachain/yuanli-startup-map-book](https://github.com/moonstachain/yuanli-startup-map-book)
- **原力OS·绿皮书**（4 部 55 章 · 物种转移指南）→ [moonstachain/yuanli-os-greenbook](https://github.com/moonstachain/yuanli-os-greenbook)　·　OS 书正文正典

白皮书是**公理 umbrella**（不增新概念，只立公理）；本三部曲是它在「资产/创业/OS」三个维度的投影。

---

## 怎么用这张图写书

知识地图 v2 是一条**通关链**：每本书 = 一条 model-shaped 链，**节点＝章、关键词＝节、因为＝章间过渡、递进＝章节顺序**。写正文时顺着通关链逐章逐节写——每个节点的「第一性问题 / 定义 / 关键词派生链 / 真源」就是写作种子。

视觉：qishi 翡翠墨绿 × 鎏金（`#0d2018 × #c9a961`）。
