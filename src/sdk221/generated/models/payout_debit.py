from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_debit_rail import PayoutDebitRail

T = TypeVar("T", bound="PayoutDebit")


@_attrs_define
class PayoutDebit:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        rail (PayoutDebitRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
    """

    amount: str
    rail: PayoutDebitRail

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "rail": rail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        rail = PayoutDebitRail(d.pop("rail"))

        payout_debit = cls(
            amount=amount,
            rail=rail,
        )

        return payout_debit
