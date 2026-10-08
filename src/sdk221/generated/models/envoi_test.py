from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvoiTest")


@_attrs_define
class EnvoiTest:
    """
    Attributes:
        delivered (bool): true si le récepteur a répondu 2xx.
        event (str):
        livemode (bool): true si le point de terminaison ne reçoit que le mode live.
        status (int | None): Code HTTP du récepteur ; null s'il n'a pas répondu.
        error (str | Unset): Cause technique quand le récepteur n'a pas répondu.
    """

    delivered: bool
    event: str
    livemode: bool
    status: int | None
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        delivered = self.delivered

        event = self.event

        livemode = self.livemode

        status: int | None
        status = self.status

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delivered": delivered,
                "event": event,
                "livemode": livemode,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delivered = d.pop("delivered")

        event = d.pop("event")

        livemode = d.pop("livemode")

        def _parse_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status = _parse_status(d.pop("status"))

        error = d.pop("error", UNSET)

        envoi_test = cls(
            delivered=delivered,
            event=event,
            livemode=livemode,
            status=status,
            error=error,
        )

        return envoi_test
