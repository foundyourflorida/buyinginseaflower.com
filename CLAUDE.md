# Working notes for Claude

- Static site generator in Python (no Node). Build with `python3 build.py`; output in `docs/`.
- Content is data-first: edit `gen/content/*.py`, not the HTML. Prices are quoted exactly as builders phrase them and carry an as-of date; never invent numbers.
- Every page that refers to the community must keep the developer disclaimer (in the footer via `LEGAL["not_affiliated"]`) and the brokerage name adjacent to contact points (Florida rule 61J2-10.025).
- Fair-housing copy rule: describe the property and the place, never who should live there (no "perfect for families/retirees/young professionals").
- YouTube videos are embedded through the lite facade in `components.lite_yt` (youtube-nocookie). Do not download builder/developer photos or floor plans; link to them instead.
- Preview server config lives in `.claude/launch.json` (port 8765).
