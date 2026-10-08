from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.webhook_event_event_class import WebhookEventEventClass

T = TypeVar("T", bound="WebhookEvent")


@_attrs_define
class WebhookEvent:
    """
    Attributes:
        created_at (datetime.datetime):
        event_class (WebhookEventEventClass):
        id (str):
        initial_attempt_id (None | str):
        is_delivery_successful (bool):
        merchant_id (str):
        object_id (None | str): Identifiant du paiement, retrait, remboursement ou litige concerné.
        type_ (str): Liste : GET /v1/webhook-event-types.
    """

    created_at: datetime.datetime
    event_class: WebhookEventEventClass
    id: str
    initial_attempt_id: None | str
    is_delivery_successful: bool
    merchant_id: str
    object_id: None | str
    type_: str

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        event_class = self.event_class.value

        id = self.id

        initial_attempt_id: None | str
        initial_attempt_id = self.initial_attempt_id

        is_delivery_successful = self.is_delivery_successful

        merchant_id = self.merchant_id

        object_id: None | str
        object_id = self.object_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "event_class": event_class,
                "id": id,
                "initial_attempt_id": initial_attempt_id,
                "is_delivery_successful": is_delivery_successful,
                "merchant_id": merchant_id,
                "object_id": object_id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        event_class = WebhookEventEventClass(d.pop("event_class"))

        id = d.pop("id")

        def _parse_initial_attempt_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        initial_attempt_id = _parse_initial_attempt_id(d.pop("initial_attempt_id"))

        is_delivery_successful = d.pop("is_delivery_successful")

        merchant_id = d.pop("merchant_id")

        def _parse_object_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        object_id = _parse_object_id(d.pop("object_id"))

        type_ = d.pop("type")

        webhook_event = cls(
            created_at=created_at,
            event_class=event_class,
            id=id,
            initial_attempt_id=initial_attempt_id,
            is_delivery_successful=is_delivery_successful,
            merchant_id=merchant_id,
            object_id=object_id,
            type_=type_,
        )

        return webhook_event
