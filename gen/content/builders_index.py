"""Loads the per-builder data modules in display order."""
from . import builder_mi_homes, builder_pulte, builder_david_weekley, builder_cardel, builder_issa

BUILDERS = [builder_mi_homes.BUILDER, builder_pulte.BUILDER, builder_david_weekley.BUILDER, builder_cardel.BUILDER, builder_issa.BUILDER]

TIER_LABEL = {"entry": "Entry", "mid": "Mid", "upper": "Upper", "estate": "Estate"}


def by_slug(slug):
    for b in BUILDERS:
        if b["slug"] == slug:
            return b
    raise KeyError(slug)


def all_plans():
    out = []
    for b in BUILDERS:
        for c in b["collections"]:
            for p in c["plans"]:
                out.append((b, c, p))
    return out


def all_qmis():
    out = []
    for b in BUILDERS:
        for q in b["quick_move_ins"]:
            out.append((b, q))
    return out
