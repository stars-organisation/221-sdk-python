from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PaymentAttempt")


@_attrs_define
class PaymentAttempt:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        error_code (None | str): provider_failed ou expired ; null tant que la tentative n'a pas échoué.
        error_message (None | str):
        id (str): Référence de la tentative chez l'opérateur.
        status (str):
    """

    amount: str
    error_code: None | str
    error_message: None | str
    id: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        error_code: None | str
        error_code = self.error_code

        error_message: None | str
        error_message = self.error_message

        id = self.id

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "error_code": error_code,
                "error_message": error_message,
                "id": id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

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

        id = d.pop("id")

        status = d.pop("status")

        payment_attempt = cls(
            amount=amount,
            error_code=error_code,
            error_message=error_message,
            id=id,
            status=status,
        )

        return payment_attempt
