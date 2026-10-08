from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.source_verifiee import SourceVerifiee


T = TypeVar("T", bound="Banque")


@_attrs_define
class Banque:
    """
    Attributes:
        bank_code (str): Code d'agrément BCEAO.
        id (str):
        name (str):
        sources (list[SourceVerifiee]):
        website (None | str): null quand le site n'est pas vérifié.
    """

    bank_code: str
    id: str
    name: str
    sources: list[SourceVerifiee]
    website: None | str

    def to_dict(self) -> dict[str, Any]:
        bank_code = self.bank_code

        id = self.id

        name = self.name

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        website: None | str
        website = self.website

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bank_code": bank_code,
                "id": id,
                "name": name,
                "sources": sources,
                "website": website,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.source_verifiee import SourceVerifiee

        d = dict(src_dict)
        bank_code = d.pop("bank_code")

        id = d.pop("id")

        name = d.pop("name")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceVerifiee.from_dict(sources_item_data)

            sources.append(sources_item)

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        banque = cls(
            bank_code=bank_code,
            id=id,
            name=name,
            sources=sources,
            website=website,
        )

        return banque
