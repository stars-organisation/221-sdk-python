from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCompteBody")


@_attrs_define
class DeleteCompteBody:
    """
    Attributes:
        password (str | Unset):
    """

    password: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        delete_compte_body = cls(
            password=password,
        )

        return delete_compte_body
