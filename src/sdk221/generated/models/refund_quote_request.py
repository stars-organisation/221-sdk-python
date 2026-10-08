from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.refund_quote_request_fee_payer import RefundQuoteRequestFeePayer
from ..types import UNSET, Unset

T = TypeVar("T", bound="RefundQuoteRequest")


@_attrs_define
class RefundQuoteRequest:
    """
    Attributes:
        amount (str): Montant à rembourser, au plus le reste remboursable du paiement.
        payment_id (UUID):
        fee_payer (RefundQuoteRequestFeePayer | Unset): Qui supporte les frais ; par défaut refund_fee_payer_default du
            projet.
    """

    amount: str
    payment_id: UUID
    fee_payer: RefundQuoteRequestFeePayer | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        payment_id = str(self.payment_id)

        fee_payer: str | Unset = UNSET
        if not isinstance(self.fee_payer, Unset):
            fee_payer = self.fee_payer.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "payment_id": payment_id,
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

        _fee_payer = d.pop("fee_payer", UNSET)
        fee_payer: RefundQuoteRequestFeePayer | Unset
        if isinstance(_fee_payer, Unset):
            fee_payer = UNSET
        else:
            fee_payer = RefundQuoteRequestFeePayer(_fee_payer)

        refund_quote_request = cls(
            amount=amount,
            payment_id=payment_id,
            fee_payer=fee_payer,
        )

        return refund_quote_request
