from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.adhesion_role import AdhesionRole

T = TypeVar("T", bound="Adhesion")


@_attrs_define
class Adhesion:
    """
    Attributes:
        project_id (str):
        role (AdhesionRole):
    """

    project_id: str
    role: AdhesionRole

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        role = self.role.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "project_id": project_id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        role = AdhesionRole(d.pop("role"))

        adhesion = cls(
            project_id=project_id,
            role=role,
        )

        return adhesion
