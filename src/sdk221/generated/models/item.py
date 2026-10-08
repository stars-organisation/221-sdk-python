from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.item_type import ItemType

T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """
    Attributes:
        enabled (bool):
        type_ (ItemType):
    """

    enabled: bool
    type_: ItemType

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        type_ = ItemType(d.pop("type"))

        item = cls(
            enabled=enabled,
            type_=type_,
        )

        return item
