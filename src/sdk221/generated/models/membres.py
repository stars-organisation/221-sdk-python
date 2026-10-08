from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.invitation import Invitation
    from ..models.membre import Membre


T = TypeVar("T", bound="Membres")


@_attrs_define
class Membres:
    """
    Attributes:
        invitations (list[Invitation] | None):
        members (list[Membre] | None):
    """

    invitations: list[Invitation] | None
    members: list[Membre] | None

    def to_dict(self) -> dict[str, Any]:
        invitations: list[dict[str, Any]] | None
        if isinstance(self.invitations, list):
            invitations = []
            for invitations_type_0_item_data in self.invitations:
                invitations_type_0_item = invitations_type_0_item_data.to_dict()
                invitations.append(invitations_type_0_item)

        else:
            invitations = self.invitations

        members: list[dict[str, Any]] | None
        if isinstance(self.members, list):
            members = []
            for members_type_0_item_data in self.members:
                members_type_0_item = members_type_0_item_data.to_dict()
                members.append(members_type_0_item)

        else:
            members = self.members

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "invitations": invitations,
                "members": members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.invitation import Invitation
        from ..models.membre import Membre

        d = dict(src_dict)

        def _parse_invitations(data: object) -> list[Invitation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                invitations_type_0 = []
                _invitations_type_0 = data
                for invitations_type_0_item_data in _invitations_type_0:
                    invitations_type_0_item = Invitation.from_dict(
                        invitations_type_0_item_data
                    )

                    invitations_type_0.append(invitations_type_0_item)

                return invitations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Invitation] | None, data)

        invitations = _parse_invitations(d.pop("invitations"))

        def _parse_members(data: object) -> list[Membre] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = []
                _members_type_0 = data
                for members_type_0_item_data in _members_type_0:
                    members_type_0_item = Membre.from_dict(members_type_0_item_data)

                    members_type_0.append(members_type_0_item)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Membre] | None, data)

        members = _parse_members(d.pop("members"))

        membres = cls(
            invitations=invitations,
            members=members,
        )

        return membres
