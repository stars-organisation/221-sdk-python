from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.telephone import Telephone
from ...types import UNSET, Response


def _get_kwargs(
    *,
    numero: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["numero"] = numero

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/telephone/analyse",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Telephone:
    if response.status_code == 200:
        response_200 = Telephone.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Telephone]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    numero: str,
) -> Response[Error | Telephone]:
    """Analyser, valider et formater un numéro sénégalais

    Args:
        numero (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Telephone]
    """

    kwargs = _get_kwargs(
        numero=numero,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    numero: str,
) -> Error | Telephone | None:
    """Analyser, valider et formater un numéro sénégalais

    Args:
        numero (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Telephone
    """

    return sync_detailed(
        client=client,
        numero=numero,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    numero: str,
) -> Response[Error | Telephone]:
    """Analyser, valider et formater un numéro sénégalais

    Args:
        numero (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Telephone]
    """

    kwargs = _get_kwargs(
        numero=numero,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    numero: str,
) -> Error | Telephone | None:
    """Analyser, valider et formater un numéro sénégalais

    Args:
        numero (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Telephone
    """

    return (
        await asyncio_detailed(
            client=client,
            numero=numero,
        )
    ).parsed
