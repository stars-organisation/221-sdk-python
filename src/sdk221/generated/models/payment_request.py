from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payment_request_currency import PaymentRequestCurrency
from ..models.payment_request_customer_device import PaymentRequestCustomerDevice
from ..models.payment_request_rail import PaymentRequestRail
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentRequest")


@_attrs_define
class PaymentRequest:
    """
    Attributes:
        amount (str): Montant à encaisser, au moins min_amount du moyen de paiement.
        currency (PaymentRequestCurrency):
        merchant_reference (str): Référence de votre commande, unique par projet et par mode.
        rail (PaymentRequestRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
        return_url (str): Où renvoyer le client après le paiement : https obligatoire.
        customer_device (PaymentRequestCustomerDevice | Unset): Appareil du client. sn_orange : mobile (par défaut)
            ouvre l'app Max it, desktop donne un QR code à scanner (next_action de type qr). Sans effet sur les autres
            moyens. EN: the customer's device. sn_orange: mobile (default) opens the Max it app, desktop returns a QR code
            to scan (next_action of type qr). No effect on other rails.
        customer_otp (str | Unset): Code composé par le client. Requis seulement si otp_required vaut true pour le moyen
            de paiement, refusé sinon.
        customer_phone (str | Unset): Numéro mobile du client, valide pour le pays du moyen de paiement. Requis en mode
            live.
        offer_code (str | Unset): Code promo du projet (insensible à la casse).
    """

    amount: str
    currency: PaymentRequestCurrency
    merchant_reference: str
    rail: PaymentRequestRail
    return_url: str
    customer_device: PaymentRequestCustomerDevice | Unset = UNSET
    customer_otp: str | Unset = UNSET
    customer_phone: str | Unset = UNSET
    offer_code: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency.value

        merchant_reference = self.merchant_reference

        rail = self.rail.value

        return_url = self.return_url

        customer_device: str | Unset = UNSET
        if not isinstance(self.customer_device, Unset):
            customer_device = self.customer_device.value

        customer_otp = self.customer_otp

        customer_phone = self.customer_phone

        offer_code = self.offer_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
                "merchant_reference": merchant_reference,
                "rail": rail,
                "return_url": return_url,
            }
        )
        if customer_device is not UNSET:
            field_dict["customer_device"] = customer_device
        if customer_otp is not UNSET:
            field_dict["customer_otp"] = customer_otp
        if customer_phone is not UNSET:
            field_dict["customer_phone"] = customer_phone
        if offer_code is not UNSET:
            field_dict["offer_code"] = offer_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = PaymentRequestCurrency(d.pop("currency"))

        merchant_reference = d.pop("merchant_reference")

        rail = PaymentRequestRail(d.pop("rail"))

        return_url = d.pop("return_url")

        _customer_device = d.pop("customer_device", UNSET)
        customer_device: PaymentRequestCustomerDevice | Unset
        if isinstance(_customer_device, Unset):
            customer_device = UNSET
        else:
            customer_device = PaymentRequestCustomerDevice(_customer_device)

        customer_otp = d.pop("customer_otp", UNSET)

        customer_phone = d.pop("customer_phone", UNSET)

        offer_code = d.pop("offer_code", UNSET)

        payment_request = cls(
            amount=amount,
            currency=currency,
            merchant_reference=merchant_reference,
            rail=rail,
            return_url=return_url,
            customer_device=customer_device,
            customer_otp=customer_otp,
            customer_phone=customer_phone,
            offer_code=offer_code,
        )

        return payment_request
