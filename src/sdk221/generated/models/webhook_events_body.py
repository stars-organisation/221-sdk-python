from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEventsBody")


@_attrs_define
class WebhookEventsBody:
    """
    Attributes:
        events (list[str] | None | Unset): Types d’événements reçus (GET /v1/webhook-event-types).
        modes (list[str] | None | Unset): Modes reçus : test, live, ou les deux.
    """

    events: list[str] | None | Unset = UNSET
    modes: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        events: list[str] | None | Unset
        if isinstance(self.events, Unset):
            events = UNSET
        elif isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        modes: list[str] | None | Unset
        if isinstance(self.modes, Unset):
            modes = UNSET
        elif isinstance(self.modes, list):
            modes = self.modes

        else:
            modes = self.modes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if events is not UNSET:
            field_dict["events"] = events
        if modes is not UNSET:
            field_dict["modes"] = modes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        def _parse_modes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modes_type_0 = cast(list[str], data)

                return modes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        modes = _parse_modes(d.pop("modes", UNSET))

        webhook_events_body = cls(
            events=events,
            modes=modes,
        )

        return webhook_events_body
