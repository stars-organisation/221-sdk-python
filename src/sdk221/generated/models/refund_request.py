from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.refund_request_fee_payer import RefundRequestFeePayer
from ..models.refund_request_reason import RefundRequestReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="RefundRequest")


@_attrs_define
class RefundRequest:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        payment_id (UUID):
        quote_hash (str):
        reason (RefundRequestReason):
        fee_payer (RefundRequestFeePayer | Unset): Doit être celui de la cotation.
    """

    amount: str
    payment_id: UUID
    quote_hash: str
    reason: RefundRequestReason
    fee_payer: RefundRequestFeePayer | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        payment_id = str(self.payment_id)

        quote_hash = self.quote_hash

        reason = self.reason.value

        fee_payer: str | Unset = UNSET
        if not isinstance(self.fee_payer, Unset):
            fee_payer = self.fee_payer.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "payment_id": payment_id,
                "quote_hash": quote_hash,
                "reason": reason,
            }
        )
        if fee_payer is not UNSET:
            field_dict["fee_payer"] = fee_payer

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        payment_id = UUID(d.pop("payment_id"))

        quote_hash = d.pop("quote_hash")

        reason = RefundRequestReason(d.pop("reason"))

        _fee_payer = d.pop("fee_payer", UNSET)
        fee_payer: RefundRequestFeePayer | Unset
        if isinstance(_fee_payer, Unset):
            fee_payer = UNSET
        else:
            fee_payer = RefundRequestFeePayer(_fee_payer)

        refund_request = cls(
            amount=amount,
            payment_id=payment_id,
            quote_hash=quote_hash,
            reason=reason,
            fee_payer=fee_payer,
        )

        return refund_request
