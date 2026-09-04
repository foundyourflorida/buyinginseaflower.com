"""Reusable HTML components. Every function returns an HTML string."""
from .html import esc, md, slugify, attrs, strip_tags
from .config import SITE, LEGAL

ICONS = {
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "message": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    "calendar": '<path d="M8 2v4M16 2v4"/><rect width="18" height="18" x="3" y="4" rx="2"/><path d="M3 10h18"/>',
    "map-pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "dollar": '<line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
    "waves": '<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "arrow": '<path d="M5 12h14M12 5l7 7-7 7"/>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
    "ruler": '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.41 2.41 0 0 1 0-3.4l2.6-2.6a2.41 2.41 0 0 1 3.4 0Z"/><path d="m14.5 12.5 2-2M11.5 9.5l2-2M8.5 6.5l2-2M17.5 15.5l2-2"/>',
    "school": '<path d="M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"/><path d="M22 10v6"/><path d="M6 12.5V16a6 3 0 0 0 12 0v-3.5"/>',
    "car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    "umbrella": '<path d="M22 12a10.06 10.06 1 0 0-20 0Z"/><path d="M12 12v8a2 2 0 0 0 4 0"/><path d="M12 2v1"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8M16 13H8M16 17H8"/>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    "hammer": '<path d="m15 12-8.373 8.373a1 1 0 1 1-3-3L12 9"/><path d="m18 15 4-4"/><path d="m21.5 11.5-1.914-1.914A2 2 0 0 1 19 8.172V7l-2.26-2.26a6 6 0 0 0-4.202-1.756L9 2.96l.92.82A6.18 6.18 0 0 1 12 8.4V10l2 2h1.172a2 2 0 0 1 1.414.586L18.5 14.5"/>',
    "trees": '<path d="M10 10v.2A3 3 0 0 1 8.9 16H5a3 3 0 0 1-1-5.8V10a3 3 0 0 1 6 0Z"/><path d="M7 16v6"/><path d="M13 19v3"/><path d="M12 19h8.3a1 1 0 0 0 .7-1.7L18 14h.3a1 1 0 0 0 .7-1.7L16 9h.2a1 1 0 0 0 .8-1.7L13 3l-1.4 1.5"/>',
    "anchor": '<path d="M12 22V8"/><path d="M5 12H2a10 10 0 0 0 20 0h-3"/><circle cx="12" cy="5" r="3"/>',
    "video": '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    "book": '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    "external": '<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
    "droplets": '<path d="M7 16.3c2.2 0 4-1.83 4-4.05 0-1.16-.57-2.26-1.71-3.19S7.29 6.75 7 5.3c-.29 1.45-1.14 2.84-2.29 3.76S3 11.1 3 12.25c0 2.22 1.8 4.05 4 4.05z"/><path d="M12.56 6.6A10.97 10.97 0 0 0 14 3.02c.5 2.5 2 4.9 4 6.5s3 3.5 3 5.5a6.98 6.98 0 0 1-11.91 4.97"/>',
    "wind": '<path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/>',
    "key": '<path d="m15.5 7.5 2.3 2.3a1 1 0 0 0 1.4 0l2.1-2.1a1 1 0 0 0 0-1.4L19 4"/><path d="m21 2-9.6 9.6"/><circle cx="7.5" cy="15.5" r="5.5"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
    "percent": '<line x1="19" x2="5" y1="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
    "compass": '<circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>',
    "plane": '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
    "cart": '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
    "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/>',
    "quote": '<path d="M16 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z"/><path d="M5 3a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2 1 1 0 0 1 1 1v1a2 2 0 0 1-2 2 1 1 0 0 0-1 1v2a1 1 0 0 0 1 1 6 6 0 0 0 6-6V5a2 2 0 0 0-2-2z"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "trending": '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/>',
    "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
}


def icon(name, cls="", size=None):
    body = ICONS.get(name, ICONS["arrow"])
    fill = "currentColor" if name in ("star",) else "none"
    s = f' width="{size}" height="{size}"' if size else ""
    return (f'<svg class="{esc(cls)}"{s} viewBox="0 0 24 24" fill="{fill}" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{body}</svg>')


def flower_mark(size=40, cls="brand__mark"):
    """The site mark: a six-petal sea flower in coral with a deep-green centre."""
    petals = "".join(
        f'<ellipse rx="8.5" ry="17" cy="-16" transform="rotate({a})" fill="#E8796B" opacity="{0.95 if a % 120 == 0 else 0.8}"/>'
        for a in range(0, 360, 60)
    )
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="-36 -36 72 72" aria-hidden="true" focusable="false">'
            f'<circle r="35" fill="#FAF0DE"/><g>{petals}</g><circle r="9" fill="#1E5540"/><circle r="3.5" fill="#FAF0DE"/></svg>')


def eho_svg():
    return ('<svg viewBox="0 0 48 48" role="img" aria-label="Equal Housing Opportunity"><path d="M24 6 4 20h6v18h28V20h6L24 6z" fill="none" stroke="currentColor" stroke-width="2.4"/>'
            '<path d="M16 24h16M16 29h16M16 34h16" stroke="currentColor" stroke-width="2.4"/></svg>')


def btn(label, href, style="primary", size="", icon_name=None, cta=None, extra="", new_tab=False):
    cls = f"btn btn--{style}" + (f" btn--{size}" if size else "") + (f" {extra}" if extra else "")
    ic = icon(icon_name) if icon_name else ""
    tgt = ' target="_blank" rel="noopener"' if new_tab else ""
    data = f' data-cta="{esc(cta)}"' if cta else ""
    return f'<a class="{cls}" href="{esc(href)}"{tgt}{data}>{ic}<span>{label}</span></a>'


def eyebrow(text, plain=False):
    return f'<p class="eyebrow{" eyebrow--plain" if plain else ""}">{text}</p>'


def section(inner, cls="", id_=None, container="container", reveal=True):
    i = f' id="{esc(id_)}"' if id_ else ""
    r = " reveal" if reveal else ""
    return f'<section class="section {cls}{r}"{i}><div class="{container}">{inner}</div></section>'


def section_head(title, lead=None, eyebrow_text=None, center=False, level=2):
    parts = [eyebrow(eyebrow_text)] if eyebrow_text else []
    parts.append(f"<h{level}>{title}</h{level}>")
    if lead:
        parts.append(f'<p class="lead">{lead}</p>')
    return f'<div class="section-head{" center" if center else ""}">{"".join(parts)}</div>'


def card(title, body, href=None, icon_name=None, kicker=None, style="", link_label="Learn more", reveal=False):
    ic = f'<div class="card__icon">{icon(icon_name)}</div>' if icon_name else ""
    kk = f'<div class="card__kicker">{esc(kicker)}</div>' if kicker else ""
    inner = f'{ic}{kk}<h3>{title}</h3><p>{body}</p>'
    cls = f"card {style}".strip()
    if href:
        return f'<a class="{cls} card--hover card--link" href="{esc(href)}">{inner}<span class="link-arrow">{link_label}</span></a>'
    return f'<div class="{cls}">{inner}</div>'


def stat(value, label, note="", small=""):
    sm = f"<small>{esc(small)}</small>" if small else ""
    nt = f'<div class="stat__note">{note}</div>' if note else ""
    return f'<div class="stat"><div class="stat__value">{value}{sm}</div><div class="stat__label">{esc(label)}</div>{nt}</div>'


def fact_strip(items):
    """items: list of (value, label, note)"""
    cells = "".join(
        f'<div><div class="stat__value">{v}</div><div class="stat__label">{esc(l)}</div>' + (f'<div class="stat__note">{n}</div>' if n else "") + "</div>"
        for v, l, n in items
    )
    return f'<div class="fact-strip">{cells}</div>'


def faq_item(q, a, cat="general", tag=None, id_=None, open_=False):
    qid = id_ or slugify(q)
    body = md(a) if not a.lstrip().startswith("<") else a
    tag_html = ""
    if tag == "insider":
        tag_html = '<span class="faq__tag faq__tag--insider">Insider perspective</span>'
    elif tag:
        tag_html = f'<span class="faq__tag">{esc(tag)}</span>'
    text = esc(q) + " " + esc(a)
    o = " open" if open_ else ""
    return (f'<details class="faq" id="{esc(qid)}" data-cat="{esc(cat)}" data-text="{text[:600]}"{o}>'
            f'<summary>{esc(q)}</summary><div class="faq__body">{body}{tag_html}</div></details>')


def faq_group(title, items, cat, intro=None):
    body = "".join(faq_item(q, a, cat, tag) for q, a, tag in items)
    ip = f'<p class="lead" style="margin-bottom:18px">{intro}</p>' if intro else ""
    return (f'<div class="faq-group" data-cat="{esc(cat)}" id="faq-{esc(cat)}"><div class="faq-group__title"><h2>{title}</h2>'
            f'<span>{len(items)} questions</span></div>{ip}{body}</div>')


def yt_thumb(video_id):
    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"


def lite_yt(video_id, title, duration="", cls="", poster=None, start=None):
    poster = poster or f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
    dur = f'<span class="lite-yt__dur">{esc(duration)}</span>' if duration else ""
    st = f' data-start="{int(start)}"' if start else ""
    return (f'<div class="lite-yt {cls}" role="button" tabindex="0" data-id="{esc(video_id)}" data-title="{esc(title)}"{st} '
            f'style="background-image:url(\'{esc(poster)}\')" aria-label="Play video: {esc(title)}">'
            f'<span class="lite-yt__play">{icon("play")}</span>{dur}<span class="lite-yt__title">{esc(title)}</span></div>')


def video_card(v, show_desc=False):
    cats = " ".join(v.get("cats", ["general"]))
    meta = []
    if v.get("date_display"):
        meta.append(esc(v["date_display"]))
    if v.get("duration"):
        meta.append(esc(v["duration"]))
    desc = f'<p class="small" style="color:var(--muted);margin:0">{esc(v["blurb"])}</p>' if show_desc and v.get("blurb") else ""
    return (f'<div class="video-card" data-filter-group="video" data-cat="{esc(cats)}">{lite_yt(v["id"], v["title"], v.get("duration", ""))}'
            f'<div class="video-card__title">{esc(v["title"])}</div><div class="video-card__meta">{" · ".join(meta)}</div>{desc}</div>')


def testimonial(quote, who, where, stars=True):
    st = '<span class="stars" aria-label="5 star review">★★★★★</span>' if stars else ""
    return (f'<figure class="testimonial"><blockquote class="testimonial__quote">{esc(quote)}</blockquote>'
            f'<figcaption class="testimonial__who">{st}<span><b>{esc(who)}</b> · {esc(where)}</span></figcaption></figure>')


def trent_take(inner_md, label="Trent's take"):
    return ('<aside class="callout callout--trent"><img src="/assets/images/trenton-miller.jpg" alt="Trenton Miller" width="64" height="64" loading="lazy">'
            f'<div><div class="callout__label">{esc(label)}</div>{md(inner_md, heading_ids=False)}</div></aside>')


def callout(inner_md, kind="note", title=None):
    h = f"<h4>{title}</h4>" if title else ""
    return f'<aside class="callout callout--{esc(kind)}">{h}{md(inner_md, heading_ids=False)}</aside>'


def cta_band(title=None, text=None, primary=None, secondary=None, note=None, eyebrow_text="Talk to a SeaFlower insider"):
    title = title or "Thinking about SeaFlower? Let&rsquo;s make sure you buy it right."
    text = text or ("A free 15-minute strategy call. I&rsquo;ll tell you which builder and lot fit what you want, what&rsquo;s "
                    "negotiable right now, and what to watch for in the contract. No pitch, no pressure.")
    primary = primary or btn("Book a free strategy call", SITE["booking_page"], "coral", "lg", "calendar", cta="cta-band-book")
    secondary = secondary or btn(f"Text {SITE['phone_display']}", f"sms:{SITE['phone_e164']}", "outline-light", "lg", "message", cta="cta-band-text")
    note = note or f"Buyer representation is by written agreement and commissions are negotiable; on new construction the builder typically pays it, so it does not raise your price. {SITE['agent']}, {SITE['brokerage']}."
    return (f'<div class="cta-band"><div class="cta-band__inner"><div>{eyebrow(eyebrow_text)}<h2>{title}</h2><p>{text}</p></div>'
            f'<div class="cta-band__actions">{primary}{secondary}<span class="cta-band__note">{note}</span></div></div></div>')


TIMELINES = [
    ("", "When are you hoping to buy?"),
    ("0-3 months", "Within 3 months"),
    ("3-6 months", "3 to 6 months"),
    ("6-12 months", "6 to 12 months"),
    ("12+ months", "12+ months, just researching"),
    ("under contract", "Already under contract, want a second opinion"),
]


def lead_form(form_id="lead", heading="Get a SeaFlower insider on your side", sub=None, submit="Send my questions",
              success=None, interest="SeaFlower", message_label="What are you trying to figure out?", compact=False,
              redirect="/thank-you/", extra_hidden=None, card=True):
    sub = sub if sub is not None else "Tell me where you are in the process. I reply personally, usually the same day."
    hidden = {"source": "buyinginseaflower.com", "interest": interest, "form": form_id}
    if extra_hidden:
        hidden.update(extra_hidden)
    hid = "".join(f'<input type="hidden" name="{esc(k)}" value="{esc(v)}">' for k, v in hidden.items())
    opts = "".join(f'<option value="{esc(v)}">{esc(l)}</option>' for v, l in TIMELINES)
    msg = "" if compact else (f'<div class="field"><label for="{form_id}-message">{esc(message_label)}</label>'
                              f'<textarea id="{form_id}-message" name="message" placeholder="Builder, budget, timeline, anything on your mind"></textarea></div>')
    action = SITE.get("form_endpoint") or ""
    success = success or "Got it. I&rsquo;ll reach out personally, usually within a few hours. Want to skip ahead? Book a time on my calendar."
    form = (
        f'<form class="form" id="{form_id}" data-lead-form action="{esc(action)}" method="post" data-redirect="{esc(redirect)}" data-success="{esc(success)}" novalidate>'
        f'{hid}<input type="hidden" name="page" value=""><input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">'
        f'<div class="form__row"><div class="field"><label for="{form_id}-name">Name</label><input id="{form_id}-name" name="name" type="text" autocomplete="name" required placeholder="First and last"></div>'
        f'<div class="field"><label for="{form_id}-email">Email</label><input id="{form_id}-email" name="email" type="email" autocomplete="email" required placeholder="you@example.com"></div></div>'
        f'<div class="form__row"><div class="field"><label for="{form_id}-phone">Phone <span style="font-weight:400;color:var(--faint)">(optional, fastest reply)</span></label><input id="{form_id}-phone" name="phone" type="tel" autocomplete="tel" placeholder="(555) 555-5555"></div>'
        f'<div class="field"><label for="{form_id}-timeline">Timeline</label><select id="{form_id}-timeline" name="timeline">{opts}</select></div></div>'
        f'{msg}'
        f'<label class="field field--check"><input type="checkbox" name="consent" value="yes" required><span>{LEGAL["consent"]}</span></label>'
        f'<button class="btn btn--coral btn--lg btn--block" type="submit">{esc(submit)}</button>'
        f'<div class="form__status" aria-live="polite"></div>'
        f'<p class="note" style="margin:4px 0 0;font-size:13px">Prefer to talk? Call or text <a href="tel:{SITE["phone_e164"]}">{SITE["phone_display"]}</a> or <a href="{SITE["booking_page"]}">book a time</a>. {SITE["agent"]}, {SITE["brokerage"]}.</p>'
        "</form>"
    )
    if not card:
        return form
    return f'<div class="form-card"><h3>{heading}</h3><p>{sub}</p>{form}</div>'


def breadcrumb(items):
    """items: list of (label, href). Last item has href None."""
    lis = []
    for label, href in items:
        if href:
            lis.append(f'<li><a href="{esc(href)}">{esc(label)}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{esc(label)}</li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, **({"item": SITE["domain"] + href} if href else {})}
            for i, (label, href) in enumerate(items)
        ],
    }


def toc(items, title="On this page"):
    lis = "".join(f'<li><a href="#{esc(i)}">{esc(l)}</a></li>' for i, l in items)
    return f'<nav class="toc" aria-label="{esc(title)}"><div class="toc__title">{esc(title)}</div><ol>{lis}</ol></nav>'


def sidebar_cta(title="Touring SeaFlower soon?", text="Bring me along, or talk first. I know the lots, the incentives and the contracts.", label="Book a free call"):
    return (f'<div class="sidebar-cta"><img src="{SITE["headshot"]}" alt="Trenton Miller" width="56" height="56" loading="lazy"><h4>{title}</h4><p>{text}</p>'
            f'{btn(label, SITE["booking_page"], "coral", icon_name="calendar", cta="sidebar-book")}'
            f'<p style="margin:12px 0 0;font-size:13px;color:#93AC9F">Or text <a href="sms:{SITE["phone_e164"]}" style="color:#fff">{SITE["phone_display"]}</a></p></div>')


def table(headers, rows, cls="", note=None, numeric_cols=()):
    th = "".join(f'<th{" class=num" if i in numeric_cols else ""}>{h}</th>' for i, h in enumerate(headers))
    tb = "".join("<tr>" + "".join(f'<td{" class=num" if i in numeric_cols else ""}>{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    n = f'<p class="table-note">{note}</p>' if note else ""
    return f'<div class="table-wrap {cls}"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>{n}'


def steps(items):
    return '<div class="steps">' + "".join(f'<div class="step"><div><h4>{t}</h4><p>{b}</p></div></div>' for t, b in items) + "</div>"


def dist_list(items):
    return '<ul class="dist-list">' + "".join(f'<li><b>{esc(n)}</b><span>{esc(d)}</span></li>' for n, d in items) + "</ul>"


def updated_badge(text=None):
    return f'<span class="updated">Updated {esc(text or SITE["updated"])}</span>'


def author_box():
    return (f'<div class="author-box"><img src="{SITE["headshot"]}" alt="Trenton Miller" width="88" height="88" loading="lazy"><div>'
            f'<h4>Written by {SITE["agent_credentials"]}</h4><p>Buyer&rsquo;s agent with {SITE["brokerage"]} and founder of Found Your Florida. Seven years on the builder side, '
            f'including operations at David Weekley Homes, where he briefly oversaw the SeaFlower community. He now represents buyers only. '
            f'<a href="/about/">More about Trenton</a> · <a href="{SITE["booking_page"]}">Book a call</a></p></div></div>')


def divider():
    return f'<div class="divider-flower">{flower_mark(36, cls="")}</div>'


def independent_note(extra=""):
    return ('<p class="disclosure disclosure--top">Independent buyer&rsquo;s guide, not the developer&rsquo;s or any builder&rsquo;s website. Figures are as '
            'published by the builders and developer on the dates noted and must be verified with them before you rely on them. '
            '<a href="https://seaflower.com/" target="_blank" rel="noopener nofollow">The developer&rsquo;s official website</a>. ' + extra + '</p>')


def sources_list(items, title="Sources and verification"):
    lis = "".join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener nofollow">{esc(t)}</a> <span style="color:var(--faint)">({esc(d)})</span></li>' for t, u, d in items)
    return f'<details class="faq" style="margin-top:2rem"><summary>{esc(title)}</summary><div class="faq__body"><ol class="source-list">{lis}</ol><p class="note" style="margin:10px 0 0">Checked {esc(SITE["updated"])}. Builder pages change often; dates show when each source was read.</p></div></details>'


def faq_schema(pairs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(md(a, heading_ids=False))}} for q, a in pairs]}


def speakable(text_html):
    return f'<div class="speakable lead">{text_html}</div>'


def brokerage_tag():
    return f'<span class="brokerage-tag">{esc(SITE["agent"])} &middot; {esc(SITE["brokerage"])}</span>'
