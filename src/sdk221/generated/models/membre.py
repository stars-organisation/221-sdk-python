from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.membre_role import MembreRole

T = TypeVar("T", bound="Membre")


@_attrs_define
class Membre:
    """
    Attributes:
        email (str):
        joined_at (datetime.datetime):
        name (str):
        role (MembreRole):
        user_id (str):
    """

    email: str
    joined_at: datetime.datetime
    name: str
    role: MembreRole
    user_id: str

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        joined_at = self.joined_at.isoformat()

        name = self.name

        role = self.role.value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "joined_at": joined_at,
                "name": name,
                "role": role,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        joined_at = datetime.datetime.fromisoformat(d.pop("joined_at"))

        name = d.pop("name")

        role = MembreRole(d.pop("role"))

        user_id = d.pop("user_id")

        membre = cls(
            email=email,
            joined_at=joined_at,
            name=name,
            role=role,
            user_id=user_id,
        )

        return membre
