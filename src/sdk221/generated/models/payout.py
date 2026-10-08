from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_rail import PayoutRail

T = TypeVar("T", bound="Payout")


@_attrs_define
class Payout:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        created_at (datetime.datetime):
        destination_id (UUID):
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        net (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        rail (PayoutRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
        status (str): État du retrait ; not_sent quand il a été refusé avant envoi. Pas une liste fermée : interrogez
            GET /v1/payouts/{id} jusqu'à un état final.
    """

    amount: str
    created_at: datetime.datetime
    destination_id: UUID
    fee: str
    id: UUID
    livemode: bool
    net: str
    rail: PayoutRail
    status: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at.isoformat()

        destination_id = str(self.destination_id)

        fee = self.fee

        id = str(self.id)

        livemode = self.livemode

        net = self.net

        rail = self.rail.value

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "created_at": created_at,
                "destination_id": destination_id,
                "fee": fee,
                "id": id,
                "livemode": livemode,
                "net": net,
                "rail": rail,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        destination_id = UUID(d.pop("destination_id"))

        fee = d.pop("fee")

        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        net = d.pop("net")

        rail = PayoutRail(d.pop("rail"))

        status = d.pop("status")

        payout = cls(
            amount=amount,
            created_at=created_at,
            destination_id=destination_id,
            fee=fee,
            id=id,
            livemode=livemode,
            net=net,
            rail=rail,
            status=status,
        )

        return payout
