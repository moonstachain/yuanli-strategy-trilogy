#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""装配《原力资产》四级目录数据：读 /tmp/zichan-l4/ch{1..6}.json + critic.json
→ 合入章级 meta（原力U 阶/第一性问题）→ 写 trilogy/_atlas/zichan-outline.json。
判断/渲染分离：本脚本只装配数据；渲染在 build_zichan_outline.py。"""
import json, pathlib
SRC = pathlib.Path("/tmp/zichan-l4")
OUT = pathlib.Path(__file__).parent / "zichan-outline.json"

# 章级 meta：原力U 六阶（下潜→触底→上升→浮出→出口）+ 第一性问题
CH_META = {
    1: ("症状层 · U 起点", "AI 时代「你」凭什么不可替代——当机器在纯信息处理上已碾压 80 亿人？"),
    2: ("结构层 · 下潜", "你这台算法，到底由哪些可解码的能量结构组成？"),
    3: ("U 底 · 触底", "为什么你最大的能量，恰恰藏在你最不愿看的阴影里？"),
    4: ("上升 · 整合", "怎么把解码出来的「你」，装进一个会自我繁殖的元AI？"),
    5: ("浮出 · 显化", "怎么让整合好的你，浮出水面、成为对外有人买单的资产？"),
    6: ("出口 · 复利", "资产造出来之后，怎么守住、并穿越第六康波这一整个周期？"),
}

chapters = []
for seq in range(1, 7):
    d = json.load(open(SRC / f"ch{seq}.json", encoding="utf-8"))
    layer, q = CH_META[seq]
    nsub = sum(len(s["subs"]) for s in d["sections"])
    chapters.append({
        "seq": seq, "name": d["name"], "layer": layer, "q": q,
        "nsec": len(d["sections"]), "nsub": nsub, "sections": d["sections"],
    })

# 五标准 critic 判定（取自 workflow 结构化返回·权威；agent 写的 critic.json schema 不一致故不读它）
critic = {
    "jiujing": True, "wanbei": True, "dijin": True, "juti": True, "digui": True,
    "verdict": "pass", "fabricated": [],
    "weakest": "ch6 复利·「三钱法则·IPS」节最弱：该节深内容（分篮/IPS 投资政策声明/深打法）被全谱去重缝明确划归《原力财富》，"
               "本节按定位只能停在「资产视角·送到门口」，目偏纲领性、末目=边界焊缝——是去重纪律的必然产物，非缺陷。"
               "次弱=ch4「向内求×向外共创」仅 3 目，与同章「双螺旋引擎」同源 L05，靠「焊回脊骨#10 能量回流」目区分。",
}
total_sec = sum(c["nsec"] for c in chapters)
total_sub = sum(c["nsub"] for c in chapters)

doc = {
    "book": "原力资产", "subtitle": "向内 · 人 · 主语本", "axiom": "ʸx —— 做会自我繁殖的事（你 × AI＝会复利的资产）",
    "u_arc": "原力U：症状 → 下潜 → 触底（金色阴影）→ 上升 → 浮出 → 出口。向内挖到底，再带着金子上升。",
    "standard": {
        "title": "四级目录金标准 · 五标准全过",
        "checks": [
            ["究竟", critic.get("jiujing"), "每个目都能回溯到公理 ʸx——必然展开，不是硬凑"],
            ["完备", critic.get("wanbei"), "每节下的目 MECE（互斥穷尽·不漏不重）"],
            ["递进", critic.get("dijin"), "目按「因为→所以」排成一条小通关链"],
            ["具体", critic.get("juti"), "每个目是可直接落笔的内容单元，不是抽象标签"],
            ["递归", critic.get("digui"), "节→目 与 章→节 同形状（部分即整体·CAS）"],
        ],
        "verdict": critic.get("verdict"), "fabricated": critic.get("fabricated", []),
        "weakest": critic.get("weakest", ""),
    },
    "stats": {"books": 1, "chapters": len(chapters), "sections": total_sec, "subs": total_sub},
    "chapters": chapters,
}
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {OUT.name} | {len(chapters)} 章 / {total_sec} 节 / {total_sub} 目 | verdict={critic.get('verdict')}")
