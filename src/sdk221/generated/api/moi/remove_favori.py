from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    jeu: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/moi/favoris/{jeu}".format(
            jeu=quote(str(jeu), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error]:
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
) -> Response[Any | Error]:
    """Retirer un jeu de mes favoris (idempotent)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
) -> Any | Error | None:
    """Retirer un jeu de mes favoris (idempotent)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        jeu=jeu,
        client=client,
    ).parsed


async def asyncio_detailed(
    jeu: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error]:
    """Retirer un jeu de mes favoris (idempotent)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
) -> Any | Error | None:
    """Retirer un jeu de mes favoris (idempotent)

    Args:
        jeu (str): Identifiant du jeu de données (catalogue /v1/jeux).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            jeu=jeu,
            client=client,
        )
    ).parsed
