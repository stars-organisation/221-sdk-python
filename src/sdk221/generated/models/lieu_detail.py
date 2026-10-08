from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.lieu import Lieu


T = TypeVar("T", bound="LieuDetail")


@_attrs_define
class LieuDetail:
    """
    Attributes:
        ancestors (list[Lieu] | None):
        children (list[Lieu] | None):
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

    ancestors: list[Lieu] | None
    children: list[Lieu] | None
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
        ancestors: list[dict[str, Any]] | None
        if isinstance(self.ancestors, list):
            ancestors = []
            for ancestors_type_0_item_data in self.ancestors:
                ancestors_type_0_item = ancestors_type_0_item_data.to_dict()
                ancestors.append(ancestors_type_0_item)

        else:
            ancestors = self.ancestors

        children: list[dict[str, Any]] | None
        if isinstance(self.children, list):
            children = []
            for children_type_0_item_data in self.children:
                children_type_0_item = children_type_0_item_data.to_dict()
                children.append(children_type_0_item)

        else:
            children = self.children

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
                "ancestors": ancestors,
                "children": children,
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
        from ..models.lieu import Lieu

        d = dict(src_dict)

        def _parse_ancestors(data: object) -> list[Lieu] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ancestors_type_0 = []
                _ancestors_type_0 = data
                for ancestors_type_0_item_data in _ancestors_type_0:
                    ancestors_type_0_item = Lieu.from_dict(ancestors_type_0_item_data)

                    ancestors_type_0.append(ancestors_type_0_item)

                return ancestors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Lieu] | None, data)

        ancestors = _parse_ancestors(d.pop("ancestors"))

        def _parse_children(data: object) -> list[Lieu] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                children_type_0 = []
                _children_type_0 = data
                for children_type_0_item_data in _children_type_0:
                    children_type_0_item = Lieu.from_dict(children_type_0_item_data)

                    children_type_0.append(children_type_0_item)

                return children_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Lieu] | None, data)

        children = _parse_children(d.pop("children"))

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

        lieu_detail = cls(
            ancestors=ancestors,
            children=children,
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

        return lieu_detail
