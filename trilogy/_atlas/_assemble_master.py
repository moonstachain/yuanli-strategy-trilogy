#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""装配《原力战略三部曲·总纲》一体化数据（合并·判断渲染分离）。
合并：outline.json（公理/康波/macro/spine/seams/reasoning）+ 三本四级目录 JSON（604目）
     + /tmp/master/weave.json（脊骨穿透矩阵）+ shapes（三形状）+ main_root → trilogy-master-outline.json。"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
def L(n): return json.load(open(HERE / n, encoding="utf-8"))
O = L("outline.json")
weave = json.load(open("/tmp/master/weave.json", encoding="utf-8"))["weave"]

# 三本：取四级目录 JSON（含 604 目）+ 补 seq/axis/scale/tier
META = {
    "原力资产": {"seq": 1, "axis": "向内 · 人", "scale": "1", "tier": "主语本体"},
    "原力创业": {"seq": 2, "axis": "向外 · 事 · 左腿", "scale": "1 → 万", "tier": "利润容器"},
    "原力OS":  {"seq": 3, "axis": "向上 · 法 · 右腿", "scale": "×万倍", "tier": "造物班底"},
}
files = {"原力资产": "zichan-outline.json", "原力创业": "chuangye-outline.json", "原力OS": "os-outline.json"}
books = []
for bn, fn in files.items():
    d = L(fn); m = META[bn]
    books.append({
        "seq": m["seq"], "name": bn, "axis": m["axis"], "scale": m["scale"], "tier": m["tier"],
        "subtitle": d.get("subtitle", ""), "axiom": d.get("axiom", ""), "model": d.get("model", ""),
        "arc_label": d.get("arc_label", ""), "arc": d.get("arc", ""), "standard": d.get("standard", {}),
        "stats": d.get("stats", {}), "chapters": d["chapters"],
    })
books.sort(key=lambda b: b["seq"])

# 三形状（U→鸿沟→莫比乌斯 ＝ 1→万→∞）·取自三本理论模型
shapes = {
    "title": "三形状 · 同一条 ʸx 螺旋的三段",
    "synthesis": "U（向内挖·凹）→ 鸿沟（向外跨·缺口）→ 莫比乌斯（向上接成闭环·无缝）＝ 1 → 万 → ∞。三段拼起来是一条首尾相衔、单面无缝的螺旋——终点即起点，起点更高。",
    "items": [
        {"book": "原力资产", "shape": "U 型 · 向内挖（凹）", "model": "U 型理论（Scharmer）", "level": "1", "glyph": "U",
         "desc": "冰山下潜到金色阴影、触底，再带着金子上升——向内挖到底才有真东西浮出。"},
        {"book": "原力创业", "shape": "鸿沟 · 向外跨（缺口）", "model": "跨越鸿沟（Moore）", "level": "万", "glyph": "chasm",
         "desc": "独创↔升维之间那道死亡缺口，用保龄球一格格压过去——跨过去才有万倍市场。"},
        {"book": "原力OS", "shape": "莫比乌斯 · 向上闭环（无缝）", "model": "莫比乌斯环 · CAS", "level": "∞", "glyph": "mobius",
         "desc": "单面闭环，你睡觉它还在长——部分即整体，输出回灌入口，终点即起点。"},
    ],
}
main_root = {"name": "原力资产（主根）",
             "note": "唯一穿三部、还向上提的那条根：资产里是主语本体，创业里是借势弹药 + 非对称壁垒，OS 里是「一纸文脉」的灵魂语料。"}

total_sec = sum(b["stats"].get("sections", 0) for b in books)
total_sub = sum(b["stats"].get("subs", 0) for b in books)
doc = {
    "title": "原力战略三部曲 · 总纲", "subtitle": "一体化四级大纲 · 一公理 → 三书 → 14章 → 138节 → 604目",
    "axiom": O["axiom"], "kangbo": O.get("kangbo", {}), "macro": O["macro"],
    "books": books, "spine": O["spine"], "main_root": main_root, "weave": weave,
    "seams": O["seams"], "wealth_note": O.get("wealth_note", ""), "shapes": shapes, "reasoning": O["reasoning"],
    "stats": {"books": len(books), "chapters": sum(len(b["chapters"]) for b in books), "sections": total_sec, "subs": total_sub},
}
(HERE / "trilogy-master-outline.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote trilogy-master-outline.json | {doc['stats']['books']} 书 / {doc['stats']['chapters']} 章 / {total_sec} 节 / {total_sub} 目 | weave {len(weave)} 脊骨")
