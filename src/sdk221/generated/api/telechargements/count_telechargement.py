from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.count_telechargement_type import CountTelechargementType
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    jeu: str,
    *,
    type_: CountTelechargementType | Unset = CountTelechargementType.TELECHARGEMENT,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/telechargements/{jeu}".format(
            jeu=quote(str(jeu), safe=""),
        ),
        "params": params,
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
    client: AuthenticatedClient | Client,
    type_: CountTelechargementType | Unset = CountTelechargementType.TELECHARGEMENT,
) -> Response[Any | Error]:
    """Compter un téléchargement ou une ouverture (anonyme, une fois par jour et par adresse IP)

    Args:
        jeu (str): Identifiant du jeu (catalogue /v1/jeux).
        type_ (CountTelechargementType | Unset):  Default: CountTelechargementType.TELECHARGEMENT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        jeu=jeu,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    jeu: str,
    *,
    client: AuthenticatedClient | Client,
    type_: CountTelechargementType | Unset = CountTelechargementType.TELECHARGEMENT,
) -> Any | Error | None:
    """Compter un téléchargement ou une ouverture (anonyme, une fois par jour et par adresse IP)

    Args:
        jeu (str): Identifiant du jeu (catalogue /v1/jeux).
        type_ (CountTelechargementType | Unset):  Default: CountTelechargementType.TELECHARGEMENT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        jeu=jeu,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    jeu: str,
    *,
    client: AuthenticatedClient | Client,
    type_: CountTelechargementType | Unset = CountTelechargementType.TELECHARGEMENT,
) -> Response[Any | Error]:
    """Compter un téléchargement ou une ouverture (anonyme, une fois par jour et par adresse IP)

    Args:
        jeu (str): Identifiant du jeu (catalogue /v1/jeux).
        type_ (CountTelechargementType | Unset):  Default: CountTelechargementType.TELECHARGEMENT.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        jeu=jeu,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    jeu: str,
    *,
    client: AuthenticatedClient | Client,
    type_: CountTelechargementType | Unset = CountTelechargementType.TELECHARGEMENT,
) -> Any | Error | None:
    """Compter un téléchargement ou une ouverture (anonyme, une fois par jour et par adresse IP)

    Args:
        jeu (str): Identifiant du jeu (catalogue /v1/jeux).
        type_ (CountTelechargementType | Unset):  Default: CountTelechargementType.TELECHARGEMENT.

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
            type_=type_,
        )
    ).parsed
