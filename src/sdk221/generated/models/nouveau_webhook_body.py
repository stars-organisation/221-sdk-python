from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NouveauWebhookBody")


@_attrs_define
class NouveauWebhookBody:
    """
    Attributes:
        url (str):
        events (list[str] | None | Unset): Types d’événements reçus (GET /v1/webhook-event-types) ; par défaut
            dataset.updated.
    """

    url: str
    events: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events: list[str] | None | Unset
        if isinstance(self.events, Unset):
            events = UNSET
        elif isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        def _parse_events(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = cast(list[str], data)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        events = _parse_events(d.pop("events", UNSET))

        nouveau_webhook_body = cls(
            url=url,
            events=events,
        )

        return nouveau_webhook_body
