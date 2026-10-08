"""SDK Python de l'API 221. Les fonctions d'appel sont dans sdk221.generated.api.<tag>."""

from .generated import AuthenticatedClient, Client
from .webhook import verify_webhook

DEFAULT_BASE_URL = "https://apps.orvlabs.com"


def client(api_key: str | None = None, base_url: str = DEFAULT_BASE_URL) -> Client | AuthenticatedClient:
    """Sans clé : quota bas par adresse IP. Avec clé : en-tête Authorization: Bearer <clé>."""
    if api_key:
        return AuthenticatedClient(base_url=base_url, token=api_key)
    return Client(base_url=base_url)


__all__ = ["AuthenticatedClient", "Client", "DEFAULT_BASE_URL", "client", "verify_webhook"]
