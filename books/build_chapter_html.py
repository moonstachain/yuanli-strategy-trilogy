#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""绿皮书章节 .md → 精装阅读版 HTML（qishi 翡翠墨绿×鎏金·判断/渲染分离）。
stdlib-only markdown 子集块解析器：# ## ### 标题 · 表格 · 围栏代码 · 有序/无序列表 · 引用 · --- 分隔 · **粗** · `码` · 〔待补〕· <!--ILLUS:key|cap--> 内联 illus/key.svg。
用法：python3 build_chapter_html.py <章节.md>  → 同名 .html。改正文重跑即更新。"""
import sys, re, html, pathlib

def inline(s):
    s = html.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`([^`]+?)`', r'<code class="ic">\1</code>', s)
    s = re.sub(r'〔(待补[^〕]*)〕', r'<span class="todo">〔\1〕</span>', s)
    return s

def render(md_path):
    md_path = pathlib.Path(md_path)
    src = md_path.read_text(encoding='utf-8')
    src = re.sub(r'<!--(?!ILLUS:).*?-->', '', src, flags=re.DOTALL)
    lines = src.split('\n')
    out, title, subtitle = [], '', ''
    body_started = [False]
    i, n = 0, len(lines)
    def is_tbl_sep(s): return bool(re.match(r'^\s*\|?[\s:|-]+\|[\s:|-]*$', s)) and '-' in s

    while i < n:
        s = lines[i].rstrip()
        st = s.strip()
        # fenced code
        if st.startswith('```'):
            j = i + 1; buf = []
            while j < n and not lines[j].strip().startswith('```'):
                buf.append(lines[j]); j += 1
            out.append('<pre class="tpl"><code>' + html.escape('\n'.join(buf)) + '</code></pre>')
            i = j + 1; continue
        # table: a |...| line followed by a separator |---|
        if st.startswith('|') and i + 1 < n and is_tbl_sep(lines[i+1]):
            rows = []; j = i
            while j < n and lines[j].strip().startswith('|'):
                rows.append(lines[j].strip()); j += 1
            cells = lambda r: [c.strip() for c in r.strip('|').split('|')]
            head = cells(rows[0]); body = rows[2:]
            th = ''.join(f'<th>{inline(c)}</th>' for c in head)
            trs = ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells(r)) + '</tr>' for r in body)
            out.append(f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
            i = j; continue
        # headings (# ## ### #### …; 4+ 级降为 h3)
        hm = re.match(r'^(#{1,6})\s+(.*)$', s)
        if hm:
            lvl, t = len(hm.group(1)), hm.group(2).strip()
            if lvl == 1: title = t
            elif lvl == 2 and (t.startswith('——') or t.startswith('--')): subtitle = t.lstrip('—-').strip()
            elif lvl == 2: out.append(f'<h2>{inline(t)}</h2>')
            else: out.append(f'<h3>{inline(t)}</h3>')
            i += 1; continue
        # divider
        if st == '---':
            if out: out.append('<div class="ornament">❧</div>')
            i += 1; continue
        # illus
        if st.startswith('<!--ILLUS:'):
            m = re.match(r'<!--ILLUS:([\w-]+)\|?(.*?)-->', st)
            if m:
                key, cap = m.group(1), m.group(2).strip()
                p = md_path.parent / 'illus' / f'{key}.svg'
                if p.exists():
                    c = f'<figcaption>{html.escape(cap)}</figcaption>' if cap else ''
                    out.append(f'<figure class="illus" data-key="{key}">{p.read_text(encoding="utf-8")}{c}</figure>')
            i += 1; continue
        # blockquote (consecutive >)
        if s.startswith('>'):
            buf = []; j = i
            while j < n and lines[j].lstrip().startswith('>'):
                buf.append(re.sub(r'^\s*>\s?', '', lines[j])); j += 1
            out.append('<blockquote class="note">' + '<br/>'.join(inline(x) for x in buf if x.strip()) + '</blockquote>')
            i = j; continue
        # lists (consecutive)
        if re.match(r'^\s*(\d+\.|[-*•]|❌|✅|☐|🔴|🟡|🟢)\s', s):
            buf = []; j = i; ordered = bool(re.match(r'^\s*\d+\.\s', s))
            while j < n and re.match(r'^\s*(\d+\.|[-*•]|❌|✅|☐|🔴|🟡|🟢)\s', lines[j]):
                item = re.sub(r'^\s*(\d+\.|[-*•])\s', '', lines[j])
                buf.append(f'<li>{inline(item)}</li>'); j += 1
            tag = 'ol' if ordered else 'ul'
            out.append(f'<{tag}>' + ''.join(buf) + f'</{tag}>')
            i = j; continue
        # blank
        if st == '':
            i += 1; continue
        # paragraph (gather consecutive plain lines)
        buf = []; j = i
        while j < n:
            x = lines[j].rstrip(); xs = x.strip()
            if xs == '' or x.startswith('#') or x.startswith('>') or xs == '---' or xs.startswith('```') or xs.startswith('|') or xs.startswith('<!--ILLUS:') or re.match(r'^\s*(\d+\.|[-*•]|❌|✅|☐|🔴|🟡|🟢)\s', x):
                break
            buf.append(x); j += 1
        txt = ''.join(buf).strip()
        if txt:
            cls = ' class="lead-cap"' if not body_started[0] else ''
            out.append(f'<p{cls}>{inline(txt)}</p>'); body_started[0] = True
        i = j if j > i else i + 1

    body = '\n'.join(out)
    sub_html = f'<div class="subtitle">{inline(subtitle)}</div>' if subtitle else ''
    book = '原力OS · 第三本' if '03-原力OS' in str(md_path) else ('原力创业 · 第二本' if '02-' in str(md_path) else '原力资产 · 第一本')
    doc = (TEMPLATE.replace('__TITLE__', html.escape(title)).replace('__SUBTITLE__', sub_html)
           .replace('__BOOK__', book).replace('__BODY__', body))
    out_path = md_path.with_suffix('.html')
    out_path.write_text(doc, encoding='utf-8')
    print(f'wrote {out_path.name} | title={title} | p={body.count("<p")} h2={body.count("<h2")} h3={body.count("<h3")} tbl={body.count("<table")} code={body.count("<pre")} fig={body.count("figure class")}')

TEMPLATE = '''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/><title>__TITLE__</title><style>
:root{--ink:#0a1612;--leather-deep:#0d2018;--leather:#14301f;--panel:rgba(20,48,31,.5);--gold-deep:#8b6f2e;--gold:#c9a961;--gold-light:#e0c887;--gold-bright:#f4e4b8;--cinnabar:#a8362c;--cinnabar-soft:#c06a5e;--jade:#5a9c6e;--cream:#efe6d4;--cream-dim:#cdc2aa;--muted:#9bae9a;--faint:#6f8470;--line:rgba(201,169,97,.18);--line2:rgba(201,169,97,.1);--serif:"Noto Serif SC","Songti SC",serif;--display:"Cinzel",Georgia,serif;--sans:"PingFang SC","Hiragino Sans GB",system-ui,sans-serif;--mono:"JetBrains Mono",Menlo,monospace}
*{box-sizing:border-box;margin:0;padding:0}
body{background:radial-gradient(1000px 620px at 82% -8%,rgba(74,124,89,.13),transparent 60%),linear-gradient(180deg,var(--ink),var(--leather-deep) 52%,var(--ink));background-attachment:fixed;color:var(--cream);font-family:var(--serif);line-height:1.95;font-size:17px;padding:0 0 90px}
.foil{background:linear-gradient(180deg,var(--gold-bright),var(--gold) 54%,var(--gold-deep));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.book{max-width:760px;margin:0 auto;padding:0 30px}
.chapter-head{text-align:center;padding:74px 26px 20px;border-bottom:1px solid var(--line);margin-bottom:42px}
.kicker{font-family:var(--display);font-size:12px;letter-spacing:.5em;color:var(--gold);text-transform:uppercase;margin-bottom:20px}
h1{font-weight:600;font-size:clamp(32px,6vw,54px);letter-spacing:.14em;line-height:1.3}
.subtitle{margin-top:18px;font-size:17px;color:var(--gold-light);font-style:italic}
h2{font-weight:600;font-size:24px;color:var(--gold-bright);letter-spacing:.04em;margin:56px 0 20px;text-align:center;position:relative}
h2::after{content:"";display:block;width:42px;height:1px;background:var(--gold-deep);margin:14px auto 0}
h3{font-weight:600;font-size:18px;color:var(--gold);letter-spacing:.03em;margin:32px 0 12px;padding-left:12px;border-left:3px solid var(--gold-deep)}
.book p{margin:0 0 20px;color:var(--cream);text-align:justify}
.book p strong{color:var(--gold-light);font-weight:600}
.book .todo{color:var(--cinnabar-soft);font-style:italic;font-size:14px;font-family:var(--sans)}
code.ic{font-family:var(--mono);font-size:.86em;color:var(--gold-light);background:rgba(201,169,97,.1);padding:1px 6px;border-radius:4px}
.lead-cap::first-letter{font-family:var(--display);font-size:3.3em;float:left;line-height:.84;margin:6px 12px 0 0;color:var(--gold);font-weight:700}
.ornament{text-align:center;color:var(--gold-deep);font-size:20px;margin:6px 0 28px;letter-spacing:.3em}
ol,ul{margin:0 0 20px;padding-left:8px;list-style:none;counter-reset:li}
.book li{position:relative;padding:5px 0 5px 30px;color:var(--cream-dim);line-height:1.8}
ol>li::before{counter-increment:li;content:counter(li);position:absolute;left:0;top:6px;font-family:var(--mono);font-size:12px;color:var(--gold);border:1px solid var(--line);border-radius:50%;width:20px;height:20px;display:flex;align-items:center;justify-content:center}
ul>li::before{content:"·";position:absolute;left:8px;color:var(--gold);font-size:20px;top:2px}
.tw{overflow-x:auto;margin:0 0 22px}
table{border-collapse:collapse;width:100%;font-size:14.5px;font-family:var(--sans)}
th{background:rgba(201,169,97,.08);color:var(--gold);text-align:left;padding:9px 13px;border-bottom:1px solid var(--gold-deep);font-weight:600;font-size:13px}
td{padding:9px 13px;border-bottom:1px solid var(--line2);color:var(--cream-dim);vertical-align:top;line-height:1.7}
td strong{color:var(--gold-light)} tr:hover td{background:rgba(201,169,97,.03)}
pre.tpl{background:rgba(0,0,0,.28);border:1px solid var(--line);border-left:3px solid var(--gold);border-radius:8px;padding:15px 18px;margin:0 0 22px;overflow-x:auto}
pre.tpl code{font-family:var(--mono);font-size:13px;color:var(--cream-dim);line-height:1.7;white-space:pre}
blockquote.note{border:1px solid var(--line);border-left:3px solid var(--cinnabar);background:rgba(168,54,44,.06);border-radius:0 10px 10px 0;padding:16px 22px;margin:24px 0;font-family:var(--sans);font-size:14px;line-height:1.85;color:var(--cream-dim)}
blockquote.note strong{color:var(--gold-light)}
figure.illus{margin:42px auto;max-width:560px;text-align:center;padding:20px 16px 14px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
figure.illus svg{width:100%;height:auto;max-width:520px;display:block;margin:0 auto;overflow:visible}
figure.illus figcaption{font-family:var(--sans);font-size:12.5px;color:var(--cream-dim);margin-top:12px;font-style:italic}
.colophon{max-width:760px;margin:50px auto 0;padding:0 30px;text-align:center;color:var(--faint);font-family:var(--sans);font-size:11.5px}
</style></head><body>
<div class="chapter-head"><div class="kicker">__BOOK__</div><h1 class="foil">__TITLE__</h1>__SUBTITLE__</div>
<article class="book">
__BODY__
</article>
<div class="colophon">原力战略三部曲 · 原力叙事引擎写作 · 翡翠墨绿 × 鎏金 · 初稿</div>
</body></html>'''

if __name__ == '__main__':
    render(sys.argv[1] if len(sys.argv) > 1 else '03-原力OS/最小闭环.md')
