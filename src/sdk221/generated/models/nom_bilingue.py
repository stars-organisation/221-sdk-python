from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="NomBilingue")


@_attrs_define
class NomBilingue:
    """
    Attributes:
        en (str):
        fr (str):
    """

    en: str
    fr: str

    def to_dict(self) -> dict[str, Any]:
        en = self.en

        fr = self.fr

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "en": en,
                "fr": fr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        en = d.pop("en")

        fr = d.pop("fr")

        nom_bilingue = cls(
            en=en,
            fr=fr,
        )

        return nom_bilingue
