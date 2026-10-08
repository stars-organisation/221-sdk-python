from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Recognised")


@_attrs_define
class Recognised:
    """
    Attributes:
        candidats (int):
        texte (str):
    """

    candidats: int
    texte: str

    def to_dict(self) -> dict[str, Any]:
        candidats = self.candidats

        texte = self.texte

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "candidats": candidats,
                "texte": texte,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        candidats = d.pop("candidats")

        texte = d.pop("texte")

        recognised = cls(
            candidats=candidats,
            texte=texte,
        )

        return recognised
