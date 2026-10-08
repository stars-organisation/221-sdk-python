from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.rattachement_methode import RattachementMethode

if TYPE_CHECKING:
    from ..models.lieu import Lieu
    from ..models.source import Source


T = TypeVar("T", bound="Rattachement")


@_attrs_define
class Rattachement:
    """
    Attributes:
        arrondissement (Lieu):
        avertissements (list[str] | None):
        commune (Lieu):
        departement (Lieu):
        distance_centroide_km (float | None):
        lat (float):
        lon (float):
        methode (RattachementMethode):
        precision (str):
        region (Lieu):
        sources (list[Source] | None):
    """

    arrondissement: Lieu
    avertissements: list[str] | None
    commune: Lieu
    departement: Lieu
    distance_centroide_km: float | None
    lat: float
    lon: float
    methode: RattachementMethode
    precision: str
    region: Lieu
    sources: list[Source] | None

    def to_dict(self) -> dict[str, Any]:
        arrondissement = self.arrondissement.to_dict()

        avertissements: list[str] | None
        if isinstance(self.avertissements, list):
            avertissements = self.avertissements

        else:
            avertissements = self.avertissements

        commune = self.commune.to_dict()

        departement = self.departement.to_dict()

        distance_centroide_km: float | None
        distance_centroide_km = self.distance_centroide_km

        lat = self.lat

        lon = self.lon

        methode = self.methode.value

        precision = self.precision

        region = self.region.to_dict()

        sources: list[dict[str, Any]] | None
        if isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "arrondissement": arrondissement,
                "avertissements": avertissements,
                "commune": commune,
                "departement": departement,
                "distance_centroide_km": distance_centroide_km,
                "lat": lat,
                "lon": lon,
                "methode": methode,
                "precision": precision,
                "region": region,
                "sources": sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lieu import Lieu
        from ..models.source import Source

        d = dict(src_dict)
        arrondissement = Lieu.from_dict(d.pop("arrondissement"))

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

        commune = Lieu.from_dict(d.pop("commune"))

        departement = Lieu.from_dict(d.pop("departement"))

        def _parse_distance_centroide_km(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        distance_centroide_km = _parse_distance_centroide_km(
            d.pop("distance_centroide_km")
        )

        lat = d.pop("lat")

        lon = d.pop("lon")

        methode = RattachementMethode(d.pop("methode"))

        precision = d.pop("precision")

        region = Lieu.from_dict(d.pop("region"))

        def _parse_sources(data: object) -> list[Source] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = Source.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Source] | None, data)

        sources = _parse_sources(d.pop("sources"))

        rattachement = cls(
            arrondissement=arrondissement,
            avertissements=avertissements,
            commune=commune,
            departement=departement,
            distance_centroide_km=distance_centroide_km,
            lat=lat,
            lon=lon,
            methode=methode,
            precision=precision,
            region=region,
            sources=sources,
        )

        return rattachement
