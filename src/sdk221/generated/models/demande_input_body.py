from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.demande_input_body_kind import DemandeInputBodyKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DemandeInputBody")


@_attrs_define
class DemandeInputBody:
    """
    Attributes:
        kind (DemandeInputBodyKind):
        title (str):
        details (str | Unset):
    """

    kind: DemandeInputBodyKind
    title: str
    details: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        title = self.title

        details = self.details

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "title": title,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = DemandeInputBodyKind(d.pop("kind"))

        title = d.pop("title")

        details = d.pop("details", UNSET)

        demande_input_body = cls(
            kind=kind,
            title=title,
            details=details,
        )

        return demande_input_body
