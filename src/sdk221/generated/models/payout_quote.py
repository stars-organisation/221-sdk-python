from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_quote_rail import PayoutQuoteRail

T = TypeVar("T", bound="PayoutQuote")


@_attrs_define
class PayoutQuote:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        destination_id (UUID):
        expires_at (datetime.datetime):
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        livemode (bool): true : objet du mode live ; false : mode test.
        net (str): Montant reçu sur le numéro.
        quote_hash (str): À renvoyer dans POST /v1/payouts : à usage unique, valable jusqu'à expires_at.
        rail (PayoutQuoteRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
    """

    amount: str
    destination_id: UUID
    expires_at: datetime.datetime
    fee: str
    livemode: bool
    net: str
    quote_hash: str
    rail: PayoutQuoteRail

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        destination_id = str(self.destination_id)

        expires_at = self.expires_at.isoformat()

        fee = self.fee

        livemode = self.livemode

        net = self.net

        quote_hash = self.quote_hash

        rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "destination_id": destination_id,
                "expires_at": expires_at,
                "fee": fee,
                "livemode": livemode,
                "net": net,
                "quote_hash": quote_hash,
                "rail": rail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        destination_id = UUID(d.pop("destination_id"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        fee = d.pop("fee")

        livemode = d.pop("livemode")

        net = d.pop("net")

        quote_hash = d.pop("quote_hash")

        rail = PayoutQuoteRail(d.pop("rail"))

        payout_quote = cls(
            amount=amount,
            destination_id=destination_id,
            expires_at=expires_at,
            fee=fee,
            livemode=livemode,
            net=net,
            quote_hash=quote_hash,
            rail=rail,
        )

        return payout_quote
