#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲《原力战略三部曲·总纲》一体化母页（公理→3书→14章→138节→604目 + 脊骨穿透矩阵）。
读 _atlas/trilogy-master-outline.json → 墨绿鎏金交互 HTML + 同源 MD。判断/渲染分离。"""
import json, html, pathlib
HERE = pathlib.Path(__file__).parent
D = json.load(open(HERE / "_atlas" / "trilogy-master-outline.json", encoding="utf-8"))
def e(s): return html.escape(str(s)) if s is not None else ""
CN = "〇一二三四五六七八九十"
def cn(n): return CN[n] if n < 11 else str(n)

# (book, section) -> [(spine_id, spine_name, role)]
sec2spine = {}
for sp in D["weave"]:
    for t in sp["threads"]:
        sec2spine.setdefault((t["book"], t["section"]), []).append((sp["id"], sp["name"], t["role"]))

SPINE_COLORS = {"s1": "#c9a961", "s2": "#5a9c6e", "s3": "#c06a5e", "s4": "#b08d57"}

def sub_row(s, i):
    why = e(s.get("why", "")); first = why.startswith("起点") or why.startswith("起 点")
    wcls = "why first" if first else "why"; wtxt = "▸ 起点" if first else f"因为 {why}"
    return f'''<div class="sub"><div class="sub-n"><span class="sx">{i:02d}</span>{e(s.get("name"))}</div>
  <div class="sub-p">{e(s.get("point"))}</div>
  <div class="sub-meta"><span class="{wcls}">{wtxt}</span><span class="canon">📎 {e(s.get("canon"))}</span></div></div>'''

def sec_block(sec, bn, ci, si):
    sp = sec2spine.get((bn, sec["name"]), [])
    dsp = " ".join(x[0] for x in sp)
    badges = "".join(f'<span class="sbadge" style="--sc:{SPINE_COLORS.get(x[0],"#c9a961")}" title="{e(x[1])}：{e(x[2])}">脊骨{x[0][1]}</span>' for x in sp)
    subs = "".join(sub_row(s, k + 1) for k, s in enumerate(sec.get("subs", [])))
    cls = "sec sp" if sp else "sec"
    return f'''<div class="{cls}" data-spine="{dsp}">
  <div class="sec-h"><span class="sec-no">{ci}.{si}</span><span class="sec-n">{e(sec.get("name"))}</span>{badges}
    <span class="sec-c">{len(sec.get("subs", []))} 目</span></div>
  <div class="sec-q">{e(sec.get("q", ""))}</div>
  <div class="subs">{subs}</div></div>'''

def ch_block(b, c):
    secs = "".join(sec_block(s, b["name"], c["seq"], i + 1) for i, s in enumerate(c["sections"]))
    return f'''<details class="ch">
  <summary><span class="seal">{cn(c["seq"])}</span><span class="ch-main"><span class="ch-n">{e(c.get("title") or ("第"+cn(c["seq"])+"章"))} · {e(c["name"])}</span>
    <span class="ch-layer">{e(c.get("layer",""))}</span></span><span class="ch-c">{len(c["sections"])} 节 · {sum(len(s["subs"]) for s in c["sections"])} 目</span><span class="chev">▾</span></summary>
  <div class="ch-body">{secs}</div></details>'''

def book_block(b):
    chs = "".join(ch_block(b, c) for c in b["chapters"])
    S = b["stats"]
    return f'''<details class="book" id="book{b['seq']}">
  <summary class="bk-sum"><span class="bk-seal">{cn(b['seq'])}</span><span class="bk-main">
    <span class="bk-n">《{e(b['name'])}》<span class="bk-axis">{e(b['axis'])} · {e(b['scale'])}</span></span>
    <span class="bk-model">模型＝{e(b['model'])} · {e(b.get('arc',''))[:46]}…</span></span>
    <span class="bk-c">{S.get('chapters','')} 章 · {S.get('sections','')} 节 · <b>{S.get('subs','')}</b> 目</span><span class="chev">▾</span></summary>
  <div class="bk-body">{chs}</div></details>'''

# 脊骨 chips + thread panels
chips = "".join(
    f'<button class="spine-chip" data-spine="{sp["id"]}" style="--sc:{SPINE_COLORS.get(sp["id"],"#c9a961")}" onclick="litSpine(\'{sp["id"]}\')">'
    f'<b>{e(sp["spine"])}</b> {e(sp["name"])} <span class="chip-c">{len(sp["threads"])}节·{len(set(t["book"] for t in sp["threads"]))}本</span></button>'
    for sp in D["weave"])
panels = ""
for sp in D["weave"]:
    rows = "".join(f'<div class="th"><span class="th-b">{e(t["book"])}</span><span class="th-s">{e(t["section"])}</span><span class="th-r">{e(t["role"])}</span></div>' for t in sp["threads"])
    panels += f'<div class="wpanel" id="wp-{sp["id"]}" style="--sc:{SPINE_COLORS.get(sp["id"],"#c9a961")}"><div class="wp-h">{e(sp["spine"])} · {e(sp["name"])} <span class="wp-note">{e(sp.get("note",""))}</span></div>{rows}</div>'

macro = "".join(
    f'<div class="ring"><div class="ring-n">{e(m["node"])}</div><div class="ring-t">{e(m["tier"])}</div><div class="ring-w">{e(m["why"])}</div></div>'
    + ('<div class="ar">→</div>' if i < len(D["macro"]) - 1 else '')
    for i, m in enumerate(D["macro"]))

SVG = {
 "U": '<svg viewBox="0 0 80 60"><path d="M16 8 V30 Q16 48 40 48 Q64 48 64 30 V8" fill="none" stroke="var(--gold)" stroke-width="2.5"/><circle cx="40" cy="48" r="3" fill="var(--cinnabar)"/></svg>',
 "chasm": '<svg viewBox="0 0 80 60"><rect x="8" y="30" width="22" height="6" fill="var(--gold)"/><rect x="50" y="30" width="22" height="6" fill="var(--gold)"/><path d="M30 33 Q40 12 50 33" fill="none" stroke="var(--cinnabar)" stroke-width="2" stroke-dasharray="3 3"/></svg>',
 "mobius": '<svg viewBox="0 0 80 60"><path d="M24 30 C24 16 56 16 56 30 C56 44 24 44 24 30 Z" fill="none" stroke="var(--gold)" stroke-width="2.5"/><path d="M40 22 L40 38" stroke="var(--gold-bright)" stroke-width="2"/><text x="40" y="58" text-anchor="middle" fill="var(--gold-light)" font-size="9">∞</text></svg>',
}
shapes = "".join(
    f'<div class="shape"><div class="shp-svg">{SVG.get(it["glyph"],"")}</div><div class="shp-n">{e(it["shape"])}</div>'
    f'<div class="shp-lv">《{e(it["book"])}》· {e(it["model"])} · {e(it["level"])}</div><div class="shp-d">{e(it["desc"])}</div></div>'
    for it in D["shapes"]["items"])

R = D["reasoning"]
seams = "".join(f'<div class="seam"><b>{e(s["name"])}</b> {e(s["rule"])}</div>' for s in D["seams"])
spine_list = "".join(f'<div class="sp-row" style="--sc:{SPINE_COLORS.get("s"+str(i+1),"#c9a961")}"><b>{e(s["n"])}</b> {e(s["name"])}<span class="sp-note">{e(s["note"])}</span></div>' for i, s in enumerate(D["spine"]))
S = D["stats"]

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>原力战略三部曲 · 总纲（一体化四级大纲）</title>
<style>
:root{{--ink:#0a1612;--leather-deep:#0d2018;--panel:rgba(20,48,31,.5);--panel2:rgba(28,61,41,.36);
--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;
--jade:#5a9c6e;--cream:#f0e6d2;--cream-dim:#d3c8b0;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.2);--line2:rgba(201,169,97,.1);
--serif:"Noto Serif SC","Songti SC",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:radial-gradient(1200px 700px at 80% -10%,rgba(74,124,89,.16),transparent 60%),radial-gradient(900px 600px at 5% 105%,rgba(201,169,97,.07),transparent 55%),linear-gradient(180deg,var(--ink),var(--leather-deep) 50%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:1.75;padding:0 0 80px}}
.foil{{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 52%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.wrap{{max-width:1060px;margin:0 auto;padding:0 24px}}
header{{text-align:center;padding:58px 24px 22px}}
.kick{{font-family:var(--display);font-size:11px;letter-spacing:.46em;color:var(--gold);text-transform:uppercase;margin-bottom:15px}}
h1{{font-weight:600;font-size:clamp(30px,5.4vw,52px);letter-spacing:.12em}}
.sub-t{{color:var(--gold-light);font-size:14.5px;margin-top:12px;letter-spacing:.04em}}
.ax{{margin:18px auto 0;max-width:680px;font-family:var(--mono);font-size:13px;color:var(--cream-dim);border:1px solid var(--line);border-radius:12px;padding:13px 18px;background:var(--panel2)}}
.ax b{{color:var(--gold-bright)}} .ax .jj{{display:block;margin-top:7px;font-family:var(--sans);font-size:11.5px;color:var(--muted);line-height:1.7}}
.kpis{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:16px}}
.kpi{{font-family:var(--mono);font-size:12px;color:var(--gold-light);padding:5px 13px;border-radius:6px;background:rgba(201,169,97,.06);border-left:2px solid var(--gold)}}
.kpi b{{color:var(--gold-bright);font-size:15px}}
.sl{{display:flex;align-items:center;gap:12px;margin:42px 0 16px}}
.sl .n{{font-family:var(--display);font-size:12px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase}}
.sl .ln{{flex:1;height:1px;background:var(--line)}} .sl .hint{{font-family:var(--sans);font-size:11px;color:var(--faint)}}
/* macro band */
.macro{{display:flex;align-items:stretch;gap:6px;flex-wrap:wrap;justify-content:center}}
.ring{{flex:1;min-width:150px;border:1px solid var(--line);border-top:2px solid var(--gold);border-radius:11px;background:var(--panel);padding:12px 13px}}
.ring-n{{font-family:var(--serif);font-size:16px;color:var(--gold-bright)}} .ring-t{{font-family:var(--mono);font-size:10px;color:var(--cinnabar-soft);margin:3px 0 6px}}
.ring-w{{font-family:var(--sans);font-size:11px;color:var(--cream-dim);line-height:1.6}}
.ar{{display:flex;align-items:center;color:var(--gold-deep);font-size:18px}}
/* spine weave matrix */
.weave-wrap{{border:1px solid var(--line);border-radius:14px;background:var(--panel2);padding:18px 20px}}
.chips{{display:flex;gap:9px;flex-wrap:wrap}}
.spine-chip{{cursor:pointer;font-family:var(--serif);font-size:13.5px;color:var(--cream);background:rgba(0,0,0,.2);border:1px solid var(--sc);border-left:3px solid var(--sc);border-radius:9px;padding:8px 13px;transition:.15s}}
.spine-chip:hover{{background:rgba(201,169,97,.08)}} .spine-chip.on{{background:var(--sc);color:var(--ink)}} .spine-chip b{{color:var(--sc)}} .spine-chip.on b{{color:var(--ink)}}
.spine-chip .chip-c{{font-family:var(--mono);font-size:10px;opacity:.8}}
.wpanels{{margin-top:14px}} .wpanel{{display:none;border-left:3px solid var(--sc);padding:4px 0 4px 14px}} .wpanel.show{{display:block}}
.wp-h{{font-family:var(--serif);font-size:14.5px;color:var(--gold-bright);margin-bottom:9px}} .wp-note{{font-family:var(--sans);font-size:11px;color:var(--muted)}}
.th{{display:flex;gap:11px;align-items:baseline;padding:5px 0;border-bottom:1px solid var(--line2);font-size:13px}}
.th-b{{font-family:var(--mono);font-size:10.5px;color:var(--sc);min-width:64px}} .th-s{{font-family:var(--serif);color:var(--gold-light);min-width:150px}} .th-r{{font-family:var(--sans);font-size:11.5px;color:var(--cream-dim)}}
.wclear{{cursor:pointer;font-family:var(--sans);font-size:11px;color:var(--faint);background:none;border:1px solid var(--line);border-radius:6px;padding:4px 10px;margin-left:8px}}
/* books / chapters / sections / 目 */
.book{{margin-top:13px;border:1px solid var(--line);border-radius:14px;background:var(--panel);overflow:hidden}}
.book[open]{{border-color:var(--gold-deep)}}
summary{{list-style:none;cursor:pointer}} summary::-webkit-details-marker{{display:none}}
.bk-sum{{display:flex;align-items:center;gap:14px;padding:17px 20px}} .bk-sum:hover{{background:rgba(201,169,97,.05)}}
.bk-seal{{font-family:var(--serif);font-size:19px;color:var(--gold-bright);width:42px;height:42px;flex:none;display:flex;align-items:center;justify-content:center;border:1px solid var(--gold);border-radius:50%}}
.bk-main{{flex:1;min-width:0}} .bk-n{{font-family:var(--serif);font-size:21px;color:var(--gold-bright)}} .bk-axis{{font-family:var(--mono);font-size:10.5px;color:var(--cinnabar-soft);margin-left:9px}}
.bk-model{{display:block;font-family:var(--sans);font-size:11.5px;color:var(--muted);margin-top:4px}} .bk-c{{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap}} .bk-c b{{color:var(--gold-bright)}}
.bk-body{{padding:2px 18px 16px;border-top:1px solid var(--line2)}}
.ch{{margin-top:10px;border:1px solid var(--line2);border-radius:10px;background:rgba(0,0,0,.13);overflow:hidden}}
.ch>summary{{display:flex;align-items:center;gap:12px;padding:12px 15px}} .ch>summary:hover{{background:rgba(201,169,97,.04)}}
.seal{{font-family:var(--serif);font-size:14px;color:var(--gold-light);width:30px;height:30px;flex:none;display:flex;align-items:center;justify-content:center;border:1px solid var(--gold-deep);border-radius:50%}}
.ch-main{{flex:1;min-width:0}} .ch-n{{font-family:var(--serif);font-size:16px;color:var(--gold-bright)}} .ch-layer{{font-family:var(--mono);font-size:10px;color:var(--cinnabar-soft);margin-left:8px}}
.ch-c{{font-family:var(--mono);font-size:10px;color:var(--gold)}} .chev{{color:var(--gold-deep);font-size:12px;transition:.2s}} details[open]>summary .chev{{transform:rotate(180deg)}}
.ch-body{{padding:2px 16px 14px}}
.sec{{margin-top:13px;padding-left:14px;border-left:2px solid var(--gold-deep);transition:.2s}}
.sec.lit{{border-left-color:var(--gold-bright);background:rgba(201,169,97,.08);box-shadow:-3px 0 0 0 var(--gold);border-radius:0 8px 8px 0}}
.sec-h{{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap}} .sec-no{{font-family:var(--mono);font-size:11px;color:var(--gold-deep)}} .sec-n{{font-family:var(--serif);font-size:15.5px;color:var(--gold-light)}}
.sbadge{{font-family:var(--sans);font-size:9px;color:var(--sc);border:1px solid var(--sc);border-radius:8px;padding:0 6px}} .sec-c{{font-family:var(--mono);font-size:10px;color:var(--faint);margin-left:auto}}
.sec-q{{font-family:var(--sans);font-size:11px;color:var(--muted);margin:3px 0 9px;line-height:1.6}}
.subs{{display:flex;flex-direction:column;gap:6px}} .sub{{padding:8px 12px;border-radius:8px;background:rgba(0,0,0,.17);border-left:2px solid var(--line)}}
.sub-n{{font-family:var(--serif);font-size:13.5px;color:var(--cream);display:flex;gap:8px}} .sx{{font-family:var(--mono);font-size:9.5px;color:var(--gold-deep)}}
.sub-p{{font-family:var(--sans);font-size:12px;color:var(--cream-dim);margin:2px 0 4px;padding-left:25px;line-height:1.55}}
.sub-meta{{display:flex;gap:11px;flex-wrap:wrap;padding-left:25px}} .why{{font-family:var(--sans);font-size:10px;color:var(--jade)}} .why.first{{color:var(--gold);font-weight:600}} .canon{{font-family:var(--mono);font-size:9px;color:var(--faint)}}
/* shapes */
.shapes{{display:grid;grid-template-columns:repeat(3,1fr);gap:13px}}
.shape{{border:1px solid var(--line);border-radius:12px;background:var(--panel);padding:15px;text-align:center}}
.shp-svg svg{{width:80px;height:60px}} .shp-n{{font-family:var(--serif);font-size:15px;color:var(--gold-bright);margin-top:6px}}
.shp-lv{{font-family:var(--mono);font-size:10px;color:var(--cinnabar-soft);margin:4px 0 7px}} .shp-d{{font-family:var(--sans);font-size:11.5px;color:var(--cream-dim);line-height:1.65}}
.synth{{margin-top:13px;text-align:center;font-family:var(--sans);font-size:12.5px;color:var(--gold-light);border:1px dashed var(--line);border-radius:10px;padding:11px 16px;line-height:1.8}}
/* reasoning / spine list / seams */
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:13px}}
.panel{{border:1px solid var(--line);border-radius:12px;background:var(--panel2);padding:15px 18px}}
.panel h3{{font-family:var(--serif);font-size:15px;color:var(--gold-bright);margin-bottom:10px;font-weight:600}}
.sp-row{{font-size:12.5px;color:var(--cream-dim);padding:6px 0;border-bottom:1px solid var(--line2);border-left:2px solid var(--sc);padding-left:10px;margin-bottom:4px;line-height:1.6}} .sp-row b{{color:var(--sc)}} .sp-note{{display:block;font-family:var(--sans);font-size:10.5px;color:var(--muted)}}
.seam{{font-family:var(--sans);font-size:11.5px;color:var(--cream-dim);padding:5px 0;line-height:1.6}} .seam b{{color:var(--gold-light)}}
.rz{{margin-bottom:11px}} .rz-k{{font-family:var(--serif);font-size:13.5px;color:var(--gold-light)}} .rz-v{{font-family:var(--sans);font-size:12px;color:var(--cream-dim);line-height:1.7;margin-top:2px}}
.wealth{{font-family:var(--sans);font-size:11.5px;color:var(--muted);border-left:2px solid var(--cinnabar);padding:7px 13px;background:rgba(168,54,44,.05);border-radius:0 8px 8px 0;line-height:1.7;margin-top:10px}}
footer{{margin-top:46px;text-align:center;color:var(--faint);font-family:var(--sans);font-size:11px;line-height:1.95;border-top:1px solid var(--line2);padding-top:24px}}
footer a{{color:var(--muted);text-decoration:none;border-bottom:1px solid var(--line2)}}
@media(max-width:720px){{.shapes,.cols{{grid-template-columns:1fr}}.ar{{display:none}}.th-s{{min-width:0}}}}
</style></head><body>
<header>
  <div class="kick">YUANLI STRATEGY TRILOGY · MASTER OUTLINE</div>
  <h1 class="foil">原力战略三部曲 · 总纲</h1>
  <div class="sub-t">{e(D["subtitle"])}</div>
  <div class="ax">公理 <b>{e(D["axiom"]["name"])}</b> · {e(D["axiom"]["def"])}<br/><b>{e(D["axiom"]["subject"])}</b>
    <span class="jj">究竟：{e(R["究竟"])}</span></div>
  <div class="kpis"><span class="kpi"><b>{S["books"]}</b> 书</span><span class="kpi"><b>{S["chapters"]}</b> 章</span><span class="kpi"><b>{S["sections"]}</b> 节</span><span class="kpi"><b>{S["subs"]}</b> 目</span><span class="kpi"><b>4</b> 脊骨穿三部</span></div>
</header>
<div class="wrap">
  <div class="sl"><span class="n">宏观推导带</span><span class="ln"></span><span class="hint">一公理如何展成三本 + 飞轮回流</span></div>
  <div class="macro">{macro}</div>

  <div class="sl"><span class="n">脊骨穿透矩阵</span><span class="ln"></span><span class="hint">点一个脊骨 → 高亮它穿过三本书的所有节（这就是「三本其实是一本」）</span></div>
  <div class="weave-wrap">
    <div class="chips">{chips}<button class="wclear" onclick="litClear()">清除高亮</button></div>
    <div class="wpanels">{panels}</div>
  </div>

  <div class="sl"><span class="n">三本书 · 全展到目（604）</span><span class="ln"></span><span class="hint">点书名展开 → 章 → 节 → 目</span></div>
  {"".join(book_block(b) for b in D["books"])}

  <div class="sl"><span class="n">三形状 · 同一条 ʸx 螺旋</span><span class="ln"></span></div>
  <div class="shapes">{shapes}</div>
  <div class="synth">{e(D["shapes"]["synthesis"])}</div>

  <div class="sl"><span class="n">四脊骨 · 三缝 · 究竟完备</span><span class="ln"></span></div>
  <div class="cols">
    <div class="panel"><h3>四脊骨（故意穿三部）+ 主根</h3>{spine_list}
      <div class="wealth"><b>主根：</b>{e(D["main_root"]["note"])}</div></div>
    <div class="panel"><h3>三缝（防双归）+ 财富折入</h3>{seams}<div class="wealth">{e(D["wealth_note"])}</div></div>
  </div>
  <div class="panel" style="margin-top:13px">
    <h3>为什么恰好三本 · 究竟 / 完备 / 递归 / 同构 / 书造自己 / 莫比乌斯</h3>
    {"".join(f'<div class="rz"><div class="rz-k">{e(k)}</div><div class="rz-v">{e(R[k])}</div></div>' for k in R)}
  </div>

  <footer>
    <div>原力战略三部曲 · 总纲（一体化四级大纲）· 判断/渲染分离（trilogy-master-outline.json + build_master_outline.py）· 墨绿鎏金</div>
    <div style="margin-top:8px"><a href="../index.html">← 三部曲门户</a> · 深读：<a href="原力资产-四级目录.html">资产</a> · <a href="原力创业-四级目录.html">创业</a> · <a href="原力OS-四级目录.html">OS</a> · <a href="原力三部曲-提纲架构.html">提纲架构</a> · <a href="原力三部曲-概念地图.html">概念地图</a></div>
  </footer>
</div>
<script>
function litClear(){{
  document.querySelectorAll('.sec.lit').forEach(x=>x.classList.remove('lit'));
  document.querySelectorAll('.spine-chip.on').forEach(x=>x.classList.remove('on'));
  document.querySelectorAll('.wpanel.show').forEach(x=>x.classList.remove('show'));
}}
function litSpine(id){{
  var chip=document.querySelector('.spine-chip[data-spine="'+id+'"]');
  var already=chip.classList.contains('on');
  litClear();
  if(already) return;
  chip.classList.add('on');
  var p=document.getElementById('wp-'+id); if(p) p.classList.add('show');
  var first=null;
  document.querySelectorAll('.sec[data-spine~="'+id+'"]').forEach(function(sec){{
    sec.classList.add('lit');
    var d=sec.closest('details.ch'); if(d) d.open=true;
    var b=sec.closest('details.book'); if(b) b.open=true;
    if(!first) first=sec;
  }});
  if(first) first.scrollIntoView({{behavior:'smooth',block:'center'}});
}}
</script>
</body></html>'''
OUT = HERE / "原力战略三部曲-总纲.html"
OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT.name} | {S['books']}书/{S['chapters']}章/{S['sections']}节/{S['subs']}目 · weave {len(D['weave'])}脊骨")

# 同源 MD
md = [f"# 原力战略三部曲 · 总纲（一体化四级大纲）\n",
      f"> {D['subtitle']}  ",
      f"> 公理 **{D['axiom']['name']}** · {D['axiom']['def']}　**{D['axiom']['subject']}**  ",
      f"> 究竟：{R['究竟']}\n", "## 宏观推导带\n"]
md.append(" → ".join(f"**{m['node']}**（{m['tier']}）" for m in D["macro"]))
md.append("\n" + "\n".join(f"- **{m['node']}**（{m['tier']}）：{m['why']}" for m in D["macro"]) + "\n")
md.append("## 脊骨穿透矩阵（让三本成为一本）\n")
for sp in D["weave"]:
    md.append(f"### {sp['spine']} · {sp['name']}　〔{sp.get('note','')}〕")
    for t in sp["threads"]:
        md.append(f"- 《{t['book']}》{t['section']} —— {t['role']}")
    md.append("")
md.append("## 三形状 · 同一条 ʸx 螺旋\n")
for it in D["shapes"]["items"]:
    md.append(f"- **{it['shape']}** ·《{it['book']}》{it['model']}（{it['level']}）—— {it['desc']}")
md.append(f"\n> {D['shapes']['synthesis']}\n")
md.append("## 四脊骨 + 主根\n" + "\n".join(f"- **{s['n']} {s['name']}** —— {s['note']}" for s in D["spine"]))
md.append(f"- **主根** —— {D['main_root']['note']}\n")
md.append("## 三缝（防双归）\n" + "\n".join(f"- **{s['name']}** —— {s['rule']}" for s in D["seams"]))
md.append(f"\n> {D['wealth_note']}\n")
md.append("## 为什么恰好三本\n" + "\n".join(f"- **{k}**：{R[k]}" for k in R))
md.append(f"\n---\n*总纲＝写整套三部曲正文的总真源。{S['books']} 书 / {S['chapters']} 章 / {S['sections']} 节 / {S['subs']} 目，4 脊骨穿三部。*")
(HERE / "原力战略三部曲-总纲.md").write_text("\n".join(md), encoding="utf-8")
print("wrote 原力战略三部曲-总纲.md")
