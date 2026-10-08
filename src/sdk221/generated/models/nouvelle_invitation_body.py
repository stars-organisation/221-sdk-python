from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.nouvelle_invitation_body_role import NouvelleInvitationBodyRole

T = TypeVar("T", bound="NouvelleInvitationBody")


@_attrs_define
class NouvelleInvitationBody:
    """
    Attributes:
        email (str):
        role (NouvelleInvitationBodyRole):
    """

    email: str
    role: NouvelleInvitationBodyRole

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        role = self.role.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email = d.pop("email")

        role = NouvelleInvitationBodyRole(d.pop("role"))

        nouvelle_invitation_body = cls(
            email=email,
            role=role,
        )

        return nouvelle_invitation_body
