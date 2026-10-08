from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.refund_quote_fee_payer import RefundQuoteFeePayer

T = TypeVar("T", bound="RefundQuote")


@_attrs_define
class RefundQuote:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        customer_receives (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        expires_at (datetime.datetime):
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        fee_payer (RefundQuoteFeePayer):
        livemode (bool): true : objet du mode live ; false : mode test.
        merchant_debited (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        payment_id (UUID):
        quote_hash (str): À renvoyer dans POST /v1/refunds : à usage unique, valable jusqu'à expires_at.
    """

    amount: str
    customer_receives: str
    expires_at: datetime.datetime
    fee: str
    fee_payer: RefundQuoteFeePayer
    livemode: bool
    merchant_debited: str
    payment_id: UUID
    quote_hash: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        customer_receives = self.customer_receives

        expires_at = self.expires_at.isoformat()

        fee = self.fee

        fee_payer = self.fee_payer.value

        livemode = self.livemode

        merchant_debited = self.merchant_debited

        payment_id = str(self.payment_id)

        quote_hash = self.quote_hash

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "customer_receives": customer_receives,
                "expires_at": expires_at,
                "fee": fee,
                "fee_payer": fee_payer,
                "livemode": livemode,
                "merchant_debited": merchant_debited,
                "payment_id": payment_id,
                "quote_hash": quote_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        customer_receives = d.pop("customer_receives")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        fee = d.pop("fee")

        fee_payer = RefundQuoteFeePayer(d.pop("fee_payer"))

        livemode = d.pop("livemode")

        merchant_debited = d.pop("merchant_debited")

        payment_id = UUID(d.pop("payment_id"))

        quote_hash = d.pop("quote_hash")

        refund_quote = cls(
            amount=amount,
            customer_receives=customer_receives,
            expires_at=expires_at,
            fee=fee,
            fee_payer=fee_payer,
            livemode=livemode,
            merchant_debited=merchant_debited,
            payment_id=payment_id,
            quote_hash=quote_hash,
        )

        return refund_quote
