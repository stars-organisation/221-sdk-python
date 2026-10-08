from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivationLiveBody")


@_attrs_define
class ActivationLiveBody:
    """
    Attributes:
        live_enabled (bool):
        acknowledged (bool | Unset): Obligatoire pour activer : confirme que les clés live déplacent de l'argent réel.
    """

    live_enabled: bool
    acknowledged: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        live_enabled = self.live_enabled

        acknowledged = self.acknowledged

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "live_enabled": live_enabled,
            }
        )
        if acknowledged is not UNSET:
            field_dict["acknowledged"] = acknowledged

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        live_enabled = d.pop("live_enabled")

        acknowledged = d.pop("acknowledged", UNSET)

        activation_live_body = cls(
            live_enabled=live_enabled,
            acknowledged=acknowledged,
        )

        return activation_live_body
