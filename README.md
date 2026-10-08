# SDK Python 221

Client de l'API 221 généré depuis l'OpenAPI par
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
(EF-221-02), vérification des signatures de webhook et données de référence hors
ligne (EF-221-03). Distribution `sdk-221`, module `sdk221`. Site et documentation :
<https://221.orvlabs.com/documentation>. Le code généré est rebâti dans le dépôt
principal (`generate.sh`) ; ce dépôt publie le résultat.

| Module | Contenu | Origine |
| --- | --- | --- |
| `sdk221.generated` | `Client`, `AuthenticatedClient`, `api.<tag>.<opération>`, `models` | Généré (httpx + attrs), jamais modifié à la main |
| `sdk221` | `client(api_key, base_url)`, `verify_webhook(...)` | Écrit à la main |
| `sdk221.offline` | `holidays`, `holiday`, `operator_for`, `banks`, `bank`, `places`, `place`, `snapshot` | Instantané versionné de `server/data.json` |

## Installation

```sh
uv add sdk-221     # ou, dans un environnement virtuel : pip install sdk-221
```

Pas encore publié sur PyPI : la commande fonctionnera à la publication.

## Développement

```sh
cd packages/sdk-python
./generate.sh      # Node et uv ; contrat Go (make openapi, sans serveur) : OpenAPI, instantané, client
uv run pytest      # tests/test_api.py appelle l'API Go locale (make dev)
```

## Clés API

Une clé a la forme `sk_221_pay_test_…` (mode test) ou `sk_221_pay_live_…` (mode réel).
Les clés déjà émises avec `221pay_test_`, `221pay_live_` ou `sk_221_` restent acceptées.

```python
import os
from sdk221 import client

api = client(os.environ["API_KEY"])  # Authorization: Bearer <clé> ; base_url= pour une autre adresse
```

Les routes de données fonctionnent aussi sans clé (`client()`), avec un quota bas
par adresse IP.

## Créer un paiement

`Idempotency-Key` est propre à chaque paiement : renvoyer la même valeur ne crée
pas de doublon. Le contrat décrit le corps des routes de paiement comme du
binaire et ne liste que la réponse 200, alors que la création répond 201 : on
passe par le client `httpx` du SDK, qui porte déjà la clé.

```python
response = api.get_httpx_client().post(
    "/v1/payments",
    headers={"Idempotency-Key": "commande-1042"},
    json={
        "amount": "10000",
        "currency": "XOF",
        "rail": "sn_wave",
        "merchant_reference": "commande-1042",
        "return_url": "https://boutique.example/merci",
    },
)
response.raise_for_status()
payment = response.json()
```

## Vérifier un webhook

Lisez le corps brut avant tout décodage JSON ; refusez la requête si la
fonction renvoie `False` (signature fausse, ou horodatage de plus de 5 minutes,
`max_age_seconds` pour changer la durée).

```python
from sdk221 import verify_webhook

# FastAPI : raw_body = await request.body()
if not verify_webhook(WEBHOOK_SECRET, request.headers.get("X-221-Timestamp", ""), raw_body, request.headers.get("X-221-Signature", "")):
    raise HTTPException(status_code=401)
```

Dédupliquez sur l'identifiant de l'événement : une livraison peut être rejouée.

## Premier appel, sans clé

```python
from sdk221 import client
from sdk221.generated.api.jours_feries import list_jours_feries

api = client()  # https://apps.orvlabs.com par défaut
jours = list_jours_feries.sync(client=api, year="2026")
print(jours.data[0]["name"]["fr"])  # « Jour de l'an »
```

Chaque opération existe en `sync`, `sync_detailed`, `asyncio` et `asyncio_detailed`.

## Erreurs et quotas

`sync_detailed` renvoie le statut, les en-têtes et `parsed` : le modèle attendu
pour 200, un `Error` (`code`, `message`, `request_id`, `fields`) pour les
erreurs décrites, `None` sinon. Testez `code` (en majuscules, par exemple
`QUOTA_EXCEEDED`), pas le statut.

```python
from sdk221.generated.models import Error

response = list_jours_feries.sync_detailed(client=api, year="2026")
if response.status_code == 429:
    wait = int(response.headers["Retry-After"])  # secondes ; ou utilisez une clé
elif isinstance(response.parsed, Error):
    raise RuntimeError(f"{response.parsed.code}: {response.parsed.message}")
```

Ne relancez pas un 429 en boucle : attendez `Retry-After` secondes.

## Hors ligne

```python
from sdk221 import offline

offline.holidays(2026)                   # jours fériés (date_status : confirmee ou previsionnelle) ; ValueError hors des années embarquées
offline.operator_for("771234567")        # opérateur du préfixe d'origine (portabilité possible)
offline.bank("K 0010 A")                 # par id ou code banque BCEAO
offline.places(level="region", q="thies")
offline.place("reg_om6lpn2l")            # avec ancêtres et enfants, comme l'API
offline.snapshot["built_at"]             # date des données embarquées
```

Les fonctions renvoient les mêmes objets JSON que l'API. Validation et
formatage des numéros et des montants (modules `telephonie` et `monnaie`) : dans
le SDK TypeScript seulement pour l'instant.

## Exemple

```sh
uv run python examples/premier_appel.py   # API_KEY et API_URL facultatifs
```

`normalize()` dans `offline.py` recopie celle de `server/internal/api/data.go` ;
`tests/test_api.py` compare les recherches hors ligne aux réponses de l'API (le
quota anonyme est de 10 appels par minute).
