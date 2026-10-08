from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.activation_live_body import ActivationLiveBody
from ...models.error import Error
from ...models.mode_live import ModeLive
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: ActivationLiveBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projets/{id}/live".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ModeLive:
    if response.status_code == 200:
        response_200 = ModeLive.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ModeLive]:
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
    body: ActivationLiveBody,
) -> Response[Error | ModeLive]:
    """Activer ou désactiver le mode live du projet (administrateurs du projet ; confirmation obligatoire
    pour activer)

    Args:
        id (str): Identifiant du projet.
        body (ActivationLiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ModeLive]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ActivationLiveBody,
) -> Error | ModeLive | None:
    """Activer ou désactiver le mode live du projet (administrateurs du projet ; confirmation obligatoire
    pour activer)

    Args:
        id (str): Identifiant du projet.
        body (ActivationLiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ModeLive
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ActivationLiveBody,
) -> Response[Error | ModeLive]:
    """Activer ou désactiver le mode live du projet (administrateurs du projet ; confirmation obligatoire
    pour activer)

    Args:
        id (str): Identifiant du projet.
        body (ActivationLiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ModeLive]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: ActivationLiveBody,
) -> Error | ModeLive | None:
    """Activer ou désactiver le mode live du projet (administrateurs du projet ; confirmation obligatoire
    pour activer)

    Args:
        id (str): Identifiant du projet.
        body (ActivationLiveBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ModeLive
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
