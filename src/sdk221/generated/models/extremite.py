from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        lieu (LieuResume | None):
        lon (float):
        precision (str):
    """

    entree: str
    lat: float
    lieu: LieuResume | None
    lon: float
    precision: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.lieu_resume import LieuResume

        entree = self.entree

        lat = self.lat

        lieu: dict[str, Any] | None
        if isinstance(self.lieu, LieuResume):
            lieu = self.lieu.to_dict()
        else:
            lieu = self.lieu

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

        def _parse_lieu(data: object) -> LieuResume | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lieu_type_0 = LieuResume.from_dict(data)

                return lieu_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LieuResume | None, data)

        lieu = _parse_lieu(d.pop("lieu"))

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
