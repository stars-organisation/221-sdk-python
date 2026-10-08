from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentLinkRequest")


@_attrs_define
class PaymentLinkRequest:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        description (str):
        expiry (datetime.datetime | Unset): Fin de validité, dans le futur ; sans valeur le lien n'expire pas.
        return_url (str | Unset):
    """

    amount: str
    description: str
    expiry: datetime.datetime | Unset = UNSET
    return_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        description = self.description

        expiry: str | Unset = UNSET
        if not isinstance(self.expiry, Unset):
            expiry = self.expiry.isoformat()

        return_url = self.return_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "description": description,
            }
        )
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if return_url is not UNSET:
            field_dict["return_url"] = return_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        description = d.pop("description")

        _expiry = d.pop("expiry", UNSET)
        expiry: datetime.datetime | Unset
        if isinstance(_expiry, Unset):
            expiry = UNSET
        else:
            expiry = datetime.datetime.fromisoformat(_expiry)

        return_url = d.pop("return_url", UNSET)

        payment_link_request = cls(
            amount=amount,
            description=description,
            expiry=expiry,
            return_url=return_url,
        )

        return payment_link_request
