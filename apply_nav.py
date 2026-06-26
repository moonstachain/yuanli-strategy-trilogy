#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站统一导航·幂等注入器。glob 仓内所有 *.html（跳过根 index.html），在 <body> 后注入 _nav 顶栏。
深度自适应 root（trilogy/→'../'，books/01-*/→'../../'）。幂等：marker 已存在则整块替换、不叠加。
用法：python3 apply_nav.py   或   import apply_nav; apply_nav.run()
注意：页面 build 脚本重渲后会丢 nav → 跑完任何 build_* 后重跑本脚本（build_portal.py 末尾已自动调用）。"""
import re, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import _nav

HERE = pathlib.Path(__file__).parent
MARK = re.compile(r"<!--YL-NAV-START-->.*?<!--YL-NAV-END-->", re.S)
BODY = re.compile(r"(<body[^>]*>)", re.I)

def current_key(rel: pathlib.Path):
    for _label, href, key in _nav.LINKS:
        if pathlib.Path(href).name == rel.name:
            return key
    return None

def run():
    done, skipped = [], []
    for p in sorted(HERE.rglob("*.html")):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(HERE)
        if str(rel) == "index.html":            # 门户本身有自己的 nav
            continue
        html = p.read_text(encoding="utf-8")
        if not BODY.search(html):
            skipped.append(str(rel)); continue
        root = "../" * (len(rel.parts) - 1)
        block = _nav.nav_html(root, current_key(rel))
        if "<!--YL-NAV-START-->" in html:
            html = MARK.sub(lambda _m: block, html, count=1)   # 幂等：整块替换
        else:
            html = BODY.sub(lambda m: m.group(1) + block, html, count=1)
        p.write_text(html, encoding="utf-8")
        done.append(str(rel))
    print(f"apply_nav: 注入/更新 {len(done)} 页" + (f" · 跳过 {len(skipped)}（无<body>）" if skipped else ""))
    return done

if __name__ == "__main__":
    run()
