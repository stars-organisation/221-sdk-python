from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.cle_creee import CleCreee
from ...models.error import Error
from ...models.rotation_cle_body import RotationCleBody
from ...types import Response


def _get_kwargs(
    id: str,
    key_id: str,
    *,
    body: RotationCleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projets/{id}/cles/{key_id}/rotate".format(
            id=quote(str(id), safe=""),
            key_id=quote(str(key_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CleCreee | Error:
    if response.status_code == 201:
        response_201 = CleCreee.from_dict(response.json())

        return response_201

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CleCreee | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: RotationCleBody,
) -> Response[CleCreee | Error]:
    """Remplacer une clé API : nouvelle clé (même nom, mode, portées et quota), l'ancienne reste valide
    pendant le délai choisi

    Args:
        id (str): Identifiant du projet.
        key_id (str):
        body (RotationCleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CleCreee | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        key_id=key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: RotationCleBody,
) -> CleCreee | Error | None:
    """Remplacer une clé API : nouvelle clé (même nom, mode, portées et quota), l'ancienne reste valide
    pendant le délai choisi

    Args:
        id (str): Identifiant du projet.
        key_id (str):
        body (RotationCleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CleCreee | Error
    """

    return sync_detailed(
        id=id,
        key_id=key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: RotationCleBody,
) -> Response[CleCreee | Error]:
    """Remplacer une clé API : nouvelle clé (même nom, mode, portées et quota), l'ancienne reste valide
    pendant le délai choisi

    Args:
        id (str): Identifiant du projet.
        key_id (str):
        body (RotationCleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CleCreee | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        key_id=key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    key_id: str,
    *,
    client: AuthenticatedClient,
    body: RotationCleBody,
) -> CleCreee | Error | None:
    """Remplacer une clé API : nouvelle clé (même nom, mode, portées et quota), l'ancienne reste valide
    pendant le délai choisi

    Args:
        id (str): Identifiant du projet.
        key_id (str):
        body (RotationCleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CleCreee | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            key_id=key_id,
            client=client,
            body=body,
        )
    ).parsed
