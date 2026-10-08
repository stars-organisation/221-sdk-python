from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.rattachement import Rattachement
from ...types import UNSET, Response


def _get_kwargs(
    *,
    lat: float,
    lon: float,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lat"] = lat

    params["lon"] = lon

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/geographie/rattacher",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Rattachement:
    if response.status_code == 200:
        response_200 = Rattachement.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Rattachement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
) -> Response[Error | Rattachement]:
    """Rattacher un point GPS à sa région, son département, son arrondissement et sa commune (géocodage
    inverse)

    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Rattachement]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
) -> Error | Rattachement | None:
    """Rattacher un point GPS à sa région, son département, son arrondissement et sa commune (géocodage
    inverse)

    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Rattachement
    """

    return sync_detailed(
        client=client,
        lat=lat,
        lon=lon,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
) -> Response[Error | Rattachement]:
    """Rattacher un point GPS à sa région, son département, son arrondissement et sa commune (géocodage
    inverse)

    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Rattachement]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lat: float,
    lon: float,
) -> Error | Rattachement | None:
    """Rattacher un point GPS à sa région, son département, son arrondissement et sa commune (géocodage
    inverse)

    Args:
        lat (float):
        lon (float):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Rattachement
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            lon=lon,
        )
    ).parsed
