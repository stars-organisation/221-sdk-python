from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.dispute_request_reason import DisputeRequestReason

T = TypeVar("T", bound="DisputeRequest")


@_attrs_define
class DisputeRequest:
    """
    Attributes:
        amount (str): Au plus le montant du paiement.
        payment_id (UUID): Paiement confirmé du projet.
        reason (DisputeRequestReason):
    """

    amount: str
    payment_id: UUID
    reason: DisputeRequestReason

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        payment_id = str(self.payment_id)

        reason = self.reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "payment_id": payment_id,
                "reason": reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        payment_id = UUID(d.pop("payment_id"))

        reason = DisputeRequestReason(d.pop("reason"))

        dispute_request = cls(
            amount=amount,
            payment_id=payment_id,
            reason=reason,
        )

        return dispute_request
