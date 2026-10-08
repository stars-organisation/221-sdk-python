from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.rotation_cle_body_grace import RotationCleBodyGrace

T = TypeVar("T", bound="RotationCleBody")


@_attrs_define
class RotationCleBody:
    """
    Attributes:
        grace (RotationCleBodyGrace): Validité restante de l'ancienne clé : now (révoquée tout de suite), 1h, 24h ou 7d.
    """

    grace: RotationCleBodyGrace

    def to_dict(self) -> dict[str, Any]:
        grace = self.grace.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "grace": grace,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        grace = RotationCleBodyGrace(d.pop("grace"))

        rotation_cle_body = cls(
            grace=grace,
        )

        return rotation_cle_body
