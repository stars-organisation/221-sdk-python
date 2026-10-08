from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    """
    Attributes:
        created_at (datetime.datetime): Date du premier paiement.
        customer_id (str): Le numéro de téléphone : un client n'est pas stocké, c'est l'ensemble des paiements d'un même
            numéro.
        email (None | str):
        livemode (bool): true : objet du mode live ; false : mode test.
        name (None | str):
        payments_count (int): Tous les essais, quel que soit leur état.
        phone (str):
        phone_country_code (str):
        total_amount (str): Somme des paiements confirmés.
    """

    created_at: datetime.datetime
    customer_id: str
    email: None | str
    livemode: bool
    name: None | str
    payments_count: int
    phone: str
    phone_country_code: str
    total_amount: str

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        customer_id = self.customer_id

        email: None | str
        email = self.email

        livemode = self.livemode

        name: None | str
        name = self.name

        payments_count = self.payments_count

        phone = self.phone

        phone_country_code = self.phone_country_code

        total_amount = self.total_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "customer_id": customer_id,
                "email": email,
                "livemode": livemode,
                "name": name,
                "payments_count": payments_count,
                "phone": phone,
                "phone_country_code": phone_country_code,
                "total_amount": total_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        customer_id = d.pop("customer_id")

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        livemode = d.pop("livemode")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        payments_count = d.pop("payments_count")

        phone = d.pop("phone")

        phone_country_code = d.pop("phone_country_code")

        total_amount = d.pop("total_amount")

        customer = cls(
            created_at=created_at,
            customer_id=customer_id,
            email=email,
            livemode=livemode,
            name=name,
            payments_count=payments_count,
            phone=phone,
            phone_country_code=phone_country_code,
            total_amount=total_amount,
        )

        return customer
