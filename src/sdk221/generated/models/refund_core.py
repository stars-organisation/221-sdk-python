from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.refund_core_currency import RefundCoreCurrency
from ..models.refund_core_fee_payer import RefundCoreFeePayer
from ..models.refund_core_reason import RefundCoreReason
from ..models.refund_core_status import RefundCoreStatus

T = TypeVar("T", bound="RefundCore")


@_attrs_define
class RefundCore:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        created_at (datetime.datetime):
        currency (RefundCoreCurrency):
        customer_receives (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        fee_payer (RefundCoreFeePayer):
        merchant_debited (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        payment_id (UUID):
        reason (RefundCoreReason):
        refund_id (UUID):
        status (RefundCoreStatus):
        updated_at (datetime.datetime):
    """

    amount: str
    created_at: datetime.datetime
    currency: RefundCoreCurrency
    customer_receives: str
    fee: str
    fee_payer: RefundCoreFeePayer
    merchant_debited: str
    payment_id: UUID
    reason: RefundCoreReason
    refund_id: UUID
    status: RefundCoreStatus
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at.isoformat()

        currency = self.currency.value

        customer_receives = self.customer_receives

        fee = self.fee

        fee_payer = self.fee_payer.value

        merchant_debited = self.merchant_debited

        payment_id = str(self.payment_id)

        reason = self.reason.value

        refund_id = str(self.refund_id)

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "created_at": created_at,
                "currency": currency,
                "customer_receives": customer_receives,
                "fee": fee,
                "fee_payer": fee_payer,
                "merchant_debited": merchant_debited,
                "payment_id": payment_id,
                "reason": reason,
                "refund_id": refund_id,
                "status": status,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = RefundCoreCurrency(d.pop("currency"))

        customer_receives = d.pop("customer_receives")

        fee = d.pop("fee")

        fee_payer = RefundCoreFeePayer(d.pop("fee_payer"))

        merchant_debited = d.pop("merchant_debited")

        payment_id = UUID(d.pop("payment_id"))

        reason = RefundCoreReason(d.pop("reason"))

        refund_id = UUID(d.pop("refund_id"))

        status = RefundCoreStatus(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        refund_core = cls(
            amount=amount,
            created_at=created_at,
            currency=currency,
            customer_receives=customer_receives,
            fee=fee,
            fee_payer=fee_payer,
            merchant_debited=merchant_debited,
            payment_id=payment_id,
            reason=reason,
            refund_id=refund_id,
            status=status,
            updated_at=updated_at,
        )

        return refund_core
