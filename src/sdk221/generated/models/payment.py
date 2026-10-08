from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payment_currency import PaymentCurrency
from ..models.payment_method import PaymentMethod
from ..models.payment_rail import PaymentRail
from ..models.payment_status import PaymentStatus
from ..models.payment_withdrawal_eligibility import PaymentWithdrawalEligibility
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.next_action_type_0 import NextActionType0


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """
    Attributes:
        amount (str): Montant à payer, remise déduite.
        checkout_url (None | str): Page de paiement ; null quand l'opérateur ne donne qu'un QR code ou une consigne
            (voir next_action).
        created_at (datetime.datetime):
        currency (PaymentCurrency):
        fee (None | str): Frais totaux ; null tant que le paiement n'est pas confirmé.
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        merchant_reference (str):
        net (None | str): Montant crédité au marchand ; null tant que le paiement n'est pas confirmé.
        next_action (NextActionType0 | None):
        rail (PaymentRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
        status (PaymentStatus):
        withdrawal_eligibility (PaymentWithdrawalEligibility): confirmed : l'argent est retirable.
        discount_amount (str | Unset): Remise accordée, avec offer_code.
        method (PaymentMethod | Unset): Présent seulement pour sn_wave et sn_orange. Utilisez rail.
        offer_code (str | Unset): Présent si un code promo a été appliqué.
        original_amount (None | str | Unset): Montant avant remise, avec offer_code.
    """

    amount: str
    checkout_url: None | str
    created_at: datetime.datetime
    currency: PaymentCurrency
    fee: None | str
    id: UUID
    livemode: bool
    merchant_reference: str
    net: None | str
    next_action: NextActionType0 | None
    rail: PaymentRail
    status: PaymentStatus
    withdrawal_eligibility: PaymentWithdrawalEligibility
    discount_amount: str | Unset = UNSET
    method: PaymentMethod | Unset = UNSET
    offer_code: str | Unset = UNSET
    original_amount: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.next_action_type_0 import NextActionType0

        amount = self.amount

        checkout_url: None | str
        checkout_url = self.checkout_url

        created_at = self.created_at.isoformat()

        currency = self.currency.value

        fee: None | str
        fee = self.fee

        id = str(self.id)

        livemode = self.livemode

        merchant_reference = self.merchant_reference

        net: None | str
        net = self.net

        next_action: dict[str, Any] | None
        if isinstance(self.next_action, NextActionType0):
            next_action = self.next_action.to_dict()
        else:
            next_action = self.next_action

        rail = self.rail.value

        status = self.status.value

        withdrawal_eligibility = self.withdrawal_eligibility.value

        discount_amount = self.discount_amount

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        offer_code = self.offer_code

        original_amount: None | str | Unset
        if isinstance(self.original_amount, Unset):
            original_amount = UNSET
        else:
            original_amount = self.original_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "checkout_url": checkout_url,
                "created_at": created_at,
                "currency": currency,
                "fee": fee,
                "id": id,
                "livemode": livemode,
                "merchant_reference": merchant_reference,
                "net": net,
                "next_action": next_action,
                "rail": rail,
                "status": status,
                "withdrawal_eligibility": withdrawal_eligibility,
            }
        )
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if method is not UNSET:
            field_dict["method"] = method
        if offer_code is not UNSET:
            field_dict["offer_code"] = offer_code
        if original_amount is not UNSET:
            field_dict["original_amount"] = original_amount

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.next_action_type_0 import NextActionType0

        d = dict(src_dict)
        amount = d.pop("amount")

        def _parse_checkout_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checkout_url = _parse_checkout_url(d.pop("checkout_url"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = PaymentCurrency(d.pop("currency"))

        def _parse_fee(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fee = _parse_fee(d.pop("fee"))

        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        merchant_reference = d.pop("merchant_reference")

        def _parse_net(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        net = _parse_net(d.pop("net"))

        def _parse_next_action(data: object) -> NextActionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_next_action_type_0 = NextActionType0.from_dict(data)

                return componentsschemas_next_action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NextActionType0 | None, data)

        next_action = _parse_next_action(d.pop("next_action"))

        rail = PaymentRail(d.pop("rail"))

        status = PaymentStatus(d.pop("status"))

        withdrawal_eligibility = PaymentWithdrawalEligibility(
            d.pop("withdrawal_eligibility")
        )

        discount_amount = d.pop("discount_amount", UNSET)

        _method = d.pop("method", UNSET)
        method: PaymentMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = PaymentMethod(_method)

        offer_code = d.pop("offer_code", UNSET)

        def _parse_original_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_amount = _parse_original_amount(d.pop("original_amount", UNSET))

        payment = cls(
            amount=amount,
            checkout_url=checkout_url,
            created_at=created_at,
            currency=currency,
            fee=fee,
            id=id,
            livemode=livemode,
            merchant_reference=merchant_reference,
            net=net,
            next_action=next_action,
            rail=rail,
            status=status,
            withdrawal_eligibility=withdrawal_eligibility,
            discount_amount=discount_amount,
            method=method,
            offer_code=offer_code,
            original_amount=original_amount,
        )

        return payment
