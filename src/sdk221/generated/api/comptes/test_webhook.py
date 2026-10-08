from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.envoi_test import EnvoiTest
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    subscription_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projets/{id}/webhooks/{subscription_id}/test".format(
            id=quote(str(id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnvoiTest | Error:
    if response.status_code == 200:
        response_200 = EnvoiTest.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EnvoiTest | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[EnvoiTest | Error]:
    """Envoyer un événement test.ping signé au point de terminaison (3 par minute au plus)

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvoiTest | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> EnvoiTest | Error | None:
    """Envoyer un événement test.ping signé au point de terminaison (3 par minute au plus)

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvoiTest | Error
    """

    return sync_detailed(
        id=id,
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[EnvoiTest | Error]:
    """Envoyer un événement test.ping signé au point de terminaison (3 par minute au plus)

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvoiTest | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
) -> EnvoiTest | Error | None:
    """Envoyer un événement test.ping signé au point de terminaison (3 par minute au plus)

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvoiTest | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed
