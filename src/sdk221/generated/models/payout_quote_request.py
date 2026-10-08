from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_quote_request_rail import PayoutQuoteRequestRail
from ..types import UNSET, Unset

T = TypeVar("T", bound="PayoutQuoteRequest")


@_attrs_define
class PayoutQuoteRequest:
    """
    Attributes:
        amount (str): Montant débité du solde disponible, frais compris.
        destination_id (UUID): Numéro ou compte enregistré par POST /v1/payout-destinations, sur le même moyen de
            paiement.
        rail (PayoutQuoteRequestRail | Unset): Requis pour un numéro mobile ; absent pour un compte bancaire.
    """

    amount: str
    destination_id: UUID
    rail: PayoutQuoteRequestRail | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        destination_id = str(self.destination_id)

        rail: str | Unset = UNSET
        if not isinstance(self.rail, Unset):
            rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "destination_id": destination_id,
            }
        )
        if rail is not UNSET:
            field_dict["rail"] = rail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        destination_id = UUID(d.pop("destination_id"))

        _rail = d.pop("rail", UNSET)
        rail: PayoutQuoteRequestRail | Unset
        if isinstance(_rail, Unset):
            rail = UNSET
        else:
            rail = PayoutQuoteRequestRail(_rail)

        payout_quote_request = cls(
            amount=amount,
            destination_id=destination_id,
            rail=rail,
        )

        return payout_quote_request
