from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.montant import Montant
from ...types import UNSET, Response


def _get_kwargs(
    *,
    montant: float,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["montant"] = montant

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/monnaie/format",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Montant:
    if response.status_code == 200:
        response_200 = Montant.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Montant]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    montant: float,
) -> Response[Error | Montant]:
    """Formater un montant en FCFA, en lettres et en euros (parité fixe)

    Args:
        montant (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Montant]
    """

    kwargs = _get_kwargs(
        montant=montant,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    montant: float,
) -> Error | Montant | None:
    """Formater un montant en FCFA, en lettres et en euros (parité fixe)

    Args:
        montant (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Montant
    """

    return sync_detailed(
        client=client,
        montant=montant,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    montant: float,
) -> Response[Error | Montant]:
    """Formater un montant en FCFA, en lettres et en euros (parité fixe)

    Args:
        montant (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Montant]
    """

    kwargs = _get_kwargs(
        montant=montant,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    montant: float,
) -> Error | Montant | None:
    """Formater un montant en FCFA, en lettres et en euros (parité fixe)

    Args:
        montant (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Montant
    """

    return (
        await asyncio_detailed(
            client=client,
            montant=montant,
        )
    ).parsed
