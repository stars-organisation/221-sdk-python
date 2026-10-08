from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dataset_page_jour_ferie import DatasetPageJourFerie
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_status: str | Unset = UNSET,
    year: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["q"] = q

    params["type"] = type_

    params["date_status"] = date_status

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/jours-feries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetPageJourFerie | Error:
    if response.status_code == 200:
        response_200 = DatasetPageJourFerie.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetPageJourFerie | Error]:
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
    type_: str | Unset = UNSET,
    date_status: str | Unset = UNSET,
    year: str | Unset = UNSET,
) -> Response[DatasetPageJourFerie | Error]:
    """Jours fériés du Sénégal

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        type_ (str | Unset):
        date_status (str | Unset):
        year (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetPageJourFerie | Error]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        type_=type_,
        date_status=date_status,
        year=year,
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
    type_: str | Unset = UNSET,
    date_status: str | Unset = UNSET,
    year: str | Unset = UNSET,
) -> DatasetPageJourFerie | Error | None:
    """Jours fériés du Sénégal

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        type_ (str | Unset):
        date_status (str | Unset):
        year (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetPageJourFerie | Error
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        type_=type_,
        date_status=date_status,
        year=year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_status: str | Unset = UNSET,
    year: str | Unset = UNSET,
) -> Response[DatasetPageJourFerie | Error]:
    """Jours fériés du Sénégal

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        type_ (str | Unset):
        date_status (str | Unset):
        year (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetPageJourFerie | Error]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        type_=type_,
        date_status=date_status,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    date_status: str | Unset = UNSET,
    year: str | Unset = UNSET,
) -> DatasetPageJourFerie | Error | None:
    """Jours fériés du Sénégal

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        type_ (str | Unset):
        date_status (str | Unset):
        year (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetPageJourFerie | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            type_=type_,
            date_status=date_status,
            year=year,
        )
    ).parsed
