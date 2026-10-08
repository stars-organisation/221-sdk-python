from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.coordonnees_precision import CoordonneesPrecision

T = TypeVar("T", bound="Coordonnees")


@_attrs_define
class Coordonnees:
    """
    Attributes:
        lat (float):
        lon (float):
        precision (CoordonneesPrecision):
    """

    lat: float
    lon: float
    precision: CoordonneesPrecision

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        lon = self.lon

        precision = self.precision.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lat": lat,
                "lon": lon,
                "precision": precision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lat = d.pop("lat")

        lon = d.pop("lon")

        precision = CoordonneesPrecision(d.pop("precision"))

        coordonnees = cls(
            lat=lat,
            lon=lon,
            precision=precision,
        )

        return coordonnees
