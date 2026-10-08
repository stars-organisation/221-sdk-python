from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="RailFeeExample")


@_attrs_define
class RailFeeExample:
    """
    Attributes:
        amount (str): Montant de l'exemple : 10000 XOF.
        collection_fee (None | str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        refund_fee (None | str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        withdrawal_fee (None | str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
    """

    amount: str
    collection_fee: None | str
    refund_fee: None | str
    withdrawal_fee: None | str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        collection_fee: None | str
        collection_fee = self.collection_fee

        refund_fee: None | str
        refund_fee = self.refund_fee

        withdrawal_fee: None | str
        withdrawal_fee = self.withdrawal_fee

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "collection_fee": collection_fee,
                "refund_fee": refund_fee,
                "withdrawal_fee": withdrawal_fee,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        def _parse_collection_fee(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        collection_fee = _parse_collection_fee(d.pop("collection_fee"))

        def _parse_refund_fee(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        refund_fee = _parse_refund_fee(d.pop("refund_fee"))

        def _parse_withdrawal_fee(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        withdrawal_fee = _parse_withdrawal_fee(d.pop("withdrawal_fee"))

        rail_fee_example = cls(
            amount=amount,
            collection_fee=collection_fee,
            refund_fee=refund_fee,
            withdrawal_fee=withdrawal_fee,
        )

        return rail_fee_example
