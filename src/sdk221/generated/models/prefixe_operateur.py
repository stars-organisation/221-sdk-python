from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.prefixe_operateur_type import PrefixeOperateurType

if TYPE_CHECKING:
    from ..models.source_verifiee import SourceVerifiee


T = TypeVar("T", bound="PrefixeOperateur")


@_attrs_define
class PrefixeOperateur:
    """
    Attributes:
        id (str):
        operator (str):
        prefix (str): Préfixe national du numéro, sans indicatif.
        sources (list[SourceVerifiee]):
        type_ (PrefixeOperateurType):
    """

    id: str
    operator: str
    prefix: str
    sources: list[SourceVerifiee]
    type_: PrefixeOperateurType

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        operator = self.operator

        prefix = self.prefix

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "operator": operator,
                "prefix": prefix,
                "sources": sources,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.source_verifiee import SourceVerifiee

        d = dict(src_dict)
        id = d.pop("id")

        operator = d.pop("operator")

        prefix = d.pop("prefix")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = SourceVerifiee.from_dict(sources_item_data)

            sources.append(sources_item)

        type_ = PrefixeOperateurType(d.pop("type"))

        prefixe_operateur = cls(
            id=id,
            operator=operator,
            prefix=prefix,
            sources=sources,
            type_=type_,
        )

        return prefixe_operateur
