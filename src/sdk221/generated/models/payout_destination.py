from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_destination_rail import PayoutDestinationRail
from ..models.payout_destination_type import PayoutDestinationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.destination_verification import DestinationVerification


T = TypeVar("T", bound="PayoutDestination")


@_attrs_define
class PayoutDestination:
    """
    Attributes:
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        type_ (PayoutDestinationType):
        verified (bool): Vrai une fois le code à 6 chiffres saisi : devis et retraits refusent un numéro non vérifié.
        available_at (datetime.datetime | Unset): Numéro vérifié : un retrait demandé avant cette date (24 h après la
            vérification) attend en file.
        bank_code (str | Unset): Compte bancaire seulement.
        holder_name (str | Unset): Compte bancaire seulement.
        phone_last_digits (str | Unset): Numéro mobile seulement.
        rail (PayoutDestinationRail | Unset): Numéro mobile seulement.
        rib_last4 (str | Unset): Compte bancaire seulement : quatre derniers caractères du RIB.
        verification (DestinationVerification | Unset):
    """

    id: UUID
    livemode: bool
    type_: PayoutDestinationType
    verified: bool
    available_at: datetime.datetime | Unset = UNSET
    bank_code: str | Unset = UNSET
    holder_name: str | Unset = UNSET
    phone_last_digits: str | Unset = UNSET
    rail: PayoutDestinationRail | Unset = UNSET
    rib_last4: str | Unset = UNSET
    verification: DestinationVerification | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        livemode = self.livemode

        type_ = self.type_.value

        verified = self.verified

        available_at: str | Unset = UNSET
        if not isinstance(self.available_at, Unset):
            available_at = self.available_at.isoformat()

        bank_code = self.bank_code

        holder_name = self.holder_name

        phone_last_digits = self.phone_last_digits

        rail: str | Unset = UNSET
        if not isinstance(self.rail, Unset):
            rail = self.rail.value

        rib_last4 = self.rib_last4

        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "livemode": livemode,
                "type": type_,
                "verified": verified,
            }
        )
        if available_at is not UNSET:
            field_dict["available_at"] = available_at
        if bank_code is not UNSET:
            field_dict["bank_code"] = bank_code
        if holder_name is not UNSET:
            field_dict["holder_name"] = holder_name
        if phone_last_digits is not UNSET:
            field_dict["phone_last_digits"] = phone_last_digits
        if rail is not UNSET:
            field_dict["rail"] = rail
        if rib_last4 is not UNSET:
            field_dict["rib_last4"] = rib_last4
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.destination_verification import (
            DestinationVerification,
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        type_ = PayoutDestinationType(d.pop("type"))

        verified = d.pop("verified")

        _available_at = d.pop("available_at", UNSET)
        available_at: datetime.datetime | Unset
        if isinstance(_available_at, Unset):
            available_at = UNSET
        else:
            available_at = datetime.datetime.fromisoformat(_available_at)

        bank_code = d.pop("bank_code", UNSET)

        holder_name = d.pop("holder_name", UNSET)

        phone_last_digits = d.pop("phone_last_digits", UNSET)

        _rail = d.pop("rail", UNSET)
        rail: PayoutDestinationRail | Unset
        if isinstance(_rail, Unset):
            rail = UNSET
        else:
            rail = PayoutDestinationRail(_rail)

        rib_last4 = d.pop("rib_last4", UNSET)

        _verification = d.pop("verification", UNSET)
        verification: DestinationVerification | Unset
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = DestinationVerification.from_dict(_verification)

        payout_destination = cls(
            id=id,
            livemode=livemode,
            type_=type_,
            verified=verified,
            available_at=available_at,
            bank_code=bank_code,
            holder_name=holder_name,
            phone_last_digits=phone_last_digits,
            rail=rail,
            rib_last4=rib_last4,
            verification=verification,
        )

        return payout_destination
