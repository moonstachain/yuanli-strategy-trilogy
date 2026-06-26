#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全站统一导航·单一来源。被 apply_nav.py 注入每一页。改这里 → 重跑 apply_nav 全站更新。"""

# 横向跳转链：(显示名, 相对 href, current-key=对应页文件名)
LINKS = [
    ("总纲", "trilogy/原力战略三部曲-总纲.html", "总纲"),
    ("概念地图", "trilogy/原力三部曲-概念地图.html", "概念地图"),
    ("提纲", "trilogy/原力三部曲-提纲架构.html", "提纲"),
    ("资产", "trilogy/原力资产-四级目录.html", "资产"),
    ("创业", "trilogy/原力创业-四级目录.html", "创业"),
    ("OS", "trilogy/原力OS-四级目录.html", "OS"),
]

NAV_CSS = (
    ".ylnav{position:sticky;top:0;z-index:9999;display:flex;align-items:center;gap:8px;flex-wrap:wrap;"
    "padding:8px 18px;background:rgba(9,20,16,.93);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);"
    "border-bottom:1px solid rgba(201,169,97,.24);box-shadow:0 2px 14px rgba(0,0,0,.28);"
    "font-family:'PingFang SC','Hiragino Sans GB',system-ui,sans-serif}"
    ".ylnav-home{display:flex;align-items:center;gap:7px;text-decoration:none;color:#f4e4b8;font-weight:600;"
    "font-size:14.5px;font-family:'Noto Serif SC','Songti SC',serif;padding:4px 13px 4px 9px;border-radius:9px;"
    "border:1px solid rgba(201,169,97,.3);background:rgba(201,169,97,.06);transition:.15s;white-space:nowrap}"
    ".ylnav-home:hover{background:rgba(201,169,97,.16);border-color:#c9a961;transform:translateX(-1px)}"
    ".ylnav-home .yh-ar{color:#c9a961;font-size:15px;font-family:monospace}"
    ".ylnav-sp{flex:1;min-width:8px}"
    ".ylnav-links{display:flex;gap:3px;flex-wrap:wrap;align-items:center}"
    ".ylnav-links .yl-lbl{color:#6f8470;font-size:10.5px;letter-spacing:.08em;margin-right:3px}"
    ".ylnav-links a{text-decoration:none;color:#9bae9a;font-size:12.5px;padding:4px 11px;border-radius:7px;"
    "transition:.15s;white-space:nowrap}"
    ".ylnav-links a:hover{color:#f4e4b8;background:rgba(201,169,97,.1)}"
    ".ylnav-links a.cur{color:#0a1612;background:#c9a961;font-weight:600}"
    "@media(max-width:640px){.ylnav{padding:7px 12px;gap:5px}.ylnav-links{width:100%;overflow-x:auto;"
    "flex-wrap:nowrap;-webkit-overflow-scrolling:touch}.ylnav-links .yl-lbl{display:none}.ylnav-sp{display:none}}"
)


def nav_html(root: str, current=None) -> str:
    """root = 到仓根的相对前缀（'../' 或 '../../'）。current = 当前页 key（高亮）。"""
    home = f'<a class="ylnav-home" href="{root}index.html"><span class="yh-ar">←</span>🏛 三部曲门户</a>'
    parts = []
    for label, href, key in LINKS:
        cur = ' class="cur"' if key == current else ''
        parts.append(f'<a href="{root}{href}"{cur}>{label}</a>')
    links = "".join(parts)
    return (f'<!--YL-NAV-START--><style>{NAV_CSS}</style>'
            f'<div class="ylnav">{home}<span class="ylnav-sp"></span>'
            f'<div class="ylnav-links"><span class="yl-lbl">跳转</span>{links}</div></div><!--YL-NAV-END-->')
