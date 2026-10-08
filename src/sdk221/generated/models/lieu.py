from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Lieu")


@_attrs_define
class Lieu:
    """
    Attributes:
        id (str):
        lat (float | None):
        level (str):
        lon (float | None):
        name (None | str):
        name_source (str):
        parent_id (None | str):
        population_2023 (int | None):
        search_key (str):
    """

    id: str
    lat: float | None
    level: str
    lon: float | None
    name: None | str
    name_source: str
    parent_id: None | str
    population_2023: int | None
    search_key: str

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        lat: float | None
        lat = self.lat

        level = self.level

        lon: float | None
        lon = self.lon

        name: None | str
        name = self.name

        name_source = self.name_source

        parent_id: None | str
        parent_id = self.parent_id

        population_2023: int | None
        population_2023 = self.population_2023

        search_key = self.search_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "lat": lat,
                "level": level,
                "lon": lon,
                "name": name,
                "name_source": name_source,
                "parent_id": parent_id,
                "population_2023": population_2023,
                "search_key": search_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_lat(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lat = _parse_lat(d.pop("lat"))

        level = d.pop("level")

        def _parse_lon(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lon = _parse_lon(d.pop("lon"))

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

        search_key = d.pop("search_key")

        lieu = cls(
            id=id,
            lat=lat,
            level=level,
            lon=lon,
            name=name,
            name_source=name_source,
            parent_id=parent_id,
            population_2023=population_2023,
            search_key=search_key,
        )

        return lieu
