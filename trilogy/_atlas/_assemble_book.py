#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""装配《原力创业》/《原力OS》四级目录数据。用法：python3 _assemble_book.py <cy|os>
读 /tmp/cy-os-l4/{cy|os}{1..4}.json + 章级 meta + 书级框架 + critic 判定（结构化返回的权威值）
→ 写 _atlas/{chuangye|os}-outline.json。判断/渲染分离：渲染在 build_book_outline.py。"""
import json, pathlib, sys
SRC = pathlib.Path("/tmp/cy-os-l4")
OUT = pathlib.Path(__file__).parent
which = sys.argv[1] if len(sys.argv) > 1 else "cy"

BOOKS = {
  "cy": {
    "keys": ["cy1", "cy2", "cy3", "cy4"], "outfile": "chuangye-outline.json",
    "book": "原力创业", "en": "YUANLI VENTURE · 4-LEVEL OUTLINE", "subtitle": "向外 · 事 · 左腿",
    "axiom": "财富 ＝ 借势 × 合力（把『做自己』变成跨过鸿沟、守得住周期的生意）",
    "model": "跨越鸿沟（Crossing the Chasm）", "arc_label": "跨越鸿沟 · 四关",
    "arc": "四关＝四个生死端口，一关过不了后面白搭：借势（输入端·我能不能持续做）→ 独创（市场端·市场认不认）→ 升维（变现端·赚不赚得到）→ 锁定（防御端·守不守得住）。",
    "note": "这份目录是逐节写《原力创业》正文的写作单元真源。四关＝财富＝借势×合力的展开；脊骨概念在四关语境发展而非复制（标 REF→资产），财富为创业产出度量（不另立财富书）。过五标准后与资产同为金标准。",
    "ch_meta": {
      1: ("关一 · 输入端（最发散）", "第一关 · 借势", "我能不能持续做？——看懂别人没看懂的康波套利窗口，且合天赋人格之力？"),
      2: ("关二 · 市场端（收成一句）", "第二关 · 独创", "市场认不认？——跳出红海做成无法被归类、用户自带预算来买的新品类？"),
      3: ("关三 · 变现端（收成一仗）", "第三关 · 升维", "赚不赚得到？——跑通成不靠我亲自下场也能赚钱、可复制的模式机器？"),
      4: ("关四 · 防御端（收成一图）", "第四关 · 锁定", "守不守得住？——利润焊死十年不被巨头收割、穿越下一个周期？"),
    },
    # critic：来自 workflow 结构化返回（权威·不读 agent 写的 critic.json）
    "critic": {
      "jiujing": True, "wanbei": True, "dijin": True, "juti": True, "digui": True, "verdict": "pass", "fabricated": [],
      "weakest": "关四·锁定（cy4）——四维护城/16控点/30法则骨架完整且全部 grounded，但部分目（虚/入/出壁垒）依赖密集案例名串而非原子锚，落笔单元略偏「案例罗列」；「原力人生融合·左手现金右手雪球」一目最贴近《原力财富》边界，已用『借势×合力产出度量·非独立财富书』守住。另：cy3 升维的 财链路/利润池/看似贵 三节都走定价议题、章级 MECE 最不脆（用不同透镜重组、非臆造）。",
    },
  },
  "os": {
    "keys": ["os1", "os2", "os3", "os4"], "outfile": "os-outline.json",
    "book": "原力OS", "en": "YUANLI OS · 4-LEVEL OUTLINE", "subtitle": "向上 · 法 · 右腿",
    "axiom": "ʸx —— 把『一个你』升级成『会造物的物种』（x·y → ʸx）",
    "model": "莫比乌斯环 · 复杂自适应系统", "arc_label": "莫比乌斯 · 四部",
    "arc": "四部＝过程（怎么从 x·y 转到 ʸx）：信念部（为什么转）→ 图景部（转向哪）→ 工具部（怎么转）→ 身份部（转完是谁）。转完交付元AI 四套（一纸文脉/一个大脑/一张地图/一条链路）。",
    "note": "这份目录是逐节写《原力OS》正文的写作单元真源。四部＝过程，身份部后 4 节＝元AI 四套交付物（呼应提纲 delivers 的器官/真实系统/成熟度）；四套 last-mile 薄处（说明书范本/蒸馏停/验证轴空）诚实标〔待补〕，不臆造。",
    "ch_meta": {
      1: ("第一部 · 为什么转（物种切换）", "信念部", "为什么必须转？——杠杆载体从碳基切到硅基，守着 x·y 的老物种会被碾过去吗？"),
      2: ("第二部 · 转向哪（硅基定律）", "图景部", "转向哪、按什么硅基物理定律转？——有没有一组违反就被拖累的定律？"),
      3: ("第三部 · 怎么转（代谢系统）", "工具部", "怎么转、靠什么日夜不停地转？——装什么代谢系统让它自己吸收、消化、繁殖？"),
      4: ("第四部 · 转完是谁（出口考试）", "身份部", "转完是谁、出口考什么？——造出下一个造物者算不算过？"),
    },
    "critic": {
      "jiujing": True, "wanbei": True, "dijin": True, "juti": True, "digui": True, "verdict": "pass", "fabricated": [],
      "weakest": "身份部（os4）·四套器官节（一个大脑/一张地图/一条链路）的 system＋组件数＋成熟度 来自 outline `delivers` 上游产物，无法在 atlas/改名表里二次验真——289/2051 组件、🟢/🟡 等靠真实系统快照背书（数字真实、随系统演进会变、已诚实标〔待补〕），是全书 grounding 最薄处；身份部四处 last-mile（文脉血肉在填/大脑蒸馏停/地图复利没接/链路验证轴空）按纪律诚实标〔待补〕，是真实成熟度非缺陷。另：os3 工具部「三化改造」第5目为 meta-桥接评注而非 MECE 平级目。",
    },
  },
}
B = BOOKS[which]
chapters = []
for i, key in enumerate(B["keys"], 1):
    d = json.load(open(SRC / f"{key}.json", encoding="utf-8"))
    layer, title, q = B["ch_meta"][i]
    nsub = sum(len(s["subs"]) for s in d["sections"])
    chapters.append({"seq": i, "name": d["name"], "title": title, "layer": layer,
                     "q": q, "nsec": len(d["sections"]), "nsub": nsub,
                     "sections": d["sections"]})

cr = B["critic"]
total_sec = sum(c["nsec"] for c in chapters)
total_sub = sum(c["nsub"] for c in chapters)
doc = {
    "book": B["book"], "en": B["en"], "subtitle": B["subtitle"], "axiom": B["axiom"],
    "model": B["model"], "arc_label": B["arc_label"], "arc": B["arc"], "note": B["note"],
    "standard": {"checks": [
        ["究竟", cr["jiujing"], "每个目都能回溯到公理 ʸx——必然展开，不是硬凑"],
        ["完备", cr["wanbei"], "每节下的目 MECE（互斥穷尽·不漏不重）"],
        ["递进", cr["dijin"], "目按「因为→所以」排成一条小通关链"],
        ["具体", cr["juti"], "每个目是可直接落笔的内容单元，不是抽象标签"],
        ["递归", cr["digui"], "节→目 与 章→节 同形状（部分即整体·CAS）"],
    ], "verdict": cr["verdict"], "fabricated": cr.get("fabricated", []), "weakest": cr.get("weakest", "")},
    "stats": {"books": 1, "chapters": len(chapters), "sections": total_sec, "subs": total_sub},
    "chapters": chapters,
}
(OUT / B["outfile"]).write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {B['outfile']} | {len(chapters)} 章 / {total_sec} 节 / {total_sub} 目 | verdict={cr['verdict']}")
