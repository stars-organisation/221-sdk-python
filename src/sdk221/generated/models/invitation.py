from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.invitation_role import InvitationRole

T = TypeVar("T", bound="Invitation")


@_attrs_define
class Invitation:
    """
    Attributes:
        email (str):
        expires_at (datetime.datetime):
        id (str):
        role (InvitationRole):
    """

    email: str
    expires_at: datetime.datetime
    id: str
    role: InvitationRole

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        expires_at = self.expires_at.isoformat()

        id = self.id

        role = self.role.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "expires_at": expires_at,
                "id": id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = d.pop("id")

        role = InvitationRole(d.pop("role"))

        invitation = cls(
            email=email,
            expires_at=expires_at,
            id=id,
            role=role,
        )

        return invitation
