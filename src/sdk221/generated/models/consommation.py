from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Consommation")


@_attrs_define
class Consommation:
    """
    Attributes:
        count (int):
        day (str):
        key_id (str):
    """

    count: int
    day: str
    key_id: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        day = self.day

        key_id = self.key_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "day": day,
                "key_id": key_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        day = d.pop("day")

        key_id = d.pop("key_id")

        consommation = cls(
            count=count,
            day=day,
            key_id=key_id,
        )

        return consommation
