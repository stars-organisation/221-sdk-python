from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.abonnement import Abonnement
from ...models.create_webhook_x221_mode import CreateWebhookX221Mode
from ...models.error import Error
from ...models.nouveau_webhook_body import NouveauWebhookBody
from ...types import Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: NouveauWebhookBody,
    x_221_mode: CreateWebhookX221Mode | Unset = CreateWebhookX221Mode.TEST,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_221_mode, Unset):
        headers["X-221-Mode"] = str(x_221_mode)

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projets/{id}/webhooks".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Abonnement | Error:
    if response.status_code == 201:
        response_201 = Abonnement.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
    body: NouveauWebhookBody,
    x_221_mode: CreateWebhookX221Mode | Unset = CreateWebhookX221Mode.TEST,
) -> Response[Abonnement | Error]:
    """Ajouter un point de terminaison webhook (une URL, des événements du catalogue)

    Args:
        id (str): Identifiant du projet.
        x_221_mode (CreateWebhookX221Mode | Unset): Mode affiché dans le tableau de bord : le
            point de terminaison reçoit les événements de ce mode. Default:
            CreateWebhookX221Mode.TEST.
        body (NouveauWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Abonnement | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_221_mode=x_221_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauWebhookBody,
    x_221_mode: CreateWebhookX221Mode | Unset = CreateWebhookX221Mode.TEST,
) -> Abonnement | Error | None:
    """Ajouter un point de terminaison webhook (une URL, des événements du catalogue)

    Args:
        id (str): Identifiant du projet.
        x_221_mode (CreateWebhookX221Mode | Unset): Mode affiché dans le tableau de bord : le
            point de terminaison reçoit les événements de ce mode. Default:
            CreateWebhookX221Mode.TEST.
        body (NouveauWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Abonnement | Error
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        x_221_mode=x_221_mode,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauWebhookBody,
    x_221_mode: CreateWebhookX221Mode | Unset = CreateWebhookX221Mode.TEST,
) -> Response[Abonnement | Error]:
    """Ajouter un point de terminaison webhook (une URL, des événements du catalogue)

    Args:
        id (str): Identifiant du projet.
        x_221_mode (CreateWebhookX221Mode | Unset): Mode affiché dans le tableau de bord : le
            point de terminaison reçoit les événements de ce mode. Default:
            CreateWebhookX221Mode.TEST.
        body (NouveauWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Abonnement | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        x_221_mode=x_221_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauWebhookBody,
    x_221_mode: CreateWebhookX221Mode | Unset = CreateWebhookX221Mode.TEST,
) -> Abonnement | Error | None:
    """Ajouter un point de terminaison webhook (une URL, des événements du catalogue)

    Args:
        id (str): Identifiant du projet.
        x_221_mode (CreateWebhookX221Mode | Unset): Mode affiché dans le tableau de bord : le
            point de terminaison reçoit les événements de ce mode. Default:
            CreateWebhookX221Mode.TEST.
        body (NouveauWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Abonnement | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            x_221_mode=x_221_mode,
        )
    ).parsed
