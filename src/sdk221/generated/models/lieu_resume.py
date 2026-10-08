from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.lieu_resume_level import LieuResumeLevel

if TYPE_CHECKING:
    from ..models.coordonnees import Coordonnees


T = TypeVar("T", bound="LieuResume")


@_attrs_define
class LieuResume:
    """
    Attributes:
        contexte (str):
        coordonnees (Coordonnees):
        id (str):
        level (LieuResumeLevel):
        name (None | str):
        name_source (str):
        parent_id (None | str):
        population_2023 (int | None):
    """

    contexte: str
    coordonnees: Coordonnees
    id: str
    level: LieuResumeLevel
    name: None | str
    name_source: str
    parent_id: None | str
    population_2023: int | None

    def to_dict(self) -> dict[str, Any]:
        contexte = self.contexte

        coordonnees = self.coordonnees.to_dict()

        id = self.id

        level = self.level.value

        name: None | str
        name = self.name

        name_source = self.name_source

        parent_id: None | str
        parent_id = self.parent_id

        population_2023: int | None
        population_2023 = self.population_2023

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contexte": contexte,
                "coordonnees": coordonnees,
                "id": id,
                "level": level,
                "name": name,
                "name_source": name_source,
                "parent_id": parent_id,
                "population_2023": population_2023,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.coordonnees import Coordonnees

        d = dict(src_dict)
        contexte = d.pop("contexte")

        coordonnees = Coordonnees.from_dict(d.pop("coordonnees"))

        id = d.pop("id")

        level = LieuResumeLevel(d.pop("level"))

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        name_source = d.pop("name_source")

        def _parse_parent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        def _parse_population_2023(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        population_2023 = _parse_population_2023(d.pop("population_2023"))

        lieu_resume = cls(
            contexte=contexte,
            coordonnees=coordonnees,
            id=id,
            level=level,
            name=name,
            name_source=name_source,
            parent_id=parent_id,
            population_2023=population_2023,
        )

        return lieu_resume
