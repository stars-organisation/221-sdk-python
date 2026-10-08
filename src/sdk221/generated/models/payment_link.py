from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payment_link_currency import PaymentLinkCurrency
from ..models.payment_link_status import PaymentLinkStatus

T = TypeVar("T", bound="PaymentLink")


@_attrs_define
class PaymentLink:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        created_at (datetime.datetime):
        currency (PaymentLinkCurrency):
        description (str):
        expiry (datetime.datetime | None):
        link_to_pay (str): Page de paiement à partager : chaque visite crée un paiement.
        livemode (bool): true : objet du mode live ; false : mode test.
        payment_link_id (UUID):
        status (PaymentLinkStatus):
    """

    amount: str
    created_at: datetime.datetime
    currency: PaymentLinkCurrency
    description: str
    expiry: datetime.datetime | None
    link_to_pay: str
    livemode: bool
    payment_link_id: UUID
    status: PaymentLinkStatus

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        created_at = self.created_at.isoformat()

        currency = self.currency.value

        description = self.description

        expiry: None | str
        if isinstance(self.expiry, datetime.datetime):
            expiry = self.expiry.isoformat()
        else:
            expiry = self.expiry

        link_to_pay = self.link_to_pay

        livemode = self.livemode

        payment_link_id = str(self.payment_link_id)

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "created_at": created_at,
                "currency": currency,
                "description": description,
                "expiry": expiry,
                "link_to_pay": link_to_pay,
                "livemode": livemode,
                "payment_link_id": payment_link_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = PaymentLinkCurrency(d.pop("currency"))

        description = d.pop("description")

        def _parse_expiry(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_type_0 = datetime.datetime.fromisoformat(data)

                return expiry_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expiry = _parse_expiry(d.pop("expiry"))

        link_to_pay = d.pop("link_to_pay")

        livemode = d.pop("livemode")

        payment_link_id = UUID(d.pop("payment_link_id"))

        status = PaymentLinkStatus(d.pop("status"))

        payment_link = cls(
            amount=amount,
            created_at=created_at,
            currency=currency,
            description=description,
            expiry=expiry,
            link_to_pay=link_to_pay,
            livemode=livemode,
            payment_link_id=payment_link_id,
            status=status,
        )

        return payment_link
