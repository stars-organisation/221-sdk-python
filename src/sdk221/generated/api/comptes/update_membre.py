from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.membre import Membre
from ...models.nouveau_role_body import NouveauRoleBody
from ...types import Response


def _get_kwargs(
    id: str,
    user_id: str,
    *,
    body: NouveauRoleBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/projets/{id}/membres/{user_id}".format(
            id=quote(str(id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Membre:
    if response.status_code == 200:
        response_200 = Membre.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Membre]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauRoleBody,
) -> Response[Error | Membre]:
    """Changer le rôle d'un membre (le dernier administrateur reste)

    Args:
        id (str): Identifiant du projet.
        user_id (str):
        body (NouveauRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Membre]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauRoleBody,
) -> Error | Membre | None:
    """Changer le rôle d'un membre (le dernier administrateur reste)

    Args:
        id (str): Identifiant du projet.
        user_id (str):
        body (NouveauRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Membre
    """

    return sync_detailed(
        id=id,
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauRoleBody,
) -> Response[Error | Membre]:
    """Changer le rôle d'un membre (le dernier administrateur reste)

    Args:
        id (str): Identifiant du projet.
        user_id (str):
        body (NouveauRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Membre]
    """

    kwargs = _get_kwargs(
        id=id,
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: NouveauRoleBody,
) -> Error | Membre | None:
    """Changer le rôle d'un membre (le dernier administrateur reste)

    Args:
        id (str): Identifiant du projet.
        user_id (str):
        body (NouveauRoleBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Membre
    """

    return (
        await asyncio_detailed(
            id=id,
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
