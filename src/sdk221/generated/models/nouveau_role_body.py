from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.nouveau_role_body_role import NouveauRoleBodyRole

T = TypeVar("T", bound="NouveauRoleBody")


@_attrs_define
class NouveauRoleBody:
    """
    Attributes:
        role (NouveauRoleBodyRole):
    """

    role: NouveauRoleBodyRole

    def to_dict(self) -> dict[str, Any]:
        role = self.role.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        role = NouveauRoleBodyRole(d.pop("role"))

        nouveau_role_body = cls(
            role=role,
        )

        return nouveau_role_body
