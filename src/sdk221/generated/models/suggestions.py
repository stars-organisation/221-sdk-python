from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.lieu_resume import LieuResume
    from ..models.source import Source


T = TypeVar("T", bound="Suggestions")


@_attrs_define
class Suggestions:
    """
    Attributes:
        data (list[LieuResume] | None):
        sources (list[Source] | None):
    """

    data: list[LieuResume] | None
    sources: list[Source] | None

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

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
                "data": data,
                "sources": sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lieu_resume import LieuResume
        from ..models.source import Source

        d = dict(src_dict)

        def _parse_data(data: object) -> list[LieuResume] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = LieuResume.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LieuResume] | None, data)

        data = _parse_data(d.pop("data"))

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

        suggestions = cls(
            data=data,
            sources=sources,
        )

        return suggestions
