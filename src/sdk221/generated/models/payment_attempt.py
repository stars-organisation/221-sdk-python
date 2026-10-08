from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payment_attempt_error_code import PaymentAttemptErrorCode

T = TypeVar("T", bound="PaymentAttempt")


@_attrs_define
class PaymentAttempt:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        attempt_id (str):
        error_code (PaymentAttemptErrorCode):
        error_message (None | str):
        reference_id (str):
        status (str):
    """

    amount: str
    attempt_id: str
    error_code: PaymentAttemptErrorCode
    error_message: None | str
    reference_id: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        attempt_id = self.attempt_id

        error_code = self.error_code.value

        error_message: None | str
        error_message = self.error_message

        reference_id = self.reference_id

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "attempt_id": attempt_id,
                "error_code": error_code,
                "error_message": error_message,
                "reference_id": reference_id,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount = d.pop("amount")

        attempt_id = d.pop("attempt_id")

        error_code = PaymentAttemptErrorCode(d.pop("error_code"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        reference_id = d.pop("reference_id")

        status = d.pop("status")

        payment_attempt = cls(
            amount=amount,
            attempt_id=attempt_id,
            error_code=error_code,
            error_message=error_message,
            reference_id=reference_id,
            status=status,
        )

        return payment_attempt
