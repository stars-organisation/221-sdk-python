from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.abonnement import Abonnement
from ...models.error import Error
from ...models.webhook_events_body import WebhookEventsBody
from ...types import Response


def _get_kwargs(
    id: str,
    subscription_id: str,
    *,
    body: WebhookEventsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/projets/{id}/webhooks/{subscription_id}".format(
            id=quote(str(id), safe=""),
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Abonnement | Error:
    if response.status_code == 200:
        response_200 = Abonnement.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Abonnement | Error]:
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
    body: WebhookEventsBody,
) -> Response[Abonnement | Error]:
    """Choisir les événements et les modes d’un point de terminaison webhook

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):
        body (WebhookEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Abonnement | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        subscription_id=subscription_id,
        body=body,
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
    body: WebhookEventsBody,
) -> Abonnement | Error | None:
    """Choisir les événements et les modes d’un point de terminaison webhook

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):
        body (WebhookEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Abonnement | Error
    """

    return sync_detailed(
        id=id,
        subscription_id=subscription_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookEventsBody,
) -> Response[Abonnement | Error]:
    """Choisir les événements et les modes d’un point de terminaison webhook

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):
        body (WebhookEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Abonnement | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        subscription_id=subscription_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    subscription_id: str,
    *,
    client: AuthenticatedClient,
    body: WebhookEventsBody,
) -> Abonnement | Error | None:
    """Choisir les événements et les modes d’un point de terminaison webhook

    Args:
        id (str): Identifiant du projet.
        subscription_id (str):
        body (WebhookEventsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Abonnement | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            subscription_id=subscription_id,
            client=client,
            body=body,
        )
    ).parsed
