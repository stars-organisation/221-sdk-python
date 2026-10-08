from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.kyc_country_documents import KycCountryDocuments


T = TypeVar("T", bound="KycDocuments")


@_attrs_define
class KycDocuments:
    """
    Attributes:
        data (list[KycCountryDocuments]): Pièces acceptées par pays.
        livemode (bool): true : objet du mode live ; false : mode test.
    """

    data: list[KycCountryDocuments]
    livemode: bool

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        livemode = self.livemode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "livemode": livemode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kyc_country_documents import KycCountryDocuments

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = KycCountryDocuments.from_dict(data_item_data)

            data.append(data_item)

        livemode = d.pop("livemode")

        kyc_documents = cls(
            data=data,
            livemode=livemode,
        )

        return kyc_documents
