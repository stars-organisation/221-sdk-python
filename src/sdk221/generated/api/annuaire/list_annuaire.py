from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.item_page import ItemPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    category: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["q"] = q

    params["category"] = category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/annuaire",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ItemPage:
    if response.status_code == 200:
        response_200 = ItemPage.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ItemPage]:
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
    q: str | Unset = UNSET,
    category: str | Unset = UNSET,
) -> Response[Error | ItemPage]:
    """Annuaire des API et SDK

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ItemPage]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        category=category,
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
    q: str | Unset = UNSET,
    category: str | Unset = UNSET,
) -> Error | ItemPage | None:
    """Annuaire des API et SDK

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ItemPage
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        category=category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    category: str | Unset = UNSET,
) -> Response[Error | ItemPage]:
    """Annuaire des API et SDK

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ItemPage]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    category: str | Unset = UNSET,
) -> Error | ItemPage | None:
    """Annuaire des API et SDK

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        category (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ItemPage
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            category=category,
        )
    ).parsed
