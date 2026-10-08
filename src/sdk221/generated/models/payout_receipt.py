from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_receipt_destination_type import PayoutReceiptDestinationType
from ..models.payout_receipt_rail import PayoutReceiptRail
from ..types import UNSET, Unset

T = TypeVar("T", bound="PayoutReceipt")


@_attrs_define
class PayoutReceipt:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        destination_last_digits (str): Quatre derniers caractères du numéro ou du RIB crédité.
        destination_type (PayoutReceiptDestinationType):
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        id (UUID): Référence 221 Pay du retrait.
        livemode (bool): true : objet du mode live ; false : mode test.
        net (str): Montant reçu sur le numéro ou le compte.
        rail_label (str): Nom du moyen de paiement (ou « Virement bancaire »), dans la langue de la requête.
        succeeded_at (datetime.datetime): Date de réussite, en UTC : l'heure de Dakar.
        rail (PayoutReceiptRail | Unset): Numéro mobile seulement.
    """

    amount: str
    destination_last_digits: str
    destination_type: PayoutReceiptDestinationType
    fee: str
    id: UUID
    livemode: bool
    net: str
    rail_label: str
    succeeded_at: datetime.datetime
    rail: PayoutReceiptRail | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        destination_last_digits = self.destination_last_digits

        destination_type = self.destination_type.value

        fee = self.fee

        id = str(self.id)

        livemode = self.livemode

        net = self.net

        rail_label = self.rail_label

        succeeded_at = self.succeeded_at.isoformat()

        rail: str | Unset = UNSET
        if not isinstance(self.rail, Unset):
            rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "destination_last_digits": destination_last_digits,
                "destination_type": destination_type,
                "fee": fee,
                "id": id,
                "livemode": livemode,
                "net": net,
                "rail_label": rail_label,
                "succeeded_at": succeeded_at,
            }
        )
        if rail is not UNSET:
            field_dict["rail"] = rail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        destination_last_digits = d.pop("destination_last_digits")

        destination_type = PayoutReceiptDestinationType(d.pop("destination_type"))

        fee = d.pop("fee")

        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        net = d.pop("net")

        rail_label = d.pop("rail_label")

        succeeded_at = datetime.datetime.fromisoformat(d.pop("succeeded_at"))

        _rail = d.pop("rail", UNSET)
        rail: PayoutReceiptRail | Unset
        if isinstance(_rail, Unset):
            rail = UNSET
        else:
            rail = PayoutReceiptRail(_rail)

        payout_receipt = cls(
            amount=amount,
            destination_last_digits=destination_last_digits,
            destination_type=destination_type,
            fee=fee,
            id=id,
            livemode=livemode,
            net=net,
            rail_label=rail_label,
            succeeded_at=succeeded_at,
            rail=rail,
        )

        return payout_receipt
