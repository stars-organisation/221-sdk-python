from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payment_detail_currency import PaymentDetailCurrency
from ..models.payment_detail_rail import PaymentDetailRail
from ..models.payment_detail_status import PaymentDetailStatus
from ..models.payment_detail_withdrawal_eligibility import (
    PaymentDetailWithdrawalEligibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dispute import Dispute
    from ..models.next_action_type_0 import NextActionType0
    from ..models.payment_attempt import PaymentAttempt
    from ..models.payment_customer import PaymentCustomer
    from ..models.refund_core import RefundCore


T = TypeVar("T", bound="PaymentDetail")


@_attrs_define
class PaymentDetail:
    """
    Attributes:
        amount (str): Montant à payer, remise déduite.
        attempts (list[PaymentAttempt]):
        checkout_url (None | str): Page de paiement ; null quand l'opérateur ne donne qu'un QR code ou une consigne
            (voir next_action).
        created_at (datetime.datetime):
        currency (PaymentDetailCurrency):
        customer (PaymentCustomer):
        disputes (list[Dispute]): Réservé : toujours vide. Les litiges sont sous GET /v1/disputes?payment_id=.
        error_code (None | str): provider_failed ou expired ; null tant que le paiement n'a pas échoué.
        error_message (None | str): Texte de error_code, dans la langue de la requête.
        fee (None | str): Frais totaux ; null tant que le paiement n'est pas confirmé.
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        merchant_reference (str):
        modified_at (datetime.datetime):
        net (None | str): Montant crédité au marchand ; null tant que le paiement n'est pas confirmé.
        next_action (NextActionType0 | None):
        rail (PaymentDetailRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
        refunds (list[RefundCore]):
        status (PaymentDetailStatus):
        withdrawal_eligibility (PaymentDetailWithdrawalEligibility): confirmed : l'argent est retirable.
        discount_amount (str | Unset): Remise accordée, avec offer_code.
        offer_code (str | Unset): Présent si un code promo a été appliqué.
        original_amount (None | str | Unset): Montant avant remise, avec offer_code.
        payment_link_description (str | Unset): Présent pour un paiement fait sur un lien de paiement : la description
            du lien, à afficher à la place de merchant_reference (link:…). EN: present for a payment made on a payment link:
            the link's description, to show instead of merchant_reference (link:…).
    """

    amount: str
    attempts: list[PaymentAttempt]
    checkout_url: None | str
    created_at: datetime.datetime
    currency: PaymentDetailCurrency
    customer: PaymentCustomer
    disputes: list[Dispute]
    error_code: None | str
    error_message: None | str
    fee: None | str
    id: UUID
    livemode: bool
    merchant_reference: str
    modified_at: datetime.datetime
    net: None | str
    next_action: NextActionType0 | None
    rail: PaymentDetailRail
    refunds: list[RefundCore]
    status: PaymentDetailStatus
    withdrawal_eligibility: PaymentDetailWithdrawalEligibility
    discount_amount: str | Unset = UNSET
    offer_code: str | Unset = UNSET
    original_amount: None | str | Unset = UNSET
    payment_link_description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.next_action_type_0 import NextActionType0

        amount = self.amount

        attempts = []
        for attempts_item_data in self.attempts:
            attempts_item = attempts_item_data.to_dict()
            attempts.append(attempts_item)

        checkout_url: None | str
        checkout_url = self.checkout_url

        created_at = self.created_at.isoformat()

        currency = self.currency.value

        customer = self.customer.to_dict()

        disputes = []
        for disputes_item_data in self.disputes:
            disputes_item = disputes_item_data.to_dict()
            disputes.append(disputes_item)

        error_code: None | str
        error_code = self.error_code

        error_message: None | str
        error_message = self.error_message

        fee: None | str
        fee = self.fee

        id = str(self.id)

        livemode = self.livemode

        merchant_reference = self.merchant_reference

        modified_at = self.modified_at.isoformat()

        net: None | str
        net = self.net

        next_action: dict[str, Any] | None
        if isinstance(self.next_action, NextActionType0):
            next_action = self.next_action.to_dict()
        else:
            next_action = self.next_action

        rail = self.rail.value

        refunds = []
        for refunds_item_data in self.refunds:
            refunds_item = refunds_item_data.to_dict()
            refunds.append(refunds_item)

        status = self.status.value

        withdrawal_eligibility = self.withdrawal_eligibility.value

        discount_amount = self.discount_amount

        offer_code = self.offer_code

        original_amount: None | str | Unset
        if isinstance(self.original_amount, Unset):
            original_amount = UNSET
        else:
            original_amount = self.original_amount

        payment_link_description = self.payment_link_description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "attempts": attempts,
                "checkout_url": checkout_url,
                "created_at": created_at,
                "currency": currency,
                "customer": customer,
                "disputes": disputes,
                "error_code": error_code,
                "error_message": error_message,
                "fee": fee,
                "id": id,
                "livemode": livemode,
                "merchant_reference": merchant_reference,
                "modified_at": modified_at,
                "net": net,
                "next_action": next_action,
                "rail": rail,
                "refunds": refunds,
                "status": status,
                "withdrawal_eligibility": withdrawal_eligibility,
            }
        )
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if offer_code is not UNSET:
            field_dict["offer_code"] = offer_code
        if original_amount is not UNSET:
            field_dict["original_amount"] = original_amount
        if payment_link_description is not UNSET:
            field_dict["payment_link_description"] = payment_link_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dispute import Dispute
        from ..models.next_action_type_0 import NextActionType0
        from ..models.payment_attempt import PaymentAttempt
        from ..models.payment_customer import PaymentCustomer
        from ..models.refund_core import RefundCore

        d = dict(src_dict)
        amount = d.pop("amount")

        attempts = []
        _attempts = d.pop("attempts")
        for attempts_item_data in _attempts:
            attempts_item = PaymentAttempt.from_dict(attempts_item_data)

            attempts.append(attempts_item)

        def _parse_checkout_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        checkout_url = _parse_checkout_url(d.pop("checkout_url"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = PaymentDetailCurrency(d.pop("currency"))

        customer = PaymentCustomer.from_dict(d.pop("customer"))

        disputes = []
        _disputes = d.pop("disputes")
        for disputes_item_data in _disputes:
            disputes_item = Dispute.from_dict(disputes_item_data)

            disputes.append(disputes_item)

        def _parse_error_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_code = _parse_error_code(d.pop("error_code"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        def _parse_fee(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        fee = _parse_fee(d.pop("fee"))

        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        merchant_reference = d.pop("merchant_reference")

        modified_at = datetime.datetime.fromisoformat(d.pop("modified_at"))

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

        rail = PaymentDetailRail(d.pop("rail"))

        refunds = []
        _refunds = d.pop("refunds")
        for refunds_item_data in _refunds:
            refunds_item = RefundCore.from_dict(refunds_item_data)

            refunds.append(refunds_item)

        status = PaymentDetailStatus(d.pop("status"))

        withdrawal_eligibility = PaymentDetailWithdrawalEligibility(
            d.pop("withdrawal_eligibility")
        )

        discount_amount = d.pop("discount_amount", UNSET)

        offer_code = d.pop("offer_code", UNSET)

        def _parse_original_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_amount = _parse_original_amount(d.pop("original_amount", UNSET))

        payment_link_description = d.pop("payment_link_description", UNSET)

        payment_detail = cls(
            amount=amount,
            attempts=attempts,
            checkout_url=checkout_url,
            created_at=created_at,
            currency=currency,
            customer=customer,
            disputes=disputes,
            error_code=error_code,
            error_message=error_message,
            fee=fee,
            id=id,
            livemode=livemode,
            merchant_reference=merchant_reference,
            modified_at=modified_at,
            net=net,
            next_action=next_action,
            rail=rail,
            refunds=refunds,
            status=status,
            withdrawal_eligibility=withdrawal_eligibility,
            discount_amount=discount_amount,
            offer_code=offer_code,
            original_amount=original_amount,
            payment_link_description=payment_link_description,
        )

        return payment_detail
