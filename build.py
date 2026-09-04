#!/usr/bin/env python3
"""Build the static site into docs/ (GitHub Pages friendly). Run: python3 build.py"""
import os, sys, shutil, hashlib, importlib, datetime, json, re
from xml.sax.saxutils import escape as xesc

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from gen import config, layout  # noqa: E402
from gen.html import strip_tags  # noqa: E402

OUT = os.path.join(ROOT, "docs")
STATIC = os.path.join(ROOT, "static")
PAGE_MODULES = ["home", "community", "location", "builders", "homes", "costs", "faq", "videos", "blog", "about", "book", "buyers_guide", "guide_print", "legal", "misc"]


def file_hash(*paths):
    h = hashlib.md5()
    for p in paths:
        with open(p, "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:10]


def write(rel, content):
    path = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def collect_pages():
    pages = []
    for name in PAGE_MODULES:
        try:
            mod = importlib.import_module(f"gen.pages.{name}")
        except ModuleNotFoundError as e:
            if f"gen.pages.{name}" in str(e):
                print(f"  (skipping missing page module: {name})")
                continue
            raise
        pages.extend(mod.pages())
    return pages


def sitemap(pages):
    rows = []
    for p in pages:
        if p.get("noindex") or p.get("file"):
            continue
        rows.append(
            f"<url><loc>{xesc(config.SITE['domain'] + p['path'])}</loc><lastmod>{p.get('modified', config.SITE['updated_iso'])}</lastmod>"
            f"<changefreq>{p.get('changefreq', 'weekly')}</changefreq><priority>{p.get('priority', '0.7')}</priority></url>"
        )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(rows) + "\n</urlset>\n"


def robots():
    d = config.SITE["domain"]
    return ("User-agent: *\nAllow: /\n\n# AI crawlers are welcome; this site is written to be cited.\n"
            "User-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Claude-SearchBot\nAllow: /\nUser-agent: Claude-User\nAllow: /\nUser-agent: anthropic-ai\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Perplexity-User\nAllow: /\n"
            "User-agent: Google-Extended\nAllow: /\nUser-agent: Applebot-Extended\nAllow: /\nUser-agent: CCBot\nAllow: /\n\n"
            f"Sitemap: {d}/sitemap.xml\n")


def llms(pages):
    d = config.SITE["domain"]
    groups = {"Core guides": [], "Builders": [], "Blog": [], "About & contact": []}
    for p in pages:
        if p.get("noindex") or p.get("file"):
            continue
        path = p["path"]
        if path.startswith("/builders/"):
            groups["Builders"].append(p)
        elif path.startswith("/blog/"):
            groups["Blog"].append(p)
        elif path in ("/about/", "/book/", "/buyers-guide/", "/contact/", "/privacy/", "/terms/", "/accessibility/"):
            groups["About & contact"].append(p)
        else:
            groups["Core guides"].append(p)
    out = [f"# {config.SITE['name']}", "", f"> {config.SITE['description']}", "",
           f"Published by Trenton Miller (Found Your Florida, LPT Realty, LLC), a buyer's agent and former builder insider (seven years with Pulte/Del Webb and David Weekley Homes, including operations at David Weekley where he briefly oversaw SeaFlower). "
           f"Contact: {config.SITE['phone_display']}, {config.SITE['email']}. This site is independent and not affiliated with SeaFlower's developer or any builder. Data is dated on each page; last site-wide update {config.SITE['updated']}.", ""]
    for g, items in groups.items():
        if not items:
            continue
        out.append(f"## {g}")
        for p in items:
            out.append(f"- [{p['title']}]({d}{p['path']}): {p.get('description', '')}")
        out.append("")
    out.append("## Full text")
    out.append(f"- [llms-full.txt]({d}/llms-full.txt): every page as plain text")
    return "\n".join(out) + "\n"


def llms_full(pages):
    d = config.SITE["domain"]
    parts = [f"# {config.SITE['name']} — full text\n\nSource: {d}/ · Updated {config.SITE['updated']}\n"]
    for p in pages:
        if p.get("noindex") or p.get("file"):
            continue
        text = p.get("text") or strip_tags(p["body"])
        parts.append(f"\n\n---\n\n# {p['title']}\n\nURL: {d}{p['path']}\n{p.get('description', '')}\n\n{text}")
    return "".join(parts) + "\n"


def feed(pages):
    d = config.SITE["domain"]
    posts = [p for p in pages if p.get("type") == "article" and p["path"].startswith("/blog/")]
    posts.sort(key=lambda p: p.get("published", ""), reverse=True)
    items = []
    for p in posts:
        pub = p.get("published", config.SITE["updated_iso"])
        dt = datetime.datetime.strptime(pub[:10], "%Y-%m-%d").strftime("%a, %d %b %Y 08:00:00 -0400")
        items.append(f"<item><title>{xesc(p['title'])}</title><link>{d}{p['path']}</link><guid>{d}{p['path']}</guid><pubDate>{dt}</pubDate><description>{xesc(p.get('description', ''))}</description></item>")
    return ('<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel>'
            f"<title>{xesc(config.SITE['name'])} blog</title><link>{d}/blog/</link><description>{xesc(config.SITE['description'])}</description><language>en-us</language>"
            + "".join(items) + "</channel></rss>\n")


def main():
    print("Building buyinginseaflower.com …")
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(STATIC, os.path.join(OUT, "assets"))
    from tools import make_images
    make_images.run(OUT)
    layout.VERSION = file_hash(os.path.join(STATIC, "css", "main.css"), os.path.join(STATIC, "js", "main.js"))
    pages = collect_pages()
    seen = set()
    for p in pages:
        key = p.get("file") or p["path"]
        assert key not in seen, f"duplicate page: {key}"
        seen.add(key)
        html = layout.render_page(p)
        if p.get("file"):
            write(p["file"], html)
        else:
            assert p["path"].startswith("/") and p["path"].endswith("/"), f"bad path {p['path']}"
            write(p["path"] + "index.html", html)
    write("sitemap.xml", sitemap(pages))
    write("robots.txt", robots())
    write("llms.txt", llms(pages))
    write("llms-full.txt", llms_full(pages))
    write("feed.xml", feed(pages))
    write("CNAME", config.SITE["domain"].replace("https://", "").replace("http://", "") + "\n")
    write(".nojekyll", "")
    from gen.components import flower_mark
    write("favicon.svg", flower_mark(64, cls="").replace('class="" ', ""))
    write("site.webmanifest", json.dumps({"name": config.SITE["name"], "short_name": "SeaFlower Guide", "start_url": "/", "display": "browser",
                                          "background_color": "#FAF0DE", "theme_color": "#1E5540",
                                          "icons": [{"src": "/assets/images/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/images/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
    total = sum(1 for _ in pages)
    print(f"  {total} pages → {OUT}  (assets v{layout.VERSION})")


if __name__ == "__main__":
    main()
