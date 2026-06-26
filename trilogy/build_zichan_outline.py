#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲《原力资产》四级目录（书→章→节→目）→ 原力资产-四级目录.html。
判断/渲染分离：读 _atlas/zichan-outline.json（数据）拼墨绿鎏金 HTML。改数据重跑即更新。"""
import json, html, pathlib
HERE = pathlib.Path(__file__).parent
D = json.load(open(HERE / "_atlas" / "zichan-outline.json", encoding="utf-8"))
def e(s): return html.escape(str(s)) if s is not None else ""

CN = "〇一二三四五六七八九十"
def cn(n): return CN[n] if n < 11 else str(n)

def sub_row(s, i):
    why = e(s.get("why", "")); first = why in ("起点", "起 点") or why.startswith("起点")
    wcls = "why first" if first else "why"
    wtxt = "▸ 起点" if first else f"因为 {why}"
    return f'''<div class="sub">
  <div class="sub-n"><span class="sx">{i:02d}</span>{e(s.get("name"))}</div>
  <div class="sub-p">{e(s.get("point"))}</div>
  <div class="sub-meta"><span class="{wcls}">{wtxt}</span><span class="canon">📎 {e(s.get("canon"))}</span></div>
</div>'''

def sec_block(sec, ci, si):
    subs = "".join(sub_row(s, k + 1) for k, s in enumerate(sec.get("subs", [])))
    return f'''<div class="sec">
  <div class="sec-h"><span class="sec-no">{ci}.{si}</span><span class="sec-n">{e(sec.get("name"))}</span>
    <span class="sec-c">{len(sec.get("subs", []))} 目</span></div>
  <div class="sec-q">{e(sec.get("q", ""))}</div>
  <div class="subs">{subs}</div>
</div>'''

def ch_block(c):
    secs = "".join(sec_block(s, c["seq"], i + 1) for i, s in enumerate(c["sections"]))
    op = " open" if c["seq"] == 1 else ""
    return f'''<details class="ch"{op}>
  <summary><span class="seal">{cn(c["seq"])}</span>
    <span class="ch-main"><span class="ch-n">第{cn(c["seq"])}章 · {e(c["name"])}</span>
      <span class="ch-layer">{e(c["layer"])}</span>
      <span class="ch-q">{e(c["q"])}</span></span>
    <span class="ch-c">{c["nsec"]} 节 · {c["nsub"]} 目</span><span class="chev">▾</span></summary>
  <div class="ch-body">{secs}</div>
</details>'''

st = D["standard"]
checks = "".join(
    f'<div class="chk {"ok" if ok else "no"}"><span class="ck-k">{e(k)}</span><span class="ck-m">{"✓" if ok else "✕"}</span><span class="ck-d">{e(desc)}</span></div>'
    for k, ok, desc in st["checks"])
arc = " → ".join(f'<b>{e(c["name"])}</b>' for c in D["chapters"])
chapters = "".join(ch_block(c) for c in D["chapters"])
S = D["stats"]
fab = st.get("fabricated", [])
fabline = f'<span class="ok-dot">臆造 {len(fab)}</span>' if not fab else f'<span class="no-dot">疑似臆造 {len(fab)}</span>'

HTML = f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>《原力资产》· 四级目录 · 金标准</title>
<style>
:root{{--ink:#0a1612;--leather-deep:#0d2018;--leather:#14301f;--panel:rgba(20,48,31,.5);--panel2:rgba(28,61,41,.36);
--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;
--jade:#5a9c6e;--cream:#f0e6d2;--cream-dim:#d3c8b0;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.2);--line2:rgba(201,169,97,.1);
--serif:"Noto Serif SC","Songti SC",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:radial-gradient(1100px 640px at 82% -8%,rgba(74,124,89,.15),transparent 60%),radial-gradient(900px 600px at 4% 104%,rgba(201,169,97,.06),transparent 55%),linear-gradient(180deg,var(--ink),var(--leather-deep) 52%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:1.75;padding:0 0 80px}}
.foil{{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 52%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 24px}}
header{{text-align:center;padding:56px 24px 24px;border-bottom:1px solid var(--line)}}
.kick{{font-family:var(--display);font-size:11px;letter-spacing:.42em;color:var(--gold);text-transform:uppercase;margin-bottom:15px}}
h1{{font-weight:600;font-size:clamp(28px,5vw,46px);letter-spacing:.1em}}
.sub-t{{color:var(--gold-light);font-size:14px;margin-top:10px;letter-spacing:.05em}}
.ax{{font-family:var(--mono);font-size:12.5px;color:var(--cream-dim);margin-top:14px}}
.ax b{{color:var(--gold-light)}}
.arc{{margin:16px auto 0;font-family:var(--sans);font-size:12px;color:var(--muted);max-width:760px;line-height:2}}
.arc b{{color:var(--gold-light)}}
.kpis{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:18px}}
.kpi{{font-family:var(--mono);font-size:12px;color:var(--gold-light);padding:5px 13px;border-radius:6px;background:rgba(201,169,97,.06);border-left:2px solid var(--gold)}}
.kpi b{{color:var(--gold-bright);font-size:14px}}
/* 金标准 */
.std{{margin:30px auto 6px;border:1px solid var(--line);border-radius:14px;background:var(--panel2);padding:18px 22px}}
.std-h{{font-family:var(--serif);font-size:15px;color:var(--gold-bright);margin-bottom:14px;display:flex;align-items:center;gap:10px}}
.std-h .vd{{font-family:var(--mono);font-size:11px;color:var(--ink);background:var(--jade);padding:2px 9px;border-radius:10px}}
.std-h .ok-dot{{font-family:var(--sans);font-size:11px;color:var(--jade);border:1px solid var(--jade);border-radius:10px;padding:1px 8px}}
.checks{{display:grid;grid-template-columns:1fr 1fr;gap:9px}}
.chk{{display:flex;align-items:baseline;gap:9px;font-size:12.5px;padding:7px 11px;border-radius:8px;background:rgba(0,0,0,.16)}}
.chk .ck-k{{font-family:var(--serif);font-size:15px;color:var(--gold-light);min-width:30px}}
.chk .ck-m{{font-family:var(--mono);color:var(--jade);font-weight:700}}
.chk.no .ck-m{{color:var(--cinnabar)}}
.chk .ck-d{{color:var(--cream-dim);font-family:var(--sans);font-size:11.5px;line-height:1.5}}
.weak{{margin-top:11px;font-family:var(--sans);font-size:11px;color:var(--muted);border-left:2px solid var(--gold-deep);padding:6px 12px;background:rgba(0,0,0,.13);line-height:1.7}}
.weak b{{color:var(--gold-light)}}
/* 章 */
.ch{{margin-top:16px;border:1px solid var(--line);border-radius:14px;background:var(--panel);overflow:hidden}}
.ch[open]{{border-color:var(--gold-deep)}}
summary{{list-style:none;cursor:pointer;display:flex;align-items:center;gap:15px;padding:18px 22px;transition:.15s}}
summary::-webkit-details-marker{{display:none}}
summary:hover{{background:rgba(201,169,97,.05)}}
.seal{{font-family:var(--serif);font-size:18px;color:var(--gold-bright);width:40px;height:40px;flex:none;display:flex;align-items:center;justify-content:center;border:1px solid var(--gold-deep);border-radius:50%;background:rgba(201,169,97,.05)}}
.ch-main{{flex:1;min-width:0}}
.ch-n{{font-family:var(--serif);font-size:19px;color:var(--gold-bright);margin-right:10px}}
.ch-layer{{font-family:var(--mono);font-size:10.5px;color:var(--cinnabar-soft);border:1px solid rgba(168,54,44,.3);border-radius:10px;padding:1px 8px;vertical-align:middle}}
.ch-q{{display:block;font-family:var(--sans);font-size:12px;color:var(--muted);margin-top:5px;line-height:1.5}}
.ch-c{{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap}}
.chev{{color:var(--gold-deep);font-size:13px;transition:.2s}}
.ch[open] .chev{{transform:rotate(180deg)}}
.ch-body{{padding:4px 22px 20px;border-top:1px solid var(--line2)}}
/* 节 L3 */
.sec{{margin-top:16px;padding-left:16px;border-left:2px solid var(--gold-deep)}}
.sec-h{{display:flex;align-items:baseline;gap:10px}}
.sec-no{{font-family:var(--mono);font-size:12px;color:var(--gold-deep)}}
.sec-n{{font-family:var(--serif);font-size:16.5px;color:var(--gold-light)}}
.sec-c{{font-family:var(--mono);font-size:10px;color:var(--faint);margin-left:auto}}
.sec-q{{font-family:var(--sans);font-size:11.5px;color:var(--muted);margin:3px 0 10px;line-height:1.6}}
/* 目 L4 */
.subs{{display:flex;flex-direction:column;gap:7px}}
.sub{{padding:9px 13px;border-radius:9px;background:rgba(0,0,0,.17);border-left:2px solid var(--line)}}
.sub-n{{font-family:var(--serif);font-size:14px;color:var(--cream);display:flex;align-items:baseline;gap:8px}}
.sx{{font-family:var(--mono);font-size:10px;color:var(--gold-deep);flex:none}}
.sub-p{{font-family:var(--sans);font-size:12.5px;color:var(--cream-dim);margin:3px 0 5px;padding-left:26px;line-height:1.6}}
.sub-meta{{display:flex;gap:12px;flex-wrap:wrap;padding-left:26px}}
.why{{font-family:var(--sans);font-size:10.5px;color:var(--jade)}}
.why.first{{color:var(--gold);font-weight:600}}
.canon{{font-family:var(--mono);font-size:9.5px;color:var(--faint)}}
footer{{margin-top:46px;text-align:center;color:var(--faint);font-family:var(--sans);font-size:11px;line-height:1.9;border-top:1px solid var(--line2);padding-top:24px}}
footer a{{color:var(--muted);text-decoration:none;border-bottom:1px solid var(--line2)}}
.note{{max-width:780px;margin:22px auto 0;font-family:var(--sans);font-size:12px;color:var(--muted);border:1px dashed var(--line);border-radius:10px;padding:13px 18px;line-height:1.8}}
.note b{{color:var(--gold-light)}}
@media(max-width:680px){{.checks{{grid-template-columns:1fr}}.ch-c{{display:none}}}}
</style></head><body>
<header>
  <div class="kick">YUANLI ASSET · 4-LEVEL OUTLINE</div>
  <h1 class="foil">《原力资产》· 四级目录</h1>
  <div class="sub-t">{e(D["subtitle"])} · 书 → 章 → 节 → 目 · 金标准</div>
  <div class="ax">公理 <b>{e(D["axiom"])}</b></div>
  <div class="arc">原力U 六阶：{arc}<br/>{e(D["u_arc"])}</div>
  <div class="kpis"><span class="kpi"><b>{S["chapters"]}</b> 章</span><span class="kpi"><b>{S["sections"]}</b> 节</span><span class="kpi"><b>{S["subs"]}</b> 目</span><span class="kpi">五标准 <b>全过</b></span></div>
</header>
<div class="wrap">
  <div class="std">
    <div class="std-h">五标准校验 <span class="vd">{e(st["verdict"]).upper()}</span> {fabline}</div>
    <div class="checks">{checks}</div>
    <div class="weak"><b>最弱节（诚实标注）</b> {e(st["weakest"])}</div>
  </div>
  {chapters}
  <div class="note"><b>这是金标准模板。</b>《原力资产》6 章 42 节 172 目，每一级都是一条「因为→所以」的通关链、每个目都回溯公理 ʸx、每个目都挂真源（觉醒课/全谱/atlas/白皮书）。过了五标准之后，《原力创业》《原力OS》将同法复制。每个「目」≈ 一个可直接落笔的写作单元——这份目录就是逐节写正文的真源。</div>
  <footer>
    <div>《原力资产》四级目录 · 判断/渲染分离（zichan-outline.json + build_zichan_outline.py）· 墨绿鎏金</div>
    <div style="margin-top:8px"><a href="../index.html">← 返回三部曲门户</a> · <a href="原力三部曲-提纲架构.html">提纲架构（书→章→节）</a> · <a href="原力三部曲-概念地图.html">知识地图</a></div>
  </footer>
</div></body></html>'''

OUT = HERE / "原力资产-四级目录.html"
OUT.write_text(HTML, encoding="utf-8")
print(f"wrote {OUT.name} | {S['chapters']} 章 / {S['sections']} 节 / {S['subs']} 目")

# 同源 Markdown（写正文的纯文本真源）
md = [f"# 《原力资产》· 四级目录（书 → 章 → 节 →目）· 金标准\n",
      f"> {D['subtitle']} · 公理 **{D['axiom']}**  ",
      f"> 原力U 六阶：{' → '.join(c['name'] for c in D['chapters'])}。{D['u_arc']}  ",
      f"> 规模：**{S['chapters']} 章 / {S['sections']} 节 / {S['subs']} 目**；五标准（究竟/完备/递进/具体/递归）**全过**（critic verdict=`{st['verdict']}`，疑似臆造 {len(st.get('fabricated',[]))}）。",
      f"\n> **五标准** —— " + " · ".join(f"{k} {'✓' if ok else '✕'}（{d}）" for k, ok, d in st['checks']),
      f"\n> **最弱节（诚实标注）**：{st['weakest']}\n", "---\n"]
for c in D["chapters"]:
    md.append(f"## 第{cn(c['seq'])}章 · {c['name']}　〔{c['layer']}〕")
    md.append(f"> {c['q']}　·　{c['nsec']} 节 / {c['nsub']} 目\n")
    for i, sec in enumerate(c["sections"], 1):
        md.append(f"### {c['seq']}.{i}　{sec['name']}")
        if sec.get("q"): md.append(f"*{sec['q']}*\n")
        for k, s in enumerate(sec.get("subs", []), 1):
            why = s.get("why", ""); w = "▸ 起点" if why.startswith("起点") else f"因为 {why}"
            md.append(f"- **{s['name']}** —— {s['point']}　`{w}`　📎 {s['canon']}")
        md.append("")
    md.append("")
md.append("---\n*这份目录是逐节写《原力资产》正文的真源。每个「目」≈ 一个可直接落笔的写作单元。过五标准后，《原力创业》《原力OS》同法复制。*")
MD = HERE / "原力资产-四级目录.md"
MD.write_text("\n".join(md), encoding="utf-8")
print(f"wrote {MD.name}")
