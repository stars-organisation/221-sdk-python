from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.dataset_page_prefixe_operateur import DatasetPagePrefixeOperateur
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    operator: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["q"] = q

    params["operator"] = operator

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/operateurs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DatasetPagePrefixeOperateur | Error:
    if response.status_code == 200:
        response_200 = DatasetPagePrefixeOperateur.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DatasetPagePrefixeOperateur | Error]:
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
    operator: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[DatasetPagePrefixeOperateur | Error]:
    """Préfixes des opérateurs de téléphonie

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        operator (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetPagePrefixeOperateur | Error]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        operator=operator,
        type_=type_,
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
    operator: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> DatasetPagePrefixeOperateur | Error | None:
    """Préfixes des opérateurs de téléphonie

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        operator (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetPagePrefixeOperateur | Error
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        operator=operator,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    operator: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> Response[DatasetPagePrefixeOperateur | Error]:
    """Préfixes des opérateurs de téléphonie

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        operator (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatasetPagePrefixeOperateur | Error]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        operator=operator,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    per_page: int | Unset = 20,
    q: str | Unset = UNSET,
    operator: str | Unset = UNSET,
    type_: str | Unset = UNSET,
) -> DatasetPagePrefixeOperateur | Error | None:
    """Préfixes des opérateurs de téléphonie

    Args:
        page (int | Unset):  Default: 1.
        per_page (int | Unset):  Default: 20.
        q (str | Unset): Recherche plein texte, sans accents ni casse.
        operator (str | Unset):
        type_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatasetPagePrefixeOperateur | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            operator=operator,
            type_=type_,
        )
    ).parsed
