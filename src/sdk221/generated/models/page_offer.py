from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.offer import Offer


T = TypeVar("T", bound="PageOffer")


@_attrs_define
class PageOffer:
    """
    Attributes:
        data (list[Offer]):
        livemode (bool): true : objet du mode live ; false : mode test.
        total_count (int): Nombre d'éléments pour ces filtres, toutes pages confondues.
    """

    data: list[Offer]
    livemode: bool
    total_count: int

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        livemode = self.livemode

        total_count = self.total_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "livemode": livemode,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.offer import Offer

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Offer.from_dict(data_item_data)

            data.append(data_item)

        livemode = d.pop("livemode")

        total_count = d.pop("total_count")

        page_offer = cls(
            data=data,
            livemode=livemode,
            total_count=total_count,
        )

        return page_offer
