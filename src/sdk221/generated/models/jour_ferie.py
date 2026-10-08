from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.jour_ferie_date_status import JourFerieDateStatus
from ..models.jour_ferie_type import JourFerieType

if TYPE_CHECKING:
    from ..models.nom_bilingue import NomBilingue
    from ..models.source_verifiee import SourceVerifiee


T = TypeVar("T", bound="JourFerie")


@_attrs_define
class JourFerie:
    """
    Attributes:
        date (datetime.date):
        date_status (JourFerieDateStatus): previsionnelle : date dépendant d'une observation, à confirmer.
        id (str):
        name (NomBilingue):
        sources (list[SourceVerifiee]):
        type_ (JourFerieType):
    """

    date: datetime.date
    date_status: JourFerieDateStatus
    id: str
    name: NomBilingue
    sources: list[SourceVerifiee]
    type_: JourFerieType

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        date_status = self.date_status.value

        id = self.id

        name = self.name.to_dict()

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "date_status": date_status,
                "id": id,
                "name": name,
                "sources": sources,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.nom_bilingue import NomBilingue
        from ..models.source_verifiee import SourceVerifiee

        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        date_status = JourFerieDateStatus(d.pop("date_status"))

        id = d.pop("id")

        name = NomBilingue.from_dict(d.pop("name"))

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceVerifiee.from_dict(sources_item_data)

            sources.append(sources_item)

        type_ = JourFerieType(d.pop("type"))

        jour_ferie = cls(
            date=date,
            date_status=date_status,
            id=id,
            name=name,
            sources=sources,
            type_=type_,
        )

        return jour_ferie
