from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_quote_request_rail import PayoutQuoteRequestRail

T = TypeVar("T", bound="PayoutQuoteRequest")


@_attrs_define
class PayoutQuoteRequest:
    """
    Attributes:
        amount (str): Montant débité du solde disponible, frais compris.
        destination_id (UUID): Numéro enregistré par POST /v1/payout-destinations, sur le même moyen de paiement.
        rail (PayoutQuoteRequestRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
    """

    amount: str
    destination_id: UUID
    rail: PayoutQuoteRequestRail

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        destination_id = str(self.destination_id)

        rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "destination_id": destination_id,
                "rail": rail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        destination_id = UUID(d.pop("destination_id"))

        rail = PayoutQuoteRequestRail(d.pop("rail"))

        payout_quote_request = cls(
            amount=amount,
            destination_id=destination_id,
            rail=rail,
        )

        return payout_quote_request
