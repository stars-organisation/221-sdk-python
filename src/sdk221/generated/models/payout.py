from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_destination_type import PayoutDestinationType
from ..models.payout_failure_reason import PayoutFailureReason
from ..models.payout_rail import PayoutRail
from ..types import UNSET, Unset

T = TypeVar("T", bound="Payout")


@_attrs_define
class Payout:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        created_at (datetime.datetime):
        destination_id (UUID):
        destination_type (PayoutDestinationType): mobile : vers un numéro ; bank : virement bancaire, processing pendant
            3 à 5 jours ouvrés.
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        net (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        status (str): État du retrait ; not_sent quand il a été refusé avant envoi. Pas une liste fermée : interrogez
            GET /v1/payouts/{id} jusqu'à un état final.
        failure_reason (PayoutFailureReason | Unset): Retrait refusé par l'opérateur : plafond du destinataire atteint,
            numéro ou compte invalide, ou indisponibilité. Aucun frais, le montant entier revient au solde. EN: why the
            operator refused the payout; no fee is charged and the whole amount returns to the balance.
        rail (PayoutRail | Unset): Numéro mobile seulement.
        release_at (datetime.datetime | Unset): Retrait en file : le numéro vient d'être vérifié, l'envoi part à partir
            de cette date.
    """

    amount: str
    created_at: datetime.datetime
    destination_id: UUID
    destination_type: PayoutDestinationType
    fee: str
    id: UUID
    livemode: bool
    net: str
    status: str
    failure_reason: PayoutFailureReason | Unset = UNSET
    rail: PayoutRail | Unset = UNSET
    release_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at.isoformat()

        destination_id = str(self.destination_id)

        destination_type = self.destination_type.value

        fee = self.fee

        id = str(self.id)

        livemode = self.livemode

        net = self.net

        status = self.status

        failure_reason: str | Unset = UNSET
        if not isinstance(self.failure_reason, Unset):
            failure_reason = self.failure_reason.value

        rail: str | Unset = UNSET
        if not isinstance(self.rail, Unset):
            rail = self.rail.value

        release_at: str | Unset = UNSET
        if not isinstance(self.release_at, Unset):
            release_at = self.release_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "created_at": created_at,
                "destination_id": destination_id,
                "destination_type": destination_type,
                "fee": fee,
                "id": id,
                "livemode": livemode,
                "net": net,
                "status": status,
            }
        )
        if failure_reason is not UNSET:
            field_dict["failure_reason"] = failure_reason
        if rail is not UNSET:
            field_dict["rail"] = rail
        if release_at is not UNSET:
            field_dict["release_at"] = release_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        destination_id = UUID(d.pop("destination_id"))

        destination_type = PayoutDestinationType(d.pop("destination_type"))

        fee = d.pop("fee")

        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        net = d.pop("net")

        status = d.pop("status")

        _failure_reason = d.pop("failure_reason", UNSET)
        failure_reason: PayoutFailureReason | Unset
        if isinstance(_failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = PayoutFailureReason(_failure_reason)

        _rail = d.pop("rail", UNSET)
        rail: PayoutRail | Unset
        if isinstance(_rail, Unset):
            rail = UNSET
        else:
            rail = PayoutRail(_rail)

        _release_at = d.pop("release_at", UNSET)
        release_at: datetime.datetime | Unset
        if isinstance(_release_at, Unset):
            release_at = UNSET
        else:
            release_at = datetime.datetime.fromisoformat(_release_at)

        payout = cls(
            amount=amount,
            created_at=created_at,
            destination_id=destination_id,
            destination_type=destination_type,
            fee=fee,
            id=id,
            livemode=livemode,
            net=net,
            status=status,
            failure_reason=failure_reason,
            rail=rail,
            release_at=release_at,
        )

        return payout
