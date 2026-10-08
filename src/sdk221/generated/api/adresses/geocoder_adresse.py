from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.geocodage import Geocodage
from ...types import UNSET, Response


def _get_kwargs(
    *,
    texte: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["texte"] = texte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/adresses/geocoder",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Geocodage:
    if response.status_code == 200:
        response_200 = Geocodage.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Geocodage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    texte: str,
) -> Response[Error | Geocodage]:
    """Géocoder une adresse descriptive au lieu connu le plus fin

    Args:
        texte (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Geocodage]
    """

    kwargs = _get_kwargs(
        texte=texte,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    texte: str,
) -> Error | Geocodage | None:
    """Géocoder une adresse descriptive au lieu connu le plus fin

    Args:
        texte (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Geocodage
    """

    return sync_detailed(
        client=client,
        texte=texte,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    texte: str,
) -> Response[Error | Geocodage]:
    """Géocoder une adresse descriptive au lieu connu le plus fin

    Args:
        texte (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Geocodage]
    """

    kwargs = _get_kwargs(
        texte=texte,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    texte: str,
) -> Error | Geocodage | None:
    """Géocoder une adresse descriptive au lieu connu le plus fin

    Args:
        texte (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Geocodage
    """

    return (
        await asyncio_detailed(
            client=client,
            texte=texte,
        )
    ).parsed
