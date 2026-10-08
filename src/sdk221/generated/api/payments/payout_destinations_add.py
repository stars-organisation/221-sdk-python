from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.pay_error import PayError
from ...models.payout_destination import PayoutDestination
from ...models.payout_destination_request import PayoutDestinationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PayoutDestinationRequest,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    if not isinstance(x_api_key, Unset):
        headers["X-API-Key"] = x_api_key

    if not isinstance(cookie, Unset):
        headers["Cookie"] = cookie

    if not isinstance(x_221_external_ref, Unset):
        headers["X-221-External-Ref"] = x_221_external_ref

    if not isinstance(x_221_project_id, Unset):
        headers["X-221-Project-Id"] = x_221_project_id

    if not isinstance(accept_language, Unset):
        headers["Accept-Language"] = accept_language

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["lang"] = lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/payout-destinations",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PayError | PayoutDestination:
    if response.status_code == 200:
        response_200 = PayoutDestination.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = PayoutDestination.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = PayError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PayError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = PayError.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = PayError.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = PayError.from_dict(response.json())

        return response_503

    response_default = PayError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PayError | PayoutDestination]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PayoutDestinationRequest,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[PayError | PayoutDestination]:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):
        body (PayoutDestinationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayError | PayoutDestination]
    """

    kwargs = _get_kwargs(
        body=body,
        project_id=project_id,
        lang=lang,
        authorization=authorization,
        x_api_key=x_api_key,
        cookie=cookie,
        x_221_external_ref=x_221_external_ref,
        x_221_project_id=x_221_project_id,
        accept_language=accept_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PayoutDestinationRequest,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> PayError | PayoutDestination | None:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):
        body (PayoutDestinationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayError | PayoutDestination
    """

    return sync_detailed(
        client=client,
        body=body,
        project_id=project_id,
        lang=lang,
        authorization=authorization,
        x_api_key=x_api_key,
        cookie=cookie,
        x_221_external_ref=x_221_external_ref,
        x_221_project_id=x_221_project_id,
        accept_language=accept_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PayoutDestinationRequest,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[PayError | PayoutDestination]:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):
        body (PayoutDestinationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayError | PayoutDestination]
    """

    kwargs = _get_kwargs(
        body=body,
        project_id=project_id,
        lang=lang,
        authorization=authorization,
        x_api_key=x_api_key,
        cookie=cookie,
        x_221_external_ref=x_221_external_ref,
        x_221_project_id=x_221_project_id,
        accept_language=accept_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PayoutDestinationRequest,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> PayError | PayoutDestination | None:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):
        body (PayoutDestinationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayError | PayoutDestination
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            project_id=project_id,
            lang=lang,
            authorization=authorization,
            x_api_key=x_api_key,
            cookie=cookie,
            x_221_external_ref=x_221_external_ref,
            x_221_project_id=x_221_project_id,
            accept_language=accept_language,
        )
    ).parsed
