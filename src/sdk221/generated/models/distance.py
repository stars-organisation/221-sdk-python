from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.distance_methode import DistanceMethode

if TYPE_CHECKING:
    from ..models.extremite import Extremite


T = TypeVar("T", bound="Distance")


@_attrs_define
class Distance:
    """
    Attributes:
        avertissements (list[str] | None):
        description (str):
        distance_km (float):
        distance_m (int):
        from_ (Extremite):
        methode (DistanceMethode):
        to (Extremite):
    """

    avertissements: list[str] | None
    description: str
    distance_km: float
    distance_m: int
    from_: Extremite
    methode: DistanceMethode
    to: Extremite

    def to_dict(self) -> dict[str, Any]:
        avertissements: list[str] | None
        if isinstance(self.avertissements, list):
            avertissements = self.avertissements

        else:
            avertissements = self.avertissements

        description = self.description

        distance_km = self.distance_km

        distance_m = self.distance_m

        from_ = self.from_.to_dict()

        methode = self.methode.value

        to = self.to.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avertissements": avertissements,
                "description": description,
                "distance_km": distance_km,
                "distance_m": distance_m,
                "from": from_,
                "methode": methode,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.extremite import Extremite

        d = dict(src_dict)

        def _parse_avertissements(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                avertissements_type_0 = cast(list[str], data)

                return avertissements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        avertissements = _parse_avertissements(d.pop("avertissements"))

        description = d.pop("description")

        distance_km = d.pop("distance_km")

        distance_m = d.pop("distance_m")

        from_ = Extremite.from_dict(d.pop("from"))

        methode = DistanceMethode(d.pop("methode"))

        to = Extremite.from_dict(d.pop("to"))

        distance = cls(
            avertissements=avertissements,
            description=description,
            distance_km=distance_km,
            distance_m=distance_m,
            from_=from_,
            methode=methode,
            to=to,
        )

        return distance
