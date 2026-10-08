from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.lieu_resume import LieuResume
    from ..models.source import Source


T = TypeVar("T", bound="Geocodage")


@_attrs_define
class Geocodage:
    """
    Attributes:
        alternatives (list[LieuResume] | None):
        ambigu (bool):
        avertissements (list[str] | None):
        lat (float | None):
        lieu (LieuResume | None):
        lon (float | None):
        precision (None | str):
        relation (None | str): en_face_de, derriere, a_cote_de ou pres_de ; null si aucune relation n'est reconnue.
        repere (None | str):
        sources (list[Source] | None):
        texte (str):
    """

    alternatives: list[LieuResume] | None
    ambigu: bool
    avertissements: list[str] | None
    lat: float | None
    lieu: LieuResume | None
    lon: float | None
    precision: None | str
    relation: None | str
    repere: None | str
    sources: list[Source] | None
    texte: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.lieu_resume import LieuResume

        alternatives: list[dict[str, Any]] | None
        if isinstance(self.alternatives, list):
            alternatives = []
            for alternatives_type_0_item_data in self.alternatives:
                alternatives_type_0_item = alternatives_type_0_item_data.to_dict()
                alternatives.append(alternatives_type_0_item)

        else:
            alternatives = self.alternatives

        ambigu = self.ambigu

        avertissements: list[str] | None
        if isinstance(self.avertissements, list):
            avertissements = self.avertissements

        else:
            avertissements = self.avertissements

        lat: float | None
        lat = self.lat

        lieu: dict[str, Any] | None
        if isinstance(self.lieu, LieuResume):
            lieu = self.lieu.to_dict()
        else:
            lieu = self.lieu

        lon: float | None
        lon = self.lon

        precision: None | str
        precision = self.precision

        relation: None | str
        relation = self.relation

        repere: None | str
        repere = self.repere

        sources: list[dict[str, Any]] | None
        if isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        texte = self.texte

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alternatives": alternatives,
                "ambigu": ambigu,
                "avertissements": avertissements,
                "lat": lat,
                "lieu": lieu,
                "lon": lon,
                "precision": precision,
                "relation": relation,
                "repere": repere,
                "sources": sources,
                "texte": texte,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lieu_resume import LieuResume
        from ..models.source import Source

        d = dict(src_dict)

        def _parse_alternatives(data: object) -> list[LieuResume] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alternatives_type_0 = []
                _alternatives_type_0 = data
                for alternatives_type_0_item_data in _alternatives_type_0:
                    alternatives_type_0_item = LieuResume.from_dict(
                        alternatives_type_0_item_data
                    )

                    alternatives_type_0.append(alternatives_type_0_item)

                return alternatives_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LieuResume] | None, data)

        alternatives = _parse_alternatives(d.pop("alternatives"))

        ambigu = d.pop("ambigu")

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

        def _parse_lat(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lat = _parse_lat(d.pop("lat"))

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

        def _parse_lon(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lon = _parse_lon(d.pop("lon"))

        def _parse_precision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        precision = _parse_precision(d.pop("precision"))

        def _parse_relation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relation = _parse_relation(d.pop("relation"))

        def _parse_repere(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repere = _parse_repere(d.pop("repere"))

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

        texte = d.pop("texte")

        geocodage = cls(
            alternatives=alternatives,
            ambigu=ambigu,
            avertissements=avertissements,
            lat=lat,
            lieu=lieu,
            lon=lon,
            precision=precision,
            relation=relation,
            repere=repere,
            sources=sources,
            texte=texte,
        )

        return geocodage
