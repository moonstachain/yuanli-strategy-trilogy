#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""原力战略三部曲·提纲架构图 渲染层（判断/渲染分离）。
读 _atlas/outline.json → 写 原力三部曲-提纲架构.html（qishi 墨绿鎏金）。改数据重跑即更新。"""
import json, html, pathlib
HERE = pathlib.Path(__file__).parent
D = json.load(open(HERE/"_atlas"/"outline.json", encoding="utf-8"))
def e(s): return html.escape(str(s)) if s is not None else ""
total_sec = sum(len(c["sections"]) for b in D["books"] for c in b["chapters"])
total_ch = sum(len(b["chapters"]) for b in D["books"])
BC = {"原力资产": "#c9a961", "原力创业": "#cdab63", "原力OS": "#9a7d3e"}

def macro_band():
    out = ""
    for i, m in enumerate(D["macro"]):
        if i: out += '<div class="m-arrow">▸</div>'
        out += f'<div class="m-node"><div class="m-seq">{m["seq"]}</div><div class="m-n">{e(m["node"])}</div><div class="m-t">{e(m["tier"])}</div><div class="m-w">{e(m["why"])}</div></div>'
    return out

def book_block(b, idx):
    color = BC.get(b["name"], "#c9a961"); seal = ["内", "外", "上"][idx]
    chs = ""
    for c in b["chapters"]:
        secs = "".join(f'<span class="sec">{e(s)}</span>' for s in c["sections"])
        done = '<span class="done">已写</span>' if c.get("done") else ''
        absorb = f'<div class="absorb">{e(c["absorb"])}</div>' if c.get("absorb") else ''
        chs += f'''<div class="ch" style="--c:{color}">
      <div class="ch-h"><span class="ch-seq">{c["seq"]}</span><span class="ch-n">{e(c["name"])}</span>
        <span class="ch-ly">{e(c["layer"])}</span>{done}<span class="ch-cnt">{len(c["sections"])} 节</span></div>
      <div class="ch-q">第一性问题 · {e(c["q"])}</div>{absorb}
      <div class="secs">{secs}</div></div>'''
    gc = f'<div class="gc">{e(b.get("guanchuan",""))}</div>' if b.get("guanchuan") else ''
    nsec = sum(len(c["sections"]) for c in b["chapters"])
    return f'''<section class="book" style="--c:{color}">
  <div class="bk-h"><span class="seal">{seal}</span><div><div class="bk-n">《{e(b["name"])}》</div>
    <div class="bk-meta">{e(b["axis"])} · 模型＝{e(b["model"])} · {e(b["scale"])}</div>
    <div class="bk-q">{e(b["question"])}</div></div><div class="bk-cnt">{len(b["chapters"])} 章<br/>{nsec} 节</div></div>{gc}
  <div class="chs">{chs}</div></section>'''

spine = "".join(f'<div class="sp"><b>{e(s["n"])}</b> {e(s["name"])}<span>{e(s["note"])}</span></div>' for s in D["spine"])
seams = "".join(f'<div class="sm"><b>{e(s["name"])}</b> {e(s["rule"])}</div>' for s in D["seams"])
R = D["reasoning"]
reason = "".join(f'<div class="rz"><div class="rz-k">{e(k)}</div><div class="rz-v">{e(R[k])}</div></div>' for k in ["究竟","完备","递归","莫比乌斯"])

HTML = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>原力战略三部曲 · 提纲架构</title>
<style>
:root{--ink:#0a1612;--leather-deep:#0d2018;--leather:#14301f;--panel:rgba(20,48,31,.5);--panel2:rgba(28,61,41,.4);--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;--jade:#4a7c59;--cream:#f0e6d2;--cream-dim:#d3c8b0;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.2);--line2:rgba(201,169,97,.1);--serif:"Noto Serif SC","Songti SC",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}
*{box-sizing:border-box;margin:0;padding:0}
body{background:radial-gradient(1100px 640px at 82% -6%,rgba(74,124,89,.16),transparent 60%),linear-gradient(180deg,var(--ink),var(--leather-deep) 52%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:1.7;padding:0 0 70px}
.foil{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 52%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}
header{text-align:center;padding:54px 24px 18px}
.kick{font-family:var(--display);font-size:12px;letter-spacing:.44em;color:var(--gold);text-transform:uppercase;margin-bottom:16px}
h1{font-weight:600;font-size:clamp(28px,5vw,48px);letter-spacing:.1em}
.ax{margin-top:16px;font-family:var(--mono);font-size:13px;color:var(--gold-light)}.ax b{color:var(--gold-bright)}
.axd{font-family:var(--sans);font-size:12.5px;color:var(--cream-dim);margin-top:7px}
.kpis{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:14px}
.kpi{font-family:var(--mono);font-size:11.5px;color:var(--gold-light);padding:4px 10px;border-radius:5px;background:rgba(201,169,97,.06);border-left:2px solid var(--gold)}
.kpi b{color:var(--gold-bright)}
.sl{display:flex;align-items:baseline;gap:12px;margin:42px 0 14px}
.sl .n{font-family:var(--display);font-size:12px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase}
.sl .ln{flex:1;height:1px;background:var(--line)}
/* 康波通史 */
.kangbo{border:1px solid rgba(168,54,44,.35);border-left:3px solid var(--cinnabar);border-radius:12px;background:rgba(168,54,44,.06);padding:15px 20px}
.kangbo .kt{font-size:16px;color:#e0a08c;font-family:var(--serif)}.kangbo .kd{font-family:var(--sans);font-size:12.5px;color:var(--cream-dim);margin-top:5px;line-height:1.7}
.kangbo .kr{font-family:var(--sans);font-size:11.5px;color:var(--muted);margin-top:5px}.kangbo .kr b{color:#e0a08c}
/* 宏观带 */
.macro{display:flex;align-items:stretch;flex-wrap:wrap;margin-top:6px}
.m-node{flex:1 1 170px;min-width:160px;border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:12px;background:var(--panel);padding:13px 14px}
.m-seq{font-family:var(--mono);font-size:10px;color:var(--gold-deep)}.m-n{font-family:var(--serif);font-size:17px;color:var(--gold-bright);margin-top:2px}
.m-t{font-family:var(--mono);font-size:11px;color:var(--gold);margin:4px 0 8px}.m-w{font-size:11.5px;color:var(--cream-dim);line-height:1.6}
.m-arrow{flex:0 0 22px;display:flex;align-items:center;justify-content:center;color:var(--gold);font-size:16px}
/* books */
.books{display:grid;grid-template-columns:1fr;gap:20px}
.book{border:1px solid var(--line);border-left:3px solid var(--c);border-radius:14px;background:var(--panel);padding:20px 22px}
.bk-h{display:flex;align-items:flex-start;gap:14px}
.seal{font-family:var(--serif);font-size:24px;color:var(--c);width:42px;height:42px;flex:0 0 42px;display:flex;align-items:center;justify-content:center;border:1px solid var(--c);border-radius:8px;background:rgba(0,0,0,.2)}
.bk-n{font-family:var(--serif);font-size:22px;color:var(--gold-bright)}.bk-meta{font-family:var(--sans);font-size:11.5px;color:var(--muted);margin-top:2px}
.bk-q{font-size:13px;color:var(--gold-light);margin-top:6px}.bk-cnt{margin-left:auto;text-align:right;font-family:var(--mono);font-size:12px;color:var(--c);flex:0 0 auto}
.gc{font-family:var(--sans);font-size:11.5px;color:var(--muted);margin:11px 0 4px;padding:7px 13px;border-left:2px solid var(--line);background:rgba(0,0,0,.13);border-radius:0 6px 6px 0}
.chs{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:12px}
.ch{border:1px solid var(--line);border-radius:11px;background:rgba(0,0,0,.16);padding:13px 15px;border-top:2px solid var(--c)}
.ch-h{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.ch-seq{font-family:var(--serif);font-size:14px;color:var(--c);border:1px solid var(--c);border-radius:50%;width:24px;height:24px;flex:0 0 24px;display:flex;align-items:center;justify-content:center}
.ch-n{font-family:var(--serif);font-size:18px;color:var(--cream)}.ch-ly{font-family:var(--mono);font-size:10.5px;color:var(--gold)}
.done{font-size:9.5px;color:var(--jade);border:1px solid rgba(74,124,89,.5);border-radius:9px;padding:1px 6px}
.ch-cnt{margin-left:auto;font-family:var(--mono);font-size:11px;color:var(--gold-light)}
.ch-q{font-size:12px;color:var(--gold-light);margin:8px 0;line-height:1.6}
.absorb{font-size:11.5px;color:#e0a08c;background:rgba(168,54,44,.07);border-left:2px solid var(--cinnabar);border-radius:0 6px 6px 0;padding:6px 11px;margin-bottom:8px;line-height:1.6}
.secs{display:flex;gap:5px;flex-wrap:wrap}
.sec{font-family:var(--sans);font-size:11px;color:var(--cream-dim);border:1px solid var(--line2);border-radius:6px;padding:3px 8px;background:rgba(0,0,0,.12)}
/* spine/seams */
.panel{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pcol{border:1px solid var(--line);border-radius:12px;background:var(--panel2);padding:16px 18px}
.pcol h4{font-family:var(--serif);font-size:15px;color:var(--gold);margin-bottom:10px}
.sp,.sm{font-family:var(--sans);font-size:12px;color:var(--cream-dim);padding:6px 0;border-bottom:1px solid var(--line2);line-height:1.6}.sp:last-child,.sm:last-child{border:0}
.sp b,.sm b{color:var(--gold-light)}.sp span{display:block;font-size:10.5px;color:var(--muted);margin-top:1px}
.wealth{margin-top:16px;font-family:var(--sans);font-size:12.5px;color:var(--cream-dim);border:1px dashed rgba(201,169,97,.4);border-radius:10px;padding:12px 16px;line-height:1.75}.wealth b{color:var(--gold-light)}
/* reasoning */
.reason{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.rz{border:1px solid var(--line);border-top:3px solid var(--gold);border-radius:12px;background:var(--panel);padding:16px 18px}
.rz-k{font-family:var(--serif);font-size:18px;color:var(--gold-bright);margin-bottom:7px}
.rz-v{font-size:12.5px;color:var(--cream-dim);line-height:1.8}
footer{text-align:center;margin-top:46px;color:var(--faint);font-family:var(--sans);font-size:11.5px;line-height:1.9}footer a{color:var(--muted)}
@media(max-width:760px){.chs,.panel,.reason{grid-template-columns:1fr}.m-node{flex-basis:100%}}
</style></head><body>
<header>
  <div class="kick">YUANLI STRATEGY TRILOGY · OUTLINE</div>
  <h1 class="foil">原力战略三部曲 · 提纲架构</h1>
  <div class="ax"><b>__AXIOM__</b></div><div class="axd">__SUBJECT__</div>
  <div class="kpis"><span class="kpi"><b>3</b> 本</span><span class="kpi"><b>__CH__</b> 章</span><span class="kpi"><b>__SEC__</b> 节</span><span class="kpi">究竟完备 · 递归 ✓</span></div>
</header>
<div class="wrap">
  <div class="sl"><span class="n">康波通史 · 前置</span><span class="ln"></span></div>
  <div class="kangbo"><div class="kt">__KT__</div><div class="kd">__KD__</div><div class="kr"><b>定位</b> __KR__</div></div>
  <div class="sl"><span class="n">宏观推导带 · 公理长出三本书</span><span class="ln"></span></div>
  <div class="macro">__MACRO__</div>
  <div class="sl"><span class="n">三本书 · __CH__ 章 __SEC__ 节</span><span class="ln"></span></div>
  <div class="books">__BOOKS__</div>
  <div class="sl"><span class="n">脊骨贯穿 · 去重三缝</span><span class="ln"></span></div>
  <div class="panel"><div class="pcol"><h4>4 根脊骨（故意穿三本）</h4>__SPINE__</div><div class="pcol"><h4>去重三缝（MECE 隔离）</h4>__SEAMS__</div></div>
  <div class="wealth">__WEALTH__</div>
  <div class="sl"><span class="n">为什么这样设计 · 究竟完备 / 递归</span><span class="ln"></span></div>
  <div class="reason">__REASON__</div>
  <footer>原力战略三部曲 · 提纲架构图 · 判断/渲染分离（outline.json + build_outline.py）· <a href="https://github.com/moonstachain/yuanli-strategy-trilogy">github.com/moonstachain/yuanli-strategy-trilogy</a> · 写三本绿皮书的章节真源</footer>
</div></body></html>'''

out = (HTML.replace("__AXIOM__", e(D["axiom"]["name"]) + " ＝ " + e(D["axiom"]["def"]))
           .replace("__SUBJECT__", e(D["axiom"]["subject"]))
           .replace("__CH__", str(total_ch)).replace("__SEC__", str(total_sec))
           .replace("__KT__", e(D["kangbo"]["title"])).replace("__KD__", e(D["kangbo"]["def"])).replace("__KR__", e(D["kangbo"]["role"]))
           .replace("__MACRO__", macro_band())
           .replace("__BOOKS__", "".join(book_block(b, i) for i, b in enumerate(D["books"])))
           .replace("__SPINE__", spine).replace("__SEAMS__", seams)
           .replace("__WEALTH__", "<b>财富的家：</b>" + e(D["wealth_note"]))
           .replace("__REASON__", reason))
(HERE/"原力三部曲-提纲架构.html").write_text(out, encoding="utf-8")
print(f"wrote 原力三部曲-提纲架构.html | books=3 chapters={total_ch} sections={total_sec}")
