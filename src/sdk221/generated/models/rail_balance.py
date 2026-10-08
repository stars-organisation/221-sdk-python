from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="RailBalance")


@_attrs_define
class RailBalance:
    """
    Attributes:
        available (str): Retirable.
        pending (str): Encaissé, pas encore retirable.
        reserved (str): Retenu par des retraits en cours.
    """

    available: str
    pending: str
    reserved: str

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        pending = self.pending

        reserved = self.reserved

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available": available,
                "pending": pending,
                "reserved": reserved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available = d.pop("available")

        pending = d.pop("pending")

        reserved = d.pop("reserved")

        rail_balance = cls(
            available=available,
            pending=pending,
            reserved=reserved,
        )

        return rail_balance
