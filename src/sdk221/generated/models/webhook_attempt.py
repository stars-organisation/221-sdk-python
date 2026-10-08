from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.webhook_request import WebhookRequest
    from ..models.webhook_response import WebhookResponse


T = TypeVar("T", bound="WebhookAttempt")


@_attrs_define
class WebhookAttempt:
    """
    Attributes:
        created_at (datetime.datetime):
        delivery_attempt (int): Numéro de l'essai, à partir de 1.
        id (UUID):
        is_delivery_successful (bool): true pour une réponse 2xx.
        livemode (bool): true : objet du mode live ; false : mode test.
        request (WebhookRequest):
        response (WebhookResponse):
    """

    created_at: datetime.datetime
    delivery_attempt: int
    id: UUID
    is_delivery_successful: bool
    livemode: bool
    request: WebhookRequest
    response: WebhookResponse

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        delivery_attempt = self.delivery_attempt

        id = str(self.id)

        is_delivery_successful = self.is_delivery_successful

        livemode = self.livemode

        request = self.request.to_dict()

        response = self.response.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "delivery_attempt": delivery_attempt,
                "id": id,
                "is_delivery_successful": is_delivery_successful,
                "livemode": livemode,
                "request": request,
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_request import WebhookRequest
        from ..models.webhook_response import WebhookResponse

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        delivery_attempt = d.pop("delivery_attempt")

        id = UUID(d.pop("id"))

        is_delivery_successful = d.pop("is_delivery_successful")

        livemode = d.pop("livemode")

        request = WebhookRequest.from_dict(d.pop("request"))

        response = WebhookResponse.from_dict(d.pop("response"))

        webhook_attempt = cls(
            created_at=created_at,
            delivery_attempt=delivery_attempt,
            id=id,
            is_delivery_successful=is_delivery_successful,
            livemode=livemode,
            request=request,
            response=response,
        )

        return webhook_attempt
