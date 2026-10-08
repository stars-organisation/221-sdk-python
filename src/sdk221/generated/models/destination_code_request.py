from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="DestinationCodeRequest")


@_attrs_define
class DestinationCodeRequest:
    """
    Attributes:
        code (str): Code à 6 chiffres reçu par e-mail par le propriétaire du compte.
    """

    code: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        destination_code_request = cls(
            code=code,
        )

        return destination_code_request
