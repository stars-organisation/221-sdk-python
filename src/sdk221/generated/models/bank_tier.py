from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="BankTier")


@_attrs_define
class BankTier:
    """
    Attributes:
        bps (int): Taux appliqué au montant entier, en points de base.
        from_ (int):
        to (int):
    """

    bps: int
    from_: int
    to: int

    def to_dict(self) -> dict[str, Any]:
        bps = self.bps

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bps": bps,
                "from": from_,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bps = d.pop("bps")

        from_ = d.pop("from")

        to = d.pop("to")

        bank_tier = cls(
            bps=bps,
            from_=from_,
            to=to,
        )

        return bank_tier
