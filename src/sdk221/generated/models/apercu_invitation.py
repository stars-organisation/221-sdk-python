from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.apercu_invitation_role import ApercuInvitationRole
from ..models.apercu_invitation_status import ApercuInvitationStatus

T = TypeVar("T", bound="ApercuInvitation")


@_attrs_define
class ApercuInvitation:
    """
    Attributes:
        email_masked (str):
        expires_at (datetime.datetime):
        project_name (str):
        role (ApercuInvitationRole):
        status (ApercuInvitationStatus):
    """

    email_masked: str
    expires_at: datetime.datetime
    project_name: str
    role: ApercuInvitationRole
    status: ApercuInvitationStatus

    def to_dict(self) -> dict[str, Any]:
        email_masked = self.email_masked

        expires_at = self.expires_at.isoformat()

        project_name = self.project_name

        role = self.role.value

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email_masked": email_masked,
                "expires_at": expires_at,
                "project_name": project_name,
                "role": role,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        email_masked = d.pop("email_masked")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        project_name = d.pop("project_name")

        role = ApercuInvitationRole(d.pop("role"))

        status = ApercuInvitationStatus(d.pop("status"))

        apercu_invitation = cls(
            email_masked=email_masked,
            expires_at=expires_at,
            project_name=project_name,
            role=role,
            status=status,
        )

        return apercu_invitation
