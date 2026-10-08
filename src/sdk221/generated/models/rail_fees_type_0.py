from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.rail_fee_example import RailFeeExample


T = TypeVar("T", bound="RailFeesType0")


@_attrs_define
class RailFeesType0:
    """
    Attributes:
        collection_bps (int | None): Part des frais d'encaissement en points de base (100 = 1 %) ; null sans tarif en
            vigueur.
        example_10000 (RailFeeExample):
        refund_bps (int | None):
        withdrawal_bps (int | None):
    """

    collection_bps: int | None
    example_10000: RailFeeExample
    refund_bps: int | None
    withdrawal_bps: int | None

    def to_dict(self) -> dict[str, Any]:
        collection_bps: int | None
        collection_bps = self.collection_bps

        example_10000 = self.example_10000.to_dict()

        refund_bps: int | None
        refund_bps = self.refund_bps

        withdrawal_bps: int | None
        withdrawal_bps = self.withdrawal_bps

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collection_bps": collection_bps,
                "example_10000": example_10000,
                "refund_bps": refund_bps,
                "withdrawal_bps": withdrawal_bps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rail_fee_example import RailFeeExample

        d = dict(src_dict)

        def _parse_collection_bps(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        collection_bps = _parse_collection_bps(d.pop("collection_bps"))

        example_10000 = RailFeeExample.from_dict(d.pop("example_10000"))

        def _parse_refund_bps(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        refund_bps = _parse_refund_bps(d.pop("refund_bps"))

        def _parse_withdrawal_bps(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        withdrawal_bps = _parse_withdrawal_bps(d.pop("withdrawal_bps"))

        rail_fees_type_0 = cls(
            collection_bps=collection_bps,
            example_10000=example_10000,
            refund_bps=refund_bps,
            withdrawal_bps=withdrawal_bps,
        )

        return rail_fees_type_0
