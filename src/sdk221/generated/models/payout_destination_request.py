from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_destination_request_rail import PayoutDestinationRequestRail
from ..models.payout_destination_request_type import PayoutDestinationRequestType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PayoutDestinationRequest")


@_attrs_define
class PayoutDestinationRequest:
    """
    Attributes:
        holder_name (str | Unset): Titulaire du compte : 2 à 70 caractères, lettres, espaces, apostrophe, tiret et
            point. EN: account holder, 2 to 70 characters.
        phone (str | Unset): Numéro mobile valide pour le pays du moyen de paiement.
        rail (PayoutDestinationRequestRail | Unset): Moyen de paiement : pays et opérateur (liste et état : GET
            /v1/rails).
        rib (str | Unset): RIB UEMOA de 24 caractères, espaces acceptés : code banque (2 lettres, 3 chiffres), guichet
            (5 chiffres), compte (12), clé (2 chiffres) vérifiée. EN: 24-character UEMOA RIB, spaces accepted; the key is
            checked.
        type_ (PayoutDestinationRequestType | Unset): mobile par défaut : rail et phone ; bank : rib et holder_name.
    """

    holder_name: str | Unset = UNSET
    phone: str | Unset = UNSET
    rail: PayoutDestinationRequestRail | Unset = UNSET
    rib: str | Unset = UNSET
    type_: PayoutDestinationRequestType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        holder_name = self.holder_name

        phone = self.phone

        rail: str | Unset = UNSET
        if not isinstance(self.rail, Unset):
            rail = self.rail.value

        rib = self.rib

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if holder_name is not UNSET:
            field_dict["holder_name"] = holder_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if rail is not UNSET:
            field_dict["rail"] = rail
        if rib is not UNSET:
            field_dict["rib"] = rib
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        holder_name = d.pop("holder_name", UNSET)

        phone = d.pop("phone", UNSET)

        _rail = d.pop("rail", UNSET)
        rail: PayoutDestinationRequestRail | Unset
        if isinstance(_rail, Unset):
            rail = UNSET
        else:
            rail = PayoutDestinationRequestRail(_rail)

        rib = d.pop("rib", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PayoutDestinationRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PayoutDestinationRequestType(_type_)

        payout_destination_request = cls(
            holder_name=holder_name,
            phone=phone,
            rail=rail,
            rib=rib,
            type_=type_,
        )

        return payout_destination_request
