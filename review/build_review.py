#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""写作自我盘点·复盘座舱（判断/渲染分离）。
读 review/reviews/*.json + history.jsonl → 渲 review/index.html（墨绿鎏金·FTF 三维 + 模块×智能体 + 自评vs人评 + 进化backlog）。
零业务逻辑·只读 JSON 拼 HTML。改 review 数据重跑即更新。"""
import json, glob, html, pathlib
HERE = pathlib.Path(__file__).parent
reviews = [json.load(open(f, encoding="utf-8")) for f in sorted(glob.glob(str(HERE/"reviews"/"*.json")))]
history = [json.loads(l) for l in open(HERE/"history.jsonl", encoding="utf-8") if l.strip()] if (HERE/"history.jsonl").exists() else []

LIGHT = {"G": "#5a9c6e", "A": "#c9a961", "R": "#c0524a"}
LDOT = {"G": "🟢", "A": "🟡", "R": "🔴"}
def esc(s): return html.escape(str(s)) if s is not None else ""

def ftf_block(r):
    se = r.get("self_eval", {}); hs = r.get("human_score", {}) or {}
    order = [("F_共鸣", "F · 共鸣", "Feelings"), ("T_可信", "T · 可信", "Trust"), ("F_共识", "F · 共识", "Future")]
    rows = ""
    for key, label, en in order:
        d = se.get(key, {}); sc = d.get("score", 0); lt = d.get("light", "A")
        h = hs.get(key)
        hmark = (f'<span class="hh" style="left:{h}%">▼ 你 {h}</span>' if isinstance(h, (int, float)) else '<span class="hh wait">▽ 待你打分</span>')
        gap = (f'<span class="gap">差 {abs(sc-h):.0f}</span>' if isinstance(h, (int, float)) else '')
        sigs = "".join(
            f'<span class="sig" style="border-color:{LIGHT.get(s.get("light","A"))}">{LDOT.get(s.get("light","A"),"")} {esc(s.get("name"))}'
            f'<span class="sx">{esc(s.get("src",""))}</span></span>'
            for s in d.get("signals", []))
        rows += f'''<div class="ftf-row">
  <div class="ftf-h"><span class="ftf-l" style="color:{LIGHT.get(lt)}">{label}</span><span class="ftf-en">{en}</span>
    <span class="ftf-tag">{esc(d.get("tagline",""))}</span><span class="ftf-sc" style="color:{LIGHT.get(lt)}">{sc}</span>{gap}</div>
  <div class="bar"><div class="fill" style="width:{sc}%;background:{LIGHT.get(lt)}"></div>{hmark}</div>
  <div class="sigs">{sigs}</div>
</div>'''
    return rows

def modules_block(r):
    out = ""
    for m in r.get("modules_agents", []):
        ags = ""
        for a in m.get("agents", []):
            comp = a.get("component")
            cn = f'<span class="comp">{esc(comp["name"])}</span>' if comp else f'<span class="comp bad">{esc(a.get("flag","—"))}</span>'
            ags += f'<div class="ag"><b>{esc(a.get("role"))}</b>{cn}<span class="did">{esc(a.get("did") or a.get("note",""))}</span></div>'
        out += f'''<div class="mod"><div class="mod-h"><span class="mod-n">{esc(m.get("module"))}</span>
      <span class="mod-g">{esc(m.get("goal"))}</span><span class="mod-s">{esc(m.get("status"))}</span></div>{ags}</div>'''
    return out

def backlog_block(r):
    out = ""
    for b in r.get("backlog", []):
        safe = "自动安全" if b.get("auto_safe") else "需人审"
        zk = "".join(
            f'<a class="zk" href="https://moonstachain.github.io/yuanli-strategy-trilogy/" onclick="return false">＋ {esc(z.get("name"))}<span class="zx">{esc(z.get("why"))}</span></a>'
            for z in b.get("zhiku_reco", []))
        zkw = f'<div class="zks"><span class="zkl">随身智库荐补能力：</span>{zk}</div>' if zk else ""
        out += f'''<div class="bk">
  <div class="bk-h"><span class="p p-{esc(b.get("p"))}">{esc(b.get("p"))}</span><b>{esc(b.get("title"))}</b>
    <span class="bk-m">{esc(b.get("mirror"))}</span><span class="bk-safe">{safe}</span><span class="bk-st">{esc(b.get("status"))}</span></div>
  <div class="bk-why"><b>为什么</b> {esc(b.get("why"))}</div>
  <div class="bk-how"><b>怎么补</b> {esc(b.get("how"))}</div>{zkw}
</div>'''
    return out

def review_section(r):
    m = r.get("mirrors", {})
    mir = "".join(f'<div class="mir"><div class="mir-v">{(m[k].get("score") if isinstance(m[k],dict) else m[k])}</div><div class="mir-k">{esc(k)}</div><div class="mir-n">{esc(m[k].get("note","") if isinstance(m[k],dict) else "")}</div></div>' for k in m)
    return f'''<section class="rev">
  <div class="rev-h"><span class="rev-t">{esc(r.get("chapter"))}</span><span class="rev-b">《{esc(r.get("book"))}》· {esc(r.get("date"))} · {esc(r.get("wordcount"))} 字</span>
    <span class="rev-o">自评 {r.get("overall_self")}</span></div>
  <div class="gov">{esc(r.get("governing_thought"))}</div>
  <div class="sl"><span>FTF 三维自评 × 你的打分</span></div>
  <div class="ftf">{ftf_block(r)}</div>
  <div class="sl"><span>三镜 meta</span></div><div class="mirs">{mir}</div>
  <div class="sl"><span>写作模块 × 智能体</span></div><div class="mods">{modules_block(r)}</div>
  <div class="sl"><span>进化 backlog（短板 → 待办 + 随身智库荐新能力）</span></div><div class="bks">{backlog_block(r)}</div>
</section>'''

body = "".join(review_section(r) for r in reviews)
n = len(reviews)
avg = round(sum(r.get("overall_self", 0) for r in reviews) / n, 1) if n else 0
hist_pts = " · ".join(f'{h.get("chapter","")}: {h.get("overall_self")}' for h in history)

HTML = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>原力叙事 · 写作复盘 🪞</title>
<style>
:root{--ink:#0a1612;--leather-deep:#0d2018;--panel:rgba(20,48,31,.5);--panel2:rgba(28,61,41,.4);--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;--jade:#5a9c6e;--cream:#f0e6d2;--cream-dim:#d3c8b0;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.2);--line2:rgba(201,169,97,.1);--serif:"Noto Serif SC","Songti SC",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}
*{box-sizing:border-box;margin:0;padding:0}
body{background:radial-gradient(1000px 600px at 82% -8%,rgba(74,124,89,.14),transparent 60%),linear-gradient(180deg,var(--ink),var(--leather-deep) 52%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:1.75;padding:0 0 70px}
.foil{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 52%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.wrap{max-width:1000px;margin:0 auto;padding:0 26px}
header{text-align:center;padding:56px 26px 22px;border-bottom:1px solid var(--line)}
.kick{font-family:var(--display);font-size:11px;letter-spacing:.46em;color:var(--gold);text-transform:uppercase;margin-bottom:16px}
h1{font-family:var(--serif);font-weight:600;font-size:clamp(26px,4.6vw,42px);letter-spacing:.1em}
.sub{color:var(--cream-dim);font-size:13px;margin-top:12px;font-family:var(--sans)}
.kpis{display:flex;gap:9px;justify-content:center;flex-wrap:wrap;margin-top:16px}
.kpi{font-family:var(--mono);font-size:11.5px;color:var(--gold-light);padding:4px 11px;border-radius:5px;background:rgba(201,169,97,.06);border-left:2px solid var(--gold)}
.kpi b{color:var(--gold-bright)}
.howto{max-width:760px;margin:20px auto 0;font-family:var(--sans);font-size:12px;color:var(--muted);line-height:1.85;border:1px dashed var(--line);border-radius:10px;padding:13px 18px}
.howto b{color:var(--gold-light)}
.rev{margin-top:40px;border:1px solid var(--line);border-radius:16px;background:var(--panel);padding:24px 26px}
.rev-h{display:flex;align-items:baseline;gap:13px;border-bottom:1px solid var(--gold-deep);padding-bottom:12px;flex-wrap:wrap}
.rev-t{font-size:22px;color:var(--gold-bright)}.rev-b{font-family:var(--sans);font-size:12px;color:var(--muted)}
.rev-o{margin-left:auto;font-family:var(--mono);font-size:14px;color:var(--gold)}
.gov{font-size:13px;color:var(--cream-dim);line-height:1.85;margin:14px 0 6px;border-left:2px solid var(--cinnabar);padding:8px 14px;background:rgba(168,54,44,.05);border-radius:0 8px 8px 0}
.sl{font-family:var(--display);font-size:11px;letter-spacing:.18em;color:var(--gold);text-transform:uppercase;margin:26px 0 12px;border-bottom:1px solid var(--line2);padding-bottom:6px}
.ftf-row{margin-bottom:18px}
.ftf-h{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.ftf-l{font-size:17px;font-weight:600}.ftf-en{font-family:var(--display);font-size:10px;color:var(--faint);letter-spacing:.2em}
.ftf-tag{font-family:var(--sans);font-size:11.5px;color:var(--muted)}.ftf-sc{margin-left:auto;font-family:var(--mono);font-size:16px}
.gap{font-family:var(--mono);font-size:11px;color:var(--cinnabar-soft);border:1px solid rgba(192,82,74,.4);border-radius:10px;padding:1px 7px;margin-left:8px}
.bar{position:relative;height:9px;background:rgba(0,0,0,.28);border-radius:6px;margin:8px 0 9px;overflow:visible}
.fill{height:100%;border-radius:6px;opacity:.85}
.hh{position:absolute;top:-2px;transform:translateX(-50%);font-family:var(--mono);font-size:10px;color:var(--gold-bright);white-space:nowrap}
.hh.wait{right:0;left:auto;transform:none;color:var(--faint)}
.sigs{display:flex;gap:7px;flex-wrap:wrap}
.sig{font-family:var(--sans);font-size:11px;color:var(--cream-dim);border:1px solid var(--line);border-left-width:2px;border-radius:6px;padding:4px 9px;background:rgba(0,0,0,.15)}
.sig .sx{display:block;font-size:10px;color:var(--faint);margin-top:2px;max-width:230px}
.mirs{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.mir{border:1px solid var(--line2);border-radius:10px;padding:13px;background:rgba(0,0,0,.16);text-align:center}
.mir-v{font-family:var(--serif);font-size:24px;color:var(--gold-bright)}.mir-k{font-size:12.5px;color:var(--gold);margin-top:2px}.mir-n{font-family:var(--sans);font-size:10.5px;color:var(--muted);margin-top:5px;line-height:1.5}
.mods{display:flex;flex-direction:column;gap:10px}
.mod{border:1px solid var(--line);border-radius:11px;background:var(--panel2);padding:13px 16px}
.mod-h{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;margin-bottom:7px}
.mod-n{font-size:15px;color:var(--gold-bright)}.mod-g{font-family:var(--sans);font-size:11.5px;color:var(--muted)}.mod-s{margin-left:auto;font-family:var(--mono);font-size:11px;color:var(--gold-light)}
.ag{font-family:var(--sans);font-size:12px;color:var(--cream-dim);padding:3px 0 3px 12px;border-left:1px solid var(--line2);margin-bottom:3px}
.ag b{color:var(--gold-light)}.comp{font-family:var(--mono);font-size:10.5px;color:var(--jade);margin:0 7px;padding:1px 7px;border:1px solid rgba(90,156,110,.4);border-radius:9px}
.comp.bad{color:var(--cinnabar-soft);border-color:rgba(192,82,74,.4)}.did{display:block;color:var(--muted);font-size:11px;margin-top:1px}
.bks{display:flex;flex-direction:column;gap:12px}
.bk{border:1px solid var(--line);border-radius:11px;background:rgba(0,0,0,.16);padding:14px 16px}
.bk-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:7px}
.p{font-family:var(--mono);font-size:10px;font-weight:700;border-radius:5px;padding:2px 7px}.p-P0{background:var(--cinnabar);color:#fff}.p-P1{background:var(--gold);color:#1a1305}.p-P2{background:rgba(201,169,97,.25);color:var(--gold-light)}
.bk-h b{font-size:14.5px;color:var(--gold-bright)}.bk-m,.bk-safe,.bk-st{font-family:var(--mono);font-size:10.5px;color:var(--muted)}.bk-st{margin-left:auto;color:var(--gold-light)}
.bk-why,.bk-how{font-family:var(--sans);font-size:12px;color:var(--cream-dim);line-height:1.7;margin-top:3px}.bk-why b,.bk-how b{color:var(--gold);font-size:11px}
.zks{margin-top:9px;display:flex;gap:8px;flex-wrap:wrap;align-items:center}.zkl{font-family:var(--sans);font-size:11px;color:var(--muted)}
.zk{font-family:var(--sans);font-size:11.5px;color:var(--gold-light);text-decoration:none;border:1px solid var(--gold-deep);border-radius:8px;padding:4px 10px;background:rgba(201,169,97,.06)}
.zk .zx{display:block;font-size:10px;color:var(--faint);margin-top:1px}
footer{text-align:center;margin-top:40px;color:var(--faint);font-family:var(--sans);font-size:11.5px;line-height:1.9}
footer a{color:var(--muted)}
@media(max-width:680px){.mirs{grid-template-columns:1fr}}
</style></head><body>
<header>
  <div class="kick">YUANLI NARRATIVE · WRITING REVIEW</div>
  <h1 class="foil">写作自我盘点 🪞</h1>
  <div class="sub">每写完一篇 · 写作模块×智能体 + FTF 三维自评 + 你的打分 + 自进化 backlog · 接随身智库</div>
  <div class="kpis"><span class="kpi"><b>__N__</b> 篇已盘</span><span class="kpi">均分 <b>__AVG__</b></span><span class="kpi">脊柱 FTF</span><span class="kpi">智库 <b>2051</b> 组件</span></div>
  <div class="howto"><b>怎么用</b>：① 我按 FTF 三维（共鸣/可信/共识）信号自评，每条挂出处、🟢🟡🔴 诚实降级。② <b>你在 <code>review/reviews/&lt;章节&gt;.json</code> 的 <code>human_score</code> 槽给每维打 0-100</b>（push 后这页实时更新）。③ <b>自评 vs 你的分，差距最大那一维 = 我的盲区 → 进化 backlog</b>，短板调随身智库荐新能力补进流水线——这就是「你给分 → 我改进」，越往后越丰富。</div>
</header>
<div class="wrap">__BODY__
<footer>原力战略三部曲 · 写作复盘 · 判断/渲染分离（reviews/*.json + build_review.py）· <a href="https://github.com/moonstachain/yuanli-strategy-trilogy">github.com/moonstachain/yuanli-strategy-trilogy</a> · push 即更新</footer>
</div></body></html>'''

out = (HTML.replace("__BODY__", body).replace("__N__", str(n)).replace("__AVG__", str(avg)))
(HERE/"index.html").write_text(out, encoding="utf-8")
print(f"wrote review/index.html | reviews={n} avg_self={avg} | history={len(history)}")
