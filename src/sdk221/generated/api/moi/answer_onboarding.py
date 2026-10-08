from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.answer_input_body import AnswerInputBody
from ...models.answer_onboarding_question import AnswerOnboardingQuestion
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    question: AnswerOnboardingQuestion,
    *,
    body: AnswerInputBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/moi/onboarding/{question}".format(
            question=quote(str(question), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    question: AnswerOnboardingQuestion,
    *,
    client: AuthenticatedClient,
    body: AnswerInputBody,
) -> Response[Any | Error]:
    """Enregistrer une réponse d’accueil (idempotent)

    Args:
        question (AnswerOnboardingQuestion):
        body (AnswerInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        question=question,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    question: AnswerOnboardingQuestion,
    *,
    client: AuthenticatedClient,
    body: AnswerInputBody,
) -> Any | Error | None:
    """Enregistrer une réponse d’accueil (idempotent)

    Args:
        question (AnswerOnboardingQuestion):
        body (AnswerInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        question=question,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    question: AnswerOnboardingQuestion,
    *,
    client: AuthenticatedClient,
    body: AnswerInputBody,
) -> Response[Any | Error]:
    """Enregistrer une réponse d’accueil (idempotent)

    Args:
        question (AnswerOnboardingQuestion):
        body (AnswerInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        question=question,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    question: AnswerOnboardingQuestion,
    *,
    client: AuthenticatedClient,
    body: AnswerInputBody,
) -> Any | Error | None:
    """Enregistrer une réponse d’accueil (idempotent)

    Args:
        question (AnswerOnboardingQuestion):
        body (AnswerInputBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            question=question,
            client=client,
            body=body,
        )
    ).parsed
