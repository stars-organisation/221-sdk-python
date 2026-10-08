from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_destination_rail import PayoutDestinationRail

T = TypeVar("T", bound="PayoutDestination")


@_attrs_define
class PayoutDestination:
    """
    Attributes:
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        phone_last_digits (str):
        rail (PayoutDestinationRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
        verified (bool):
    """

    id: UUID
    livemode: bool
    phone_last_digits: str
    rail: PayoutDestinationRail
    verified: bool

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        livemode = self.livemode

        phone_last_digits = self.phone_last_digits

        rail = self.rail.value

        verified = self.verified

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "livemode": livemode,
                "phone_last_digits": phone_last_digits,
                "rail": rail,
                "verified": verified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        phone_last_digits = d.pop("phone_last_digits")

        rail = PayoutDestinationRail(d.pop("rail"))

        verified = d.pop("verified")

        payout_destination = cls(
            id=id,
            livemode=livemode,
            phone_last_digits=phone_last_digits,
            rail=rail,
            verified=verified,
        )

        return payout_destination
