from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Conditions")


@_attrs_define
class Conditions:
    """
    Attributes:
        accepted (bool):
        version (str):
    """

    accepted: bool
    version: str

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accepted": accepted,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        version = d.pop("version")

        conditions = cls(
            accepted=accepted,
            version=version,
        )

        return conditions
