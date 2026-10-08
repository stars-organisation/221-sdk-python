from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PaymentCustomer")


@_attrs_define
class PaymentCustomer:
    """
    Attributes:
        email (None | str): Toujours null : 221 Pay ne collecte pas l'e-mail.
        name (None | str): Toujours null : 221 Pay ne collecte pas le nom.
        phone (None | str):
    """

    email: None | str
    name: None | str
    phone: None | str

    def to_dict(self) -> dict[str, Any]:
        email: None | str
        email = self.email

        name: None | str
        name = self.name

        phone: None | str
        phone = self.phone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "name": name,
                "phone": phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(d.pop("email"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        payment_customer = cls(
            email=email,
            name=name,
            phone=phone,
        )

        return payment_customer
