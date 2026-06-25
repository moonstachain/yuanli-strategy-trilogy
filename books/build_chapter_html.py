#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把绿皮书章节 .md 渲染成精装阅读版 HTML（qishi 翡翠墨绿×鎏金·judgment/render 分离）。
用法：python3 build_chapter_html.py <章节.md>  → 同名 .html
正文是判断（.md），样式是渲染（本脚本）；改正文重跑即更新。"""
import sys, re, html, pathlib

def inline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'（(待补[^）]*)）|〔(待补[^〕]*)〕', lambda m: '<span class="todo">〔'+(m.group(1) or m.group(2))+'〕</span>', s)
    return s

def render(md_path):
    src = pathlib.Path(md_path).read_text(encoding='utf-8')
    src = re.sub(r'<!--.*?-->', '', src, flags=re.DOTALL)  # drop meta comment
    lines = src.split('\n')
    out, para, quote = [], [], []
    title = subtitle = ''
    body_started = [False]
    def flush_para():
        if para:
            txt = ''.join(para).strip()
            if txt:
                cls = ' class="lead-cap"' if not body_started[0] else ''
                out.append(f'<p{cls}>{inline(txt)}</p>')
                body_started[0] = True
            para.clear()
    def flush_quote():
        if quote:
            out.append('<blockquote class="note">' + '<br/>'.join(inline(q) for q in quote) + '</blockquote>')
            quote.clear()
    for ln in lines:
        s = ln.rstrip()
        if s.startswith('# '):
            flush_para(); flush_quote(); title = s[2:].strip()
        elif s.startswith('## '):
            flush_para(); flush_quote()
            t = s[3:].strip()
            if t.startswith('——') or t.startswith('--'):
                subtitle = t.lstrip('—-').strip()
            else:
                out.append(f'<h2>{inline(t)}</h2>')
        elif s.strip() == '---':
            flush_para(); flush_quote()
            if out: out.append('<div class="ornament">❧</div>')
        elif s.startswith('> '):
            flush_para(); quote.append(s[2:].strip())
        elif s.strip() == '' and quote and not s.startswith('>'):
            quote.append('')
        elif s.strip() == '':
            flush_para()
        else:
            flush_para_break = quote and not s.startswith('>')
            if flush_para_break: flush_quote()
            para.append(s)
    flush_para(); flush_quote()
    body = '\n'.join(out)

    HTML = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>__TITLE__</title><style>
:root{--ink:#0a1612;--leather-deep:#0d2018;--leather:#14301f;--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;--jade:#4a7c59;--cream:#efe6d4;--cream-dim:#cdc2aa;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.18);
--serif:"Noto Serif SC","Songti SC","STSong",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;}
*{box-sizing:border-box;margin:0;padding:0}
body{background:radial-gradient(1000px 620px at 82% -8%,rgba(74,124,89,.13),transparent 60%),linear-gradient(180deg,var(--ink),var(--leather-deep) 52%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:2.05;font-size:17.5px;padding:0 0 90px;-webkit-font-smoothing:antialiased}
.foil{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 54%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.book{max-width:740px;margin:0 auto;padding:0 30px}
.chapter-head{text-align:center;padding:78px 26px 20px;border-bottom:1px solid var(--line);margin-bottom:46px}
.kicker{font-family:var(--display);font-size:12px;letter-spacing:.5em;color:var(--gold);text-transform:uppercase;margin-bottom:22px}
h1{font-weight:600;font-size:clamp(34px,6vw,56px);letter-spacing:.16em;line-height:1.3}
.subtitle{margin-top:20px;font-size:18px;color:var(--gold-light);letter-spacing:.04em;font-style:italic}
h2{font-weight:600;font-size:23px;color:var(--gold-bright);letter-spacing:.05em;margin:54px 0 22px;padding-bottom:0;text-align:center;position:relative}
h2::after{content:"";display:block;width:42px;height:1px;background:var(--gold-deep);margin:14px auto 0}
.book p{margin:0 0 22px;color:var(--cream);text-align:justify}
.book p strong{color:var(--gold-light);font-weight:600}
.book p .todo{color:var(--cinnabar-soft);font-style:italic;font-size:14.5px;font-family:var(--sans)}
.lead-cap::first-letter{font-family:var(--display);font-size:3.4em;float:left;line-height:.84;margin:6px 12px 0 0;color:var(--gold);font-weight:700}
.ornament{text-align:center;color:var(--gold-deep);font-size:20px;margin:8px 0 30px;letter-spacing:.3em}
blockquote.note{border:1px solid var(--line);border-left:3px solid var(--cinnabar);background:rgba(168,54,44,.06);border-radius:0 10px 10px 0;padding:18px 24px;margin:40px 0 0;font-family:var(--sans);font-size:13.5px;line-height:1.85;color:var(--cream-dim)}
blockquote.note strong{color:var(--gold-light)}
blockquote.note .todo{color:var(--cinnabar-soft)}
.colophon{max-width:740px;margin:54px auto 0;padding:0 30px;text-align:center;color:var(--faint);font-family:var(--sans);font-size:11.5px;letter-spacing:.06em}
</style></head><body>
<div class="chapter-head">
  <div class="kicker">原力资产 · 第一本</div>
  <h1 class="foil">__TITLE__</h1>
  __SUBTITLE__
</div>
<article class="book">
__BODY__
</article>
<div class="colophon">原力战略三部曲 · 原力叙事引擎写作 · 翡翠墨绿 × 鎏金 · 初稿</div>
</body></html>'''
    sub_html = f'<div class="subtitle">{inline(subtitle)}</div>' if subtitle else ''
    doc = (HTML.replace('__TITLE__', html.escape(title))
               .replace('__SUBTITLE__', sub_html)
               .replace('__BODY__', body))
    out_path = pathlib.Path(md_path).with_suffix('.html')
    out_path.write_text(doc, encoding='utf-8')
    print(f'wrote {out_path.name} | title={title} | paras={body.count("<p")} | sections={body.count("<h2")}')

if __name__ == '__main__':
    render(sys.argv[1] if len(sys.argv) > 1 else '01-原力资产/第一章-觉察.md')
