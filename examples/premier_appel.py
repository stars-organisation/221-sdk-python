"""uv run python examples/premier_appel.py (API_KEY et API_URL facultatifs)."""

import os

from sdk221 import DEFAULT_BASE_URL, client, offline
from sdk221.generated.api.jours_feries import list_jours_feries
from sdk221.generated.models import Error

api = client(os.environ.get("API_KEY"), os.environ.get("API_URL", DEFAULT_BASE_URL))
response = list_jours_feries.sync_detailed(client=api, year="2026")
if response.status_code == 200:
    first = response.parsed.data[0]
    print("En ligne :", response.parsed.pagination.total, "jours fériés en 2026, le premier :", first["date"], first["name"]["fr"], f"({first['date_status']})", "quota restant", response.headers["RateLimit-Remaining"])
elif isinstance(response.parsed, Error):
    retry = f" (réessayez dans {response.headers['Retry-After']} s)" if response.status_code == 429 else ""
    print(f"{response.status_code} {response.parsed.code} : {response.parsed.message}{retry}")
else:
    print(response.status_code, response.content.decode())

print("Hors ligne :", offline.places(level="region", q="thies")[0]["name"])
