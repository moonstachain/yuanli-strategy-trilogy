#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原力战略三部曲 · 门户渲染器（数据驱动·判断/渲染分离）。
读 portal-map.json + roadmap.json + trilogy/_atlas/*.json + 扫 books/ → index.html。
活看板：正文进度自动扫 books/ 已写章节；元AI四套读 outline.json delivers；复盘读 review/history.jsonl。
每写一章 / 加一行数据 → 重跑即长。末尾跑孤儿审计（仓内 *.html 是否全收）。"""
import json, html, pathlib, glob, sys
HERE = pathlib.Path(__file__).parent
def e(s): return html.escape(str(s)) if s is not None else ""
def J(p): return json.load(open(HERE / p, encoding="utf-8"))
CN = "〇一二三四五六七八九十"
def cn(n): return CN[n] if 0 <= n < 11 else str(n)

PM = J("portal-map.json"); RM = J("roadmap.json")
OUTLINE = J("trilogy/_atlas/outline.json")
HISTORY = [json.loads(l) for l in open(HERE / "review/history.jsonl", encoding="utf-8") if l.strip()] if (HERE / "review/history.jsonl").exists() else []
MAT = {"G": ("🟢", "#5a9c6e"), "A": ("🟡", "#c9a961"), "R": ("🔴", "#c0524a")}
ST = {"live": ("✅", "在线"), "writing": ("🚧", "在写"), "planned": ("🔮", "规划")}
linked = set()   # 收集所有渲染出的 href（孤儿审计用）

def reg(href):
    if href: linked.add(href.split("#")[0])
    return href

# ---------- 三本书：扫 books/ 算真实进度 ----------
def book_progress(b):
    od = J(f"trilogy/_atlas/{b['outline']}")
    chapters = [{"name": c["name"], "title": c.get("title") or f"第{cn(c['seq'])}章", "seq": c["seq"],
                 "nsub": sum(len(s["subs"]) for s in c["sections"]), "written": False, "href": None} for c in od["chapters"]]
    extras = []
    for f in sorted(glob.glob(str(HERE / b["dir"] / "*.html"))):
        stem = pathlib.Path(f).stem
        rel = str(pathlib.Path(f).relative_to(HERE))
        hit = next((c for c in chapters if c["name"] in stem), None)
        if hit and not hit["written"]:
            hit["written"] = True; hit["href"] = rel
        else:
            extras.append({"title": stem, "href": rel})
    nw = sum(1 for c in chapters if c["written"])
    return {"meta": b, "stats": od["stats"], "chapters": chapters, "extras": extras, "n_written": nw, "n_total": len(chapters)}

BOOKS = [book_progress(b) for b in PM["books"]]
TOT_CH = sum(b["n_total"] for b in BOOKS)
TOT_W = sum(b["n_written"] for b in BOOKS)
TOT_PIECES = TOT_W + sum(len(b["extras"]) for b in BOOKS)
TOT_SEC = sum(b["stats"]["sections"] for b in BOOKS)
TOT_SUB = sum(b["stats"]["subs"] for b in BOOKS)

def card(en):
    badge, _ = ST.get(en.get("status", "live"), ("", ""))
    cls = "card feature" if en.get("feature") else "card"
    return f'''<a class="{cls}" href="{e(reg(en["href"]))}">
  <div class="c-h"><span class="ic">{e(en.get("icon",""))}</span><span class="ttl">{e(en["title"])}</span><span class="st">{badge}</span></div>
  <div class="dsc">{e(en["desc"])}</div>
  <div class="when">何时点进来 · {e(en.get("when",""))}</div></a>'''

def book_block(bp):
    b = bp["meta"]; pct = round(100 * bp["n_written"] / bp["n_total"]) if bp["n_total"] else 0
    chips = ""
    for c in bp["chapters"]:
        if c["written"]:
            chips += f'<a class="chap done" href="{e(reg(c["href"]))}">✅ {e(c["title"])} · {e(c["name"])}</a>'
        else:
            chips += f'<span class="chap todo">🔮 {e(c["title"])} · {e(c["name"])}<span class="cn">{c["nsub"]}目</span></span>'
    extra = "".join(f'<a class="chap extra" href="{e(reg(x["href"]))}">📖 {e(x["title"])}<span class="cn">专题</span></a>' for x in bp["extras"])
    note = f'<div class="bk-note">💰 {e(b["note"])}</div>' if b.get("note") else ""
    return f'''<div class="bk">
  <div class="bk-head"><span class="bk-seal">{cn(b["seq"])}</span><div class="bk-id">
    <div class="bk-n">《{e(b["name"])}》<span class="bk-ax">{e(b["axis"])} · {e(b["scale"])} · 模型＝{e(b["model"])}</span></div>
    <div class="bk-q">{e(b["question"])}</div></div>
    <a class="bk-l4" href="{e(reg(b["l4"]))}">📑 四级目录<span class="l4c">{bp["stats"]["chapters"]}章 {bp["stats"]["sections"]}节 <b>{bp["stats"]["subs"]}</b>目</span></a></div>
  <div class="prog"><div class="prog-bar"><span style="width:{pct}%"></span></div><span class="prog-t">正文 {bp["n_written"]}/{bp["n_total"]} 章{(" · +"+str(len(bp["extras"]))+" 专题") if bp["extras"] else ""}</span></div>
  <div class="chaps">{chips}{extra}</div>{note}</div>'''

# ---------- 元AI 四套（读 delivers）----------
dv = OUTLINE["books"][2].get("delivers", {})
organs = ""
for o in dv.get("organs", []):
    dot, col = MAT.get(o.get("mat", "A"), ("🟡", "#c9a961"))
    organs += f'''<div class="organ" style="--mc:{col}"><div class="o-h"><span class="o-n">{e(o["name"])}</span><span class="o-or">{e(o["organ"])}</span><span class="o-m">{dot}</span></div>
  <div class="o-d">{e(o["def"])}</div><div class="o-s">真实系统 · {e(o["system"])}</div><div class="o-mn">{e(o["mnote"])}</div></div>'''

# ---------- 复盘轨迹（读 history）----------
htrack = "".join(
    f'<div class="ht"><span class="ht-c">{e(h.get("chapter",""))}</span><span class="ht-bars">'
    f'共鸣 <b>{h.get("F_共鸣","-")}</b> · 可信 <b>{h.get("T_可信","-")}</b> · 共识 <b>{h.get("F_共识","-")}</b></span>'
    f'<span class="ht-o">自评 {h.get("overall_self","-")}</span></div>' for h in HISTORY)

# ---------- 路线图 ----------
def rlist(items): return "".join(f'<li>{e(x)}</li>' for x in items)
future = "".join(f'<div class="fb"><b>{e(f["name"])}</b><span class="fb-s">{e(f["status"])}</span><div class="fb-n">{e(f["note"])}</div></div>' for f in RM.get("future_books", []))

M = PM["meta"]
ov_cards = "".join(card(x) for x in PM["overview"])
pl_cards = "".join(card(x) for x in PM["pipeline"])
books_html = "".join(book_block(b) for b in BOOKS)

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{e(M["title"])} · 门户</title>
<meta name="description" content="{e(M["tagline"])}"/>
<style>
:root{{--ink:#0a1612;--leather-deep:#0d2018;--panel:rgba(20,48,31,.55);--panel2:rgba(28,61,41,.4);
--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;
--jade:#5a9c6e;--cream:#f0e6d2;--cream-dim:#d3c8b0;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.2);--line2:rgba(201,169,97,.1);
--serif:"Noto Serif SC","Songti SC",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}}
*{{box-sizing:border-box;margin:0;padding:0}} html{{scroll-behavior:smooth}}
body{{background:radial-gradient(1200px 700px at 80% -10%,rgba(74,124,89,.16),transparent 60%),radial-gradient(900px 600px at 4% 104%,rgba(201,169,97,.07),transparent 55%),linear-gradient(180deg,var(--ink),var(--leather-deep) 50%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:1.75;padding:0 0 70px}}
.foil{{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 52%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 24px}}
header{{text-align:center;padding:62px 24px 18px}}
.kick{{font-family:var(--display);font-size:12px;letter-spacing:.5em;color:var(--gold);text-transform:uppercase;margin-bottom:18px}}
h1{{font-weight:600;font-size:clamp(34px,6.4vw,60px);letter-spacing:.16em}}
.tag{{margin-top:16px;font-size:15px;color:var(--gold-light);letter-spacing:.04em}}
.ax{{margin:16px auto 0;max-width:660px;font-family:var(--mono);font-size:12px;color:var(--cream-dim);border:1px solid var(--line);border-radius:11px;padding:11px 16px;background:var(--panel2);line-height:1.7}}
.ax b{{color:var(--gold-bright)}}
.kpis{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:16px}}
.kpi{{font-family:var(--mono);font-size:12px;color:var(--gold-light);padding:5px 12px;border-radius:6px;background:rgba(201,169,97,.06);border-left:2px solid var(--gold)}}
.kpi b{{color:var(--gold-bright);font-size:14px}} .kpi.live{{border-left-color:var(--jade)}} .kpi.live b{{color:var(--jade)}}
/* nav */
nav{{position:sticky;top:0;z-index:9;background:rgba(10,22,18,.86);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);margin-top:18px}}
nav .nin{{max-width:1080px;margin:0 auto;padding:11px 24px;display:flex;gap:7px;flex-wrap:wrap;justify-content:center}}
nav a{{font-family:var(--sans);font-size:12px;color:var(--muted);text-decoration:none;padding:5px 12px;border-radius:7px;border:1px solid transparent;transition:.15s}}
nav a:hover{{color:var(--gold-bright);border-color:var(--line);background:rgba(201,169,97,.05)}}
/* section label */
.sl{{display:flex;align-items:baseline;gap:13px;margin:44px 0 16px}}
.sl .rn{{font-family:var(--display);font-size:13px;color:var(--gold);letter-spacing:.1em}} .sl .n{{font-family:var(--serif);font-size:19px;color:var(--gold-bright)}}
.sl .ln{{flex:1;height:1px;background:var(--line)}} .sl .hint{{font-family:var(--sans);font-size:11px;color:var(--faint)}}
/* cards */
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:15px}}
.card{{display:block;text-decoration:none;color:inherit;border:1px solid var(--line);border-radius:13px;background:var(--panel);padding:18px 20px;transition:.18s;position:relative;overflow:hidden}}
.card::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--gold);opacity:.6;transition:.18s}}
.card:hover{{border-color:var(--gold);transform:translateY(-2px);box-shadow:0 12px 30px rgba(0,0,0,.32)}} .card:hover::before{{opacity:1;width:4px}}
.card.feature{{grid-column:1/-1;background:linear-gradient(110deg,var(--panel),rgba(168,54,44,.05));border-top:3px solid var(--gold)}} .card.feature::before{{display:none}}
.c-h{{display:flex;align-items:baseline;gap:9px}} .ic{{font-size:20px}} .ttl{{font-size:18px;color:var(--gold-bright)}} .card.feature .ttl{{font-size:22px}} .st{{margin-left:auto;font-size:12px}}
.dsc{{font-size:13px;color:var(--cream-dim);margin-top:9px;line-height:1.7}} .when{{font-family:var(--sans);font-size:11px;color:var(--faint);margin-top:9px;border-top:1px solid var(--line2);padding-top:7px}}
/* books */
.bk{{border:1px solid var(--line);border-radius:14px;background:var(--panel);padding:18px 20px;margin-bottom:14px}}
.bk-head{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}}
.bk-seal{{font-family:var(--serif);font-size:18px;color:var(--gold-bright);width:40px;height:40px;flex:none;display:flex;align-items:center;justify-content:center;border:1px solid var(--gold);border-radius:50%}}
.bk-id{{flex:1;min-width:200px}} .bk-n{{font-family:var(--serif);font-size:20px;color:var(--gold-bright)}} .bk-ax{{font-family:var(--mono);font-size:10.5px;color:var(--cinnabar-soft);margin-left:9px}}
.bk-q{{font-family:var(--sans);font-size:12px;color:var(--muted);margin-top:3px}}
.bk-l4{{text-decoration:none;color:var(--gold-light);font-family:var(--sans);font-size:12px;border:1px solid var(--line);border-radius:9px;padding:8px 13px;transition:.15s;white-space:nowrap}} .bk-l4:hover{{border-color:var(--gold);background:rgba(201,169,97,.06)}} .l4c{{display:block;font-family:var(--mono);font-size:10px;color:var(--faint);margin-top:2px}} .l4c b{{color:var(--gold)}}
.prog{{display:flex;align-items:center;gap:11px;margin:13px 0 11px}}
.prog-bar{{flex:1;height:7px;background:rgba(0,0,0,.3);border-radius:4px;overflow:hidden}} .prog-bar span{{display:block;height:100%;background:linear-gradient(90deg,var(--gold-deep),var(--gold-bright));border-radius:4px}}
.prog-t{{font-family:var(--mono);font-size:11px;color:var(--gold-light);white-space:nowrap}}
.chaps{{display:flex;flex-wrap:wrap;gap:7px}}
.chap{{font-family:var(--sans);font-size:12px;text-decoration:none;border-radius:8px;padding:6px 11px;border:1px solid var(--line2)}}
.chap.done{{color:var(--gold-bright);background:rgba(201,169,97,.1);border-color:var(--gold-deep)}} .chap.done:hover{{background:rgba(201,169,97,.18)}}
.chap.todo{{color:var(--faint);background:rgba(0,0,0,.13)}} .chap.extra{{color:var(--jade);border-color:var(--jade)}} .chap.extra:hover{{background:rgba(90,156,110,.1)}}
.cn{{font-family:var(--mono);font-size:9px;opacity:.7;margin-left:5px}}
.bk-note{{font-family:var(--sans);font-size:11px;color:var(--muted);margin-top:11px;border-left:2px solid var(--cinnabar);padding:6px 12px;background:rgba(168,54,44,.05);border-radius:0 7px 7px 0;line-height:1.7}}
/* systems / 元AI四套 */
.organs{{display:grid;grid-template-columns:repeat(2,1fr);gap:13px}}
.organ{{border:1px solid var(--line);border-top:3px solid var(--mc);border-radius:12px;background:var(--panel);padding:14px 16px}}
.o-h{{display:flex;align-items:baseline;gap:9px}} .o-n{{font-family:var(--serif);font-size:17px;color:var(--gold-bright)}} .o-or{{font-family:var(--mono);font-size:10.5px;color:var(--mc)}} .o-m{{margin-left:auto}}
.o-d{{font-size:12.5px;color:var(--cream-dim);margin:7px 0 6px;line-height:1.6}} .o-s{{font-family:var(--sans);font-size:11px;color:var(--gold-light);border-top:1px solid var(--line2);padding-top:6px}} .o-mn{{font-family:var(--sans);font-size:10.5px;color:var(--muted);margin-top:3px}}
.flow{{margin-top:12px;font-family:var(--sans);font-size:12px;color:var(--gold-light);padding:9px 14px;background:rgba(201,169,97,.05);border-radius:9px;line-height:1.75}}
.lastmile{{margin-top:8px;font-family:var(--sans);font-size:11.5px;color:var(--cream-dim);padding:8px 14px;border:1px dashed rgba(192,82,74,.4);border-radius:9px;line-height:1.7}}
/* roadmap */
.cols3{{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}}
.rmcard{{border:1px solid var(--line);border-radius:12px;background:var(--panel2);padding:15px 18px}} .rmcard h4{{font-family:var(--serif);font-size:14px;color:var(--gold-bright);margin-bottom:9px;font-weight:600}}
.rmcard ul{{list-style:none}} .rmcard li{{font-family:var(--sans);font-size:12px;color:var(--cream-dim);padding:5px 0 5px 16px;position:relative;line-height:1.6}} .rmcard li::before{{content:"▸";position:absolute;left:0;color:var(--gold-deep)}}
.rm-now{{border-top:2px solid var(--jade)}} .rm-near{{border-top:2px solid var(--gold)}} .rm-far{{border-top:2px solid var(--faint)}}
.htrack{{border:1px solid var(--line);border-radius:11px;background:var(--panel2);padding:12px 16px;margin-top:11px}}
.ht{{display:flex;align-items:baseline;gap:11px;padding:5px 0;border-bottom:1px solid var(--line2);font-size:12px;flex-wrap:wrap}} .ht-c{{font-family:var(--serif);color:var(--gold-light);min-width:110px}} .ht-bars{{font-family:var(--sans);font-size:11px;color:var(--cream-dim)}} .ht-bars b{{color:var(--gold-bright)}} .ht-o{{margin-left:auto;font-family:var(--mono);font-size:11px;color:var(--gold)}}
.future{{display:grid;grid-template-columns:1fr 1fr;gap:11px;margin-top:12px}}
.fb{{border:1px dashed var(--line);border-radius:10px;padding:11px 15px}} .fb b{{font-family:var(--serif);font-size:15px;color:var(--gold-light)}} .fb-s{{font-family:var(--sans);font-size:11px;color:var(--cinnabar-soft);margin-left:8px}} .fb-n{{font-family:var(--sans);font-size:11px;color:var(--muted);margin-top:5px;line-height:1.6}}
.selfdoc{{max-width:880px;margin:30px auto 0;font-family:var(--sans);font-size:11.5px;color:var(--muted);border:1px dashed var(--line);border-radius:11px;padding:13px 18px;line-height:1.85}} .selfdoc b{{color:var(--gold-light)}}
footer{{margin-top:50px;text-align:center;color:var(--faint);font-family:var(--sans);font-size:11.5px;line-height:1.95;border-top:1px solid var(--line2);padding-top:26px}} footer a{{color:var(--muted);text-decoration:none;border-bottom:1px solid var(--line2)}}
footer .q{{font-family:var(--serif);color:var(--gold);font-size:15px;margin-bottom:12px}}
@media(max-width:720px){{.grid,.organs,.cols3,.future{{grid-template-columns:1fr}}}}
</style></head><body>
<header>
  <div class="kick">{e(M["en"])}</div>
  <h1 class="foil">{e(M["title"])}</h1>
  <div class="tag">{e(M["tagline"])}</div>
  <div class="ax"><b>{e(M["axiom_name"])}</b> · {e(M["axiom_def"])}</div>
  <div class="kpis"><span class="kpi"><b>{len(BOOKS)}</b> 书</span><span class="kpi"><b>{TOT_CH}</b> 章</span><span class="kpi"><b>{TOT_SEC}</b> 节</span><span class="kpi"><b>{TOT_SUB}</b> 目</span><span class="kpi"><b>4</b> 脊骨</span><span class="kpi live">正文 <b>{TOT_W}/{TOT_CH}</b> 章 · {TOT_PIECES} 篇成稿</span></div>
</header>
<nav><div class="nin">
  <a href="#overview">统观</a><a href="#books">三本书</a><a href="#pipeline">写作产线</a><a href="#systems">元AI 四套</a><a href="#roadmap">进度 · 路线图</a>
  <a href="{e(M["github"])}" target="_blank">GitHub ↗</a>
</div></nav>
<div class="wrap">

  <div class="sl" id="overview"><span class="rn">Ⅰ</span><span class="n">统观 · 一眼看全</span><span class="ln"></span><span class="hint">先看全局，再钻细节</span></div>
  <div class="grid">{ov_cards}</div>

  <div class="sl" id="books"><span class="rn">Ⅱ</span><span class="n">三本书 · 逐本深入</span><span class="ln"></span><span class="hint">书 → 章 → 节 → 目（递归脊柱）· 进度自动追踪</span></div>
  {books_html}

  <div class="sl" id="pipeline"><span class="rn">Ⅲ</span><span class="n">写作产线 · 怎么写出来的</span><span class="ln"></span><span class="hint">方法论 + 自进化复盘</span></div>
  <div class="grid">{pl_cards}</div>
  {f'<div class="htrack"><div style="font-family:var(--sans);font-size:11px;color:var(--faint);margin-bottom:7px">复盘轨迹（FTF 三维 · 越写越准）</div>{htrack}</div>' if htrack else ''}

  <div class="sl" id="systems"><span class="rn">Ⅳ</span><span class="n">元AI 四套 · 通往哪</span><span class="ln"></span><span class="hint">四部转出来的四交付物 = 四个正在跑的真实系统</span></div>
  <div class="organs">{organs}</div>
  {f'<div class="flow"><b>数据流</b> · {e(dv.get("flow",""))}</div>' if dv.get("flow") else ''}
  {f'<div class="lastmile">{e(dv.get("last_mile",""))}</div>' if dv.get("last_mile") else ''}

  <div class="sl" id="roadmap"><span class="rn">Ⅴ</span><span class="n">飞轮 · 进度 & 路线图</span><span class="ln"></span><span class="hint">写一章长一块（自繁殖）</span></div>
  <div class="cols3">
    <div class="rmcard rm-now"><h4>✅ 现在（已落地）</h4><ul>{rlist(RM.get("now",[]))}</ul></div>
    <div class="rmcard rm-near"><h4>🚧 近期（在做）</h4><ul>{rlist(RM.get("near",[]))}</ul></div>
    <div class="rmcard rm-far"><h4>🔮 远期（在望）</h4><ul>{rlist(RM.get("far",[]))}</ul></div>
  </div>
  <div style="font-family:var(--sans);font-size:12px;color:var(--muted);margin:16px 0 8px">🔮 未来书（不开坑·观察后定）</div>
  <div class="future">{future}</div>

  <div class="selfdoc"><b>这个门户的结构本身满足 究竟/完备/递进/具体/递归：</b>
    <b>究竟</b>＝一根公理 ʸx，门户是它的前门，每区都是它的展开；
    <b>完备</b>＝{len(linked)} 个存量页每页有家（构建脚本自动审计孤儿）+ 每个增量槽（604目正文/复盘/元AI四套/未来书）都预留；
    <b>递进</b>＝顶→地→生长六层（北极星→统观→三本书→产线→系统→飞轮）；
    <b>具体</b>＝每入口都是可点页 + 状态徽章 + 一句「何时点进来」；
    <b>递归</b>＝三本书区自相似于 书→章→节→目，门户＝「一纸文脉」器官在渲染自己。
    判断/渲染分离：portal-map.json + roadmap.json + 三本 outline JSON → build_portal.py（每写一章重跑即长）。</div>

  <footer>
    <div class="q">{e(OUTLINE["axiom"]["subject"])}</div>
    <div>原力战略三部曲 · 门户（数据驱动·活的）· 墨绿鎏金 · <a href="{e(M["github"])}" target="_blank">moonstachain/yuanli-strategy-trilogy</a></div>
  </footer>
</div></body></html>'''

(HERE / "index.html").write_text(HTML, encoding="utf-8")
print(f"wrote index.html | {len(BOOKS)}书/{TOT_CH}章/{TOT_SEC}节/{TOT_SUB}目 · 正文 {TOT_W}/{TOT_CH}章 {TOT_PIECES}篇 · 元AI {len(dv.get('organs',[]))}套 · 复盘 {len(HISTORY)}篇")

# ---------- 全站统一导航（收尾·防重渲孤岛）----------
try:
    import apply_nav; apply_nav.run()
except Exception as _ex:
    print("apply_nav 跳过：", _ex)

# ---------- 孤儿审计 ----------
all_html = {str(p.relative_to(HERE)) for p in HERE.rglob("*.html") if ".git" not in p.parts}
all_html.discard("index.html")
orphans = sorted(all_html - linked)
if orphans:
    print(f"⚠️  孤儿页（未被门户收录）{len(orphans)}：")
    for o in orphans: print("   -", o)
    sys.exit(0)
else:
    print(f"✅ 孤儿审计 PASS · 仓内 {len(all_html)} 个内容页全部收录（0 未收）")
