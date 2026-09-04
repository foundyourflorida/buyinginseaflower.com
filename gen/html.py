"""Tiny HTML helpers and a deliberately small Markdown-ish converter used for long-form content."""
import re
import html as _html


def esc(s):
    return _html.escape(str(s), quote=True)


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")
    return s[:80]


def attrs(**kw):
    out = []
    for k, v in kw.items():
        if v is None or v is False:
            continue
        k = k.rstrip("_").replace("_", "-")
        if v is True:
            out.append(k)
        else:
            out.append(f'{k}="{esc(v)}"')
    return (" " + " ".join(out)) if out else ""


_INLINE = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])"), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)"), r'<a href="\2">\1</a>'),
]


def inline(s):
    s = re.sub(r"&(?![a-zA-Z#0-9]+;)", "&amp;", s)
    for rx, rep in _INLINE:
        s = rx.sub(rep, s)
    # external links open in new tab
    s = re.sub(r'<a href="(https?://[^"]+)">', r'<a href="\1" target="_blank" rel="noopener">', s)
    return s


def md(text, heading_ids=True):
    """Convert a small Markdown subset to HTML.

    Supports: ## / ### headings, paragraphs, - lists, 1. lists, > quotes, | tables |, ---,
    :::trent / :::note / :::info / :::warn callout blocks (closed with :::), raw HTML lines (<...>),
    and inline **bold**, *italic*, `code`, [text](url).
    """
    lines = text.strip("\n").split("\n")
    out, buf, i = [], [], 0

    def flush():
        if buf:
            out.append("<p>" + inline(" ".join(x.strip() for x in buf)) + "</p>")
            buf.clear()

    while i < len(lines):
        s = lines[i].strip()
        if not s:
            flush(); i += 1; continue
        if s.startswith("### ") or s.startswith("## "):
            flush()
            level = 3 if s.startswith("### ") else 2
            txt = s[4:] if level == 3 else s[3:]
            hid = f' id="{slugify(re.sub(r"<[^>]+>", "", txt))}"' if heading_ids else ""
            out.append(f"<h{level}{hid}>{inline(txt)}</h{level}>")
            i += 1; continue
        if s == "---":
            flush(); out.append("<hr>"); i += 1; continue
        if s.startswith(":::"):
            flush()
            kind = s[3:].strip().split(" ", 1)
            ctype = kind[0] or "note"
            title = kind[1] if len(kind) > 1 else ""
            block = []
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                block.append(lines[i]); i += 1
            i += 1
            inner = md("\n".join(block), heading_ids=False)
            if ctype == "trent":
                out.append(
                    '<aside class="callout callout--trent"><img src="/assets/images/trenton-miller.jpg" alt="Trenton Miller" width="64" height="64" loading="lazy">'
                    f'<div><div class="callout__label">{esc(title) or "Trent&rsquo;s take"}</div>{inner}</div></aside>'
                )
            else:
                h = f"<h4>{inline(title)}</h4>" if title else ""
                out.append(f'<aside class="callout callout--{esc(ctype)}">{h}{inner}</aside>')
            continue
        if s.startswith("> "):
            flush(); q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip()[1:].strip()); i += 1
            out.append("<blockquote>" + inline(" ".join(q)) + "</blockquote>")
            continue
        if re.match(r"^[-*] ", s):
            flush(); items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i].strip()):
                items.append(lines[i].strip()[2:]); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        if re.match(r"^\d+\. ", s):
            flush(); items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(re.sub(r"^\d+\. ", "", lines[i].strip())); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
            continue
        if s.startswith("|"):
            flush(); rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            head = rows[0]
            body = [r for r in rows[1:] if not all(re.match(r"^:?-+:?$", c or "-") for c in r)]
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            tb = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body)
            out.append(f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            continue
        if s.startswith("<"):
            flush(); raw = []
            while i < len(lines) and lines[i].strip():
                raw.append(lines[i]); i += 1
            out.append("\n".join(raw))
            continue
        buf.append(s); i += 1
    flush()
    return "\n".join(out)


def strip_tags(html_text):
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html_text, flags=re.S)
    t = re.sub(r"<br\s*/?>|</p>|</li>|</h[1-6]>|</tr>|</div>", "\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = _html.unescape(t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()
