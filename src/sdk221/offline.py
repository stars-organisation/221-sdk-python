"""Données de référence embarquées (instantané versionné) : mêmes objets JSON que l'API."""

import json
import re
import unicodedata
from importlib.resources import files

_data = json.loads(files(__package__).joinpath("data.json").read_text("utf-8"))

snapshot = {
    "built_at": _data["built_at"],
    "api_version": _data["api_version"],
    "geographie": _data["geographie_meta"],
}


def normalize(value: str) -> str:
    """Copie de normalize() dans server/internal/api/data.go (règle search_key de data/src/geographie/lieux.py)."""
    text = "".join(c for c in unicodedata.normalize("NFKD", value) if not unicodedata.combining(c)).lower()
    text = re.sub(r"['’‘`ʼ]", "", text).replace("œ", "oe").replace("æ", "ae")
    return " ".join(re.sub(r"[^a-z0-9]", " ", text).split())


def holidays(year: int | str | None = None) -> list[dict]:
    """Lève ValueError pour une année absente de l'instantané : interrogez GET /v1/jours-feries?year=."""
    items = _data["jours-feries"]
    if not year:
        return items
    found = [h for h in items if h["date"].startswith(str(year))]
    if not found:
        years = sorted({h["date"][:4] for h in items})
        raise ValueError(f"Aucun jour férié embarqué pour {year} (années : {', '.join(years)}). Interrogez GET /v1/jours-feries?year={year}.")
    return found


def holiday(iso_date: str) -> dict | None:
    return next((h for h in _data["jours-feries"] if h["date"] == iso_date), None)


def operator_for(national_number: str) -> dict | None:
    """Opérateur d'origine d'un numéro national (9 chiffres, sans +221) : préfixe le plus long.
    Avec la portabilité, l'abonné peut avoir changé d'opérateur."""
    matches = [p for p in _data["operateurs"] if national_number.startswith(p["prefix"])]
    return max(matches, key=lambda p: len(p["prefix"]), default=None)


def banks(q: str | None = None) -> list[dict]:
    if not q:
        return _data["banques"]
    needle = normalize(q)
    return [b for b in _data["banques"] if needle in normalize(json.dumps(b, ensure_ascii=False))]


def bank(id_or_code: str) -> dict | None:
    """Par identifiant (« k0010a ») ou code banque BCEAO (« K 0010 A »)."""
    return next((b for b in _data["banques"] if id_or_code in (b["id"], b["bank_code"])), None)


def places(level: str | None = None, parent_id: str | None = None, q: str | None = None) -> list[dict]:
    """Mêmes filtres et même tri que GET /v1/geographie, sans pagination."""
    needle = normalize(q) if q else ""
    matches = [
        p
        for p in _data["geographie"]
        if (not level or p["level"] == level)
        and (not parent_id or p["parent_id"] == parent_id)
        and (not needle or needle in p["search_key"] or needle in normalize(p["name"] or ""))
    ]
    if not needle:
        return matches
    return sorted(matches, key=lambda p: 0 if p["search_key"] == needle else 1 if p["search_key"].startswith(needle) else 2)


def place(id: str) -> dict | None:
    """Même forme que GET /v1/geographie/{id} : le lieu, ses ancêtres (région d'abord) et ses enfants."""
    by_id = {p["id"]: p for p in _data["geographie"]}
    found = by_id.get(id)
    if not found:
        return None
    ancestors = []
    parent = by_id.get(found["parent_id"] or "")
    while parent:
        ancestors.insert(0, parent)
        parent = by_id.get(parent["parent_id"] or "")
    children = [p for p in _data["geographie"] if p["parent_id"] == id]
    return {**found, "ancestors": ancestors, "children": children}
