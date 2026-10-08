"""Contre l'API Go locale (make dev) ; API_URL remplace l'adresse par défaut."""

import os

from sdk221 import DEFAULT_BASE_URL, client, offline
from sdk221.generated.api.banques import get_banque
from sdk221.generated.api.geographie import get_lieu
from sdk221.generated.api.jours_feries import list_jours_feries
from sdk221.generated.api.telephone import analyse_telephone
from sdk221.generated.models import Error

BASE_URL = os.environ.get("API_URL", DEFAULT_BASE_URL)
api = client(base_url=BASE_URL)


def test_matches_offline_snapshot():
    phone = analyse_telephone.sync_detailed(client=api, numero="77 123 45 67")
    assert phone.parsed.operator.name == offline.operator_for("771234567")["operator"]
    assert phone.headers["RateLimit-Limit"]
    holidays = list_jours_feries.sync(client=api, year="2026", per_page=100)
    assert [day.to_dict() for day in holidays.data] == offline.holidays(2026)
    dakar = get_lieu.sync(client=api, id="reg_om6lpn2l")
    assert dakar.to_dict() == offline.place("reg_om6lpn2l")


def test_errors():
    missing = get_banque.sync_detailed(client=api, id="inconnue")
    assert missing.status_code == 404
    assert isinstance(missing.parsed, Error) and missing.parsed.code == "NOT_FOUND"
    bad_key = get_banque.sync_detailed(client=client("cle-invalide", BASE_URL), id="k0010a")
    assert bad_key.status_code == 401
