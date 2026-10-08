from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="OperateurTelephoneType0")


@_attrs_define
class OperateurTelephoneType0:
    """
    Attributes:
        name (str):
        prefix (str):
        sources (list[Any] | None):
        type_ (str):
    """

    name: str
    prefix: str
    sources: list[Any] | None
    type_: str

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        prefix = self.prefix

        sources: list[Any] | None
        if isinstance(self.sources, list):
            sources = self.sources

        else:
            sources = self.sources

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "prefix": prefix,
                "sources": sources,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        prefix = d.pop("prefix")

        def _parse_sources(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = cast(list[Any], data)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        sources = _parse_sources(d.pop("sources"))

        type_ = d.pop("type")

        operateur_telephone_type_0 = cls(
            name=name,
            prefix=prefix,
            sources=sources,
            type_=type_,
        )

        return operateur_telephone_type_0
