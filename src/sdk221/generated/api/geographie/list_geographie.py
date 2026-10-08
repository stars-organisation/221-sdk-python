from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lieu_page import LieuPage
from ...models.list_geographie_level import ListGeographieLevel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    level: ListGeographieLevel | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_level: str | Unset = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    params["parent_id"] = parent_id

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/geographie",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LieuPage:
    if response.status_code == 200:
        response_200 = LieuPage.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | LieuPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    level: ListGeographieLevel | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[Error | LieuPage]:
    """Lieux : filtre par niveau, parent ou recherche tolérante

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        level (ListGeographieLevel | Unset):
        parent_id (str | Unset):
        q (str | Unset): Sans accents ni casse ; « thies » trouve Thiès.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LieuPage]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        level=level,
        parent_id=parent_id,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    level: ListGeographieLevel | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Error | LieuPage | None:
    """Lieux : filtre par niveau, parent ou recherche tolérante

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        level (ListGeographieLevel | Unset):
        parent_id (str | Unset):
        q (str | Unset): Sans accents ni casse ; « thies » trouve Thiès.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LieuPage
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        level=level,
        parent_id=parent_id,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    level: ListGeographieLevel | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Response[Error | LieuPage]:
    """Lieux : filtre par niveau, parent ou recherche tolérante

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        level (ListGeographieLevel | Unset):
        parent_id (str | Unset):
        q (str | Unset): Sans accents ni casse ; « thies » trouve Thiès.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LieuPage]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        level=level,
        parent_id=parent_id,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    level: ListGeographieLevel | Unset = UNSET,
    parent_id: str | Unset = UNSET,
    q: str | Unset = UNSET,
) -> Error | LieuPage | None:
    """Lieux : filtre par niveau, parent ou recherche tolérante

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        level (ListGeographieLevel | Unset):
        parent_id (str | Unset):
        q (str | Unset): Sans accents ni casse ; « thies » trouve Thiès.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LieuPage
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            level=level,
            parent_id=parent_id,
            q=q,
        )
    ).parsed
