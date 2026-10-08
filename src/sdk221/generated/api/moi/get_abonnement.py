from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.suivi import Suivi
from ...types import Response


def _get_kwargs(
    jeu: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/moi/abonnements/{jeu}".format(
            jeu=quote(str(jeu), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Suivi:
    if response.status_code == 200:
        response_200 = Suivi.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Suivi]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    jeu: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | Suivi]:
    """État d’un jeu dans mes abonnements aux nouvelles versions (e-mail)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Suivi]
    """

    kwargs = _get_kwargs(
        jeu=jeu,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    jeu: str,
    *,
    client: AuthenticatedClient,
) -> Error | Suivi | None:
    """État d’un jeu dans mes abonnements aux nouvelles versions (e-mail)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Suivi
    """

    return sync_detailed(
        jeu=jeu,
        client=client,
    ).parsed


async def asyncio_detailed(
    jeu: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | Suivi]:
    """État d’un jeu dans mes abonnements aux nouvelles versions (e-mail)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Suivi]
    """

    kwargs = _get_kwargs(
        jeu=jeu,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    jeu: str,
    *,
    client: AuthenticatedClient,
) -> Error | Suivi | None:
    """État d’un jeu dans mes abonnements aux nouvelles versions (e-mail)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Suivi
    """

    return (
        await asyncio_detailed(
            jeu=jeu,
            client=client,
        )
    ).parsed
