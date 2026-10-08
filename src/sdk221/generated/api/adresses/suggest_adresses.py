from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.suggestions import Suggestions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/adresses/suggestions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Suggestions:
    if response.status_code == 200:
        response_200 = Suggestions.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Suggestions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
) -> Response[Error | Suggestions]:
    """Suggestions à la saisie : régions, départements, arrondissements, communes et localités

    Args:
        q (str):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Suggestions]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
) -> Error | Suggestions | None:
    """Suggestions à la saisie : régions, départements, arrondissements, communes et localités

    Args:
        q (str):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Suggestions
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
) -> Response[Error | Suggestions]:
    """Suggestions à la saisie : régions, départements, arrondissements, communes et localités

    Args:
        q (str):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Suggestions]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str,
    limit: int | Unset = 10,
) -> Error | Suggestions | None:
    """Suggestions à la saisie : régions, départements, arrondissements, communes et localités

    Args:
        q (str):
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Suggestions
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
        )
    ).parsed
