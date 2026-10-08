from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.lieu_resume import LieuResume


T = TypeVar("T", bound="Extremite")


@_attrs_define
class Extremite:
    """
    Attributes:
        entree (str):
        lat (float):
        lieu (LieuResume):
        lon (float):
        precision (str):
    """

    entree: str
    lat: float
    lieu: LieuResume
    lon: float
    precision: str

    def to_dict(self) -> dict[str, Any]:
        entree = self.entree

        lat = self.lat

        lieu = self.lieu.to_dict()

        lon = self.lon

        precision = self.precision

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entree": entree,
                "lat": lat,
                "lieu": lieu,
                "lon": lon,
                "precision": precision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lieu_resume import LieuResume

        d = dict(src_dict)
        entree = d.pop("entree")

        lat = d.pop("lat")

        lieu = LieuResume.from_dict(d.pop("lieu"))

        lon = d.pop("lon")

        precision = d.pop("precision")

        extremite = cls(
            entree=entree,
            lat=lat,
            lieu=lieu,
            lon=lon,
            precision=precision,
        )

        return extremite
