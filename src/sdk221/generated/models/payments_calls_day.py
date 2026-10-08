from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PaymentsCallsDay")


@_attrs_define
class PaymentsCallsDay:
    """
    Attributes:
        count (int):
        day (str): Jour UTC, AAAA-MM-JJ.
    """

    count: int
    day: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        day = self.day

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "day": day,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        count = d.pop("count")

        day = d.pop("day")

        payments_calls_day = cls(
            count=count,
            day=day,
        )

        return payments_calls_day
