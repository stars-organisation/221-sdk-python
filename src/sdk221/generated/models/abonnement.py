from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Abonnement")


@_attrs_define
class Abonnement:
    """
    Attributes:
        events (list[str] | None):
        id (str):
        local_only (bool): Adresse locale ou privée : livrée en développement seulement, jamais en production.
        modes (list[str] | None): Modes dont le point de terminaison reçoit les événements de paiement : test, live.
        url (str):
        created_at (datetime.datetime | Unset):
    """

    events: list[str] | None
    id: str
    local_only: bool
    modes: list[str] | None
    url: str
    created_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        events: list[str] | None
        if isinstance(self.events, list):
            events = self.events

        else:
            events = self.events

        id = self.id

        local_only = self.local_only

        modes: list[str] | None
        if isinstance(self.modes, list):
            modes = self.modes

        else:
            modes = self.modes

        url = self.url

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "events": events,
                "id": id,
                "local_only": local_only,
                "modes": modes,
                "url": url,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_events(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                events_type_0 = cast(list[str], data)

                return events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        events = _parse_events(d.pop("events"))

        id = d.pop("id")

        local_only = d.pop("local_only")

        def _parse_modes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                modes_type_0 = cast(list[str], data)

                return modes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        modes = _parse_modes(d.pop("modes"))

        url = d.pop("url")

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        abonnement = cls(
            events=events,
            id=id,
            local_only=local_only,
            modes=modes,
            url=url,
            created_at=created_at,
        )

        return abonnement
