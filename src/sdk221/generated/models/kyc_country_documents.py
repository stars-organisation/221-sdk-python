from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.item import Item


T = TypeVar("T", bound="KycCountryDocuments")


@_attrs_define
class KycCountryDocuments:
    """
    Attributes:
        country (str):
        documents (list[Item]):
    """

    country: str
    documents: list[Item]

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.item import Item

        d = dict(src_dict)
        country = d.pop("country")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = Item.from_dict(documents_item_data)

            documents.append(documents_item)

        kyc_country_documents = cls(
            country=country,
            documents=documents,
        )

        return kyc_country_documents
