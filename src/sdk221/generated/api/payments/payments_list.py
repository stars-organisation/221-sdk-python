from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.pay_error import PayError
from ...models.payment_list import PaymentList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    method: str | Unset = UNSET,
    rail: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    q: str | Unset = UNSET,
    customer_phone: str | Unset = UNSET,
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

    params["limit"] = limit

    params["offset"] = offset

    params["cursor"] = cursor

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = status

    else:
        json_status = status
    params["status"] = json_status

    params["method"] = method

    params["rail"] = rail

    params["from"] = from_

    params["to"] = to

    params["q"] = q

    params["customer_phone"] = customer_phone

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/payments",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PayError | PaymentList:
    if response.status_code == 200:
        response_200 = PaymentList.from_dict(response.json())

        return response_200

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
) -> Response[PayError | PaymentList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    method: str | Unset = UNSET,
    rail: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    q: str | Unset = UNSET,
    customer_phone: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[PayError | PaymentList]:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        cursor (str | Unset):
        status (list[str] | None | Unset):
        method (str | Unset):
        rail (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        q (str | Unset):
        customer_phone (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayError | PaymentList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        lang=lang,
        limit=limit,
        offset=offset,
        cursor=cursor,
        status=status,
        method=method,
        rail=rail,
        from_=from_,
        to=to,
        q=q,
        customer_phone=customer_phone,
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
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    method: str | Unset = UNSET,
    rail: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    q: str | Unset = UNSET,
    customer_phone: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> PayError | PaymentList | None:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        cursor (str | Unset):
        status (list[str] | None | Unset):
        method (str | Unset):
        rail (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        q (str | Unset):
        customer_phone (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayError | PaymentList
    """

    return sync_detailed(
        client=client,
        project_id=project_id,
        lang=lang,
        limit=limit,
        offset=offset,
        cursor=cursor,
        status=status,
        method=method,
        rail=rail,
        from_=from_,
        to=to,
        q=q,
        customer_phone=customer_phone,
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
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    method: str | Unset = UNSET,
    rail: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    q: str | Unset = UNSET,
    customer_phone: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> Response[PayError | PaymentList]:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        cursor (str | Unset):
        status (list[str] | None | Unset):
        method (str | Unset):
        rail (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        q (str | Unset):
        customer_phone (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PayError | PaymentList]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        lang=lang,
        limit=limit,
        offset=offset,
        cursor=cursor,
        status=status,
        method=method,
        rail=rail,
        from_=from_,
        to=to,
        q=q,
        customer_phone=customer_phone,
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
    project_id: str | Unset = UNSET,
    lang: str | Unset = UNSET,
    limit: str | Unset = UNSET,
    offset: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    status: list[str] | None | Unset = UNSET,
    method: str | Unset = UNSET,
    rail: str | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    q: str | Unset = UNSET,
    customer_phone: str | Unset = UNSET,
    authorization: str | Unset = UNSET,
    x_api_key: str | Unset = UNSET,
    cookie: str | Unset = UNSET,
    x_221_external_ref: str | Unset = UNSET,
    x_221_project_id: str | Unset = UNSET,
    accept_language: str | Unset = UNSET,
) -> PayError | PaymentList | None:
    """
    Args:
        project_id (str | Unset):
        lang (str | Unset):
        limit (str | Unset):
        offset (str | Unset):
        cursor (str | Unset):
        status (list[str] | None | Unset):
        method (str | Unset):
        rail (str | Unset):
        from_ (str | Unset):
        to (str | Unset):
        q (str | Unset):
        customer_phone (str | Unset):
        authorization (str | Unset):
        x_api_key (str | Unset):
        cookie (str | Unset):
        x_221_external_ref (str | Unset):
        x_221_project_id (str | Unset):
        accept_language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PayError | PaymentList
    """

    return (
        await asyncio_detailed(
            client=client,
            project_id=project_id,
            lang=lang,
            limit=limit,
            offset=offset,
            cursor=cursor,
            status=status,
            method=method,
            rail=rail,
            from_=from_,
            to=to,
            q=q,
            customer_phone=customer_phone,
            authorization=authorization,
            x_api_key=x_api_key,
            cookie=cookie,
            x_221_external_ref=x_221_external_ref,
            x_221_project_id=x_221_project_id,
            accept_language=accept_language,
        )
    ).parsed
