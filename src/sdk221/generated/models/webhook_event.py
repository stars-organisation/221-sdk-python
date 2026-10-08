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
        created (datetime.datetime):
        event_class (WebhookEventEventClass):
        event_id (str):
        event_type (str): Liste : GET /v1/webhook-event-types.
        initial_attempt_id (None | str):
        is_delivery_successful (bool):
        merchant_id (str):
        object_id (None | str): Identifiant du paiement, retrait, remboursement ou litige concerné.
        profile_id (str):
    """

    created: datetime.datetime
    event_class: WebhookEventEventClass
    event_id: str
    event_type: str
    initial_attempt_id: None | str
    is_delivery_successful: bool
    merchant_id: str
    object_id: None | str
    profile_id: str

    def to_dict(self) -> dict[str, Any]:
        created = self.created.isoformat()

        event_class = self.event_class.value

        event_id = self.event_id

        event_type = self.event_type

        initial_attempt_id: None | str
        initial_attempt_id = self.initial_attempt_id

        is_delivery_successful = self.is_delivery_successful

        merchant_id = self.merchant_id

        object_id: None | str
        object_id = self.object_id

        profile_id = self.profile_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created": created,
                "event_class": event_class,
                "event_id": event_id,
                "event_type": event_type,
                "initial_attempt_id": initial_attempt_id,
                "is_delivery_successful": is_delivery_successful,
                "merchant_id": merchant_id,
                "object_id": object_id,
                "profile_id": profile_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created = datetime.datetime.fromisoformat(d.pop("created"))

        event_class = WebhookEventEventClass(d.pop("event_class"))

        event_id = d.pop("event_id")

        event_type = d.pop("event_type")

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

        profile_id = d.pop("profile_id")

        webhook_event = cls(
            created=created,
            event_class=event_class,
            event_id=event_id,
            event_type=event_type,
            initial_attempt_id=initial_attempt_id,
            is_delivery_successful=is_delivery_successful,
            merchant_id=merchant_id,
            object_id=object_id,
            profile_id=profile_id,
        )

        return webhook_event
