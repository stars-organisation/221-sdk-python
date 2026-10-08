from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.webhook_event import WebhookEvent


T = TypeVar("T", bound="WebhookEventList")


@_attrs_define
class WebhookEventList:
    """
    Attributes:
        events (list[WebhookEvent]):
        livemode (bool): true : objet du mode live ; false : mode test.
        total_count (int):
    """

    events: list[WebhookEvent]
    livemode: bool
    total_count: int

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        livemode = self.livemode

        total_count = self.total_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "livemode": livemode,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_event import WebhookEvent

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = WebhookEvent.from_dict(events_item_data)

            events.append(events_item)

        livemode = d.pop("livemode")

        total_count = d.pop("total_count")

        webhook_event_list = cls(
            events=events,
            livemode=livemode,
            total_count=total_count,
        )

        return webhook_event_list
