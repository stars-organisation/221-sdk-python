from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.montant_currency import MontantCurrency

T = TypeVar("T", bound="Montant")


@_attrs_define
class Montant:
    """
    Attributes:
        amount (int):
        currency (MontantCurrency):
        eur (float):
        eur_parity (float):
        formatted (str):
        words (str):
    """

    amount: int
    currency: MontantCurrency
    eur: float
    eur_parity: float
    formatted: str
    words: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency.value

        eur = self.eur

        eur_parity = self.eur_parity

        formatted = self.formatted

        words = self.words

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
                "eur": eur,
                "eur_parity": eur_parity,
                "formatted": formatted,
                "words": words,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = MontantCurrency(d.pop("currency"))

        eur = d.pop("eur")

        eur_parity = d.pop("eur_parity")

        formatted = d.pop("formatted")

        words = d.pop("words")

        montant = cls(
            amount=amount,
            currency=currency,
            eur=eur,
            eur_parity=eur_parity,
            formatted=formatted,
            words=words,
        )

        return montant
