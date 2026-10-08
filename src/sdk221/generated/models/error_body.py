from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="ErrorBody")


@_attrs_define
class ErrorBody:
    """
    Attributes:
        code (str):
        details (Any):
        message (str):
    """

    code: str
    details: Any
    message: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        details = self.details

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "details": details,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        details = d.pop("details")

        message = d.pop("message")

        error_body = cls(
            code=code,
            details=details,
            message=message,
        )

        return error_body
