from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="ModeLive")


@_attrs_define
class ModeLive:
    """
    Attributes:
        live_enabled (bool):
    """

    live_enabled: bool

    def to_dict(self) -> dict[str, Any]:
        live_enabled = self.live_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "live_enabled": live_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        live_enabled = d.pop("live_enabled")

        mode_live = cls(
            live_enabled=live_enabled,
        )

        return mode_live
