from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_destination_request_rail import PayoutDestinationRequestRail

T = TypeVar("T", bound="PayoutDestinationRequest")


@_attrs_define
class PayoutDestinationRequest:
    """
    Attributes:
        phone (str): Numéro mobile valide pour le pays du moyen de paiement.
        rail (PayoutDestinationRequestRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
    """

    phone: str
    rail: PayoutDestinationRequestRail

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "phone": phone,
                "rail": rail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        phone = d.pop("phone")

        rail = PayoutDestinationRequestRail(d.pop("rail"))

        payout_destination_request = cls(
            phone=phone,
            rail=rail,
        )

        return payout_destination_request
