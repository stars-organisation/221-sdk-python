from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.report_input_body import ReportInputBody
from ...models.signalement import Signalement
from ...types import Response


def _get_kwargs(
    *,
    body: ReportInputBody,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/signalements",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Signalement:
    if response.status_code == 201:
        response_201 = Signalement.from_dict(response.json())

        return response_201

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Signalement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReportInputBody,
    idempotency_key: str,
) -> Response[Error | Signalement]:
    """Signaler une erreur de donnée (Turnstile, 5 envois par heure et par adresse IP, idempotent)

    Args:
        idempotency_key (str): Une valeur par signalement : un renvoi avec la même clé renvoie le
            même signalement.
        body (ReportInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signalement]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ReportInputBody,
    idempotency_key: str,
) -> Error | Signalement | None:
    """Signaler une erreur de donnée (Turnstile, 5 envois par heure et par adresse IP, idempotent)

    Args:
        idempotency_key (str): Une valeur par signalement : un renvoi avec la même clé renvoie le
            même signalement.
        body (ReportInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signalement
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReportInputBody,
    idempotency_key: str,
) -> Response[Error | Signalement]:
    """Signaler une erreur de donnée (Turnstile, 5 envois par heure et par adresse IP, idempotent)

    Args:
        idempotency_key (str): Une valeur par signalement : un renvoi avec la même clé renvoie le
            même signalement.
        body (ReportInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signalement]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReportInputBody,
    idempotency_key: str,
) -> Error | Signalement | None:
    """Signaler une erreur de donnée (Turnstile, 5 envois par heure et par adresse IP, idempotent)

    Args:
        idempotency_key (str): Une valeur par signalement : un renvoi avec la même clé renvoie le
            même signalement.
        body (ReportInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signalement
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
