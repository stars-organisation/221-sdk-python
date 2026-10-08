from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.payout import Payout


T = TypeVar("T", bound="CollectionPayout")


@_attrs_define
class CollectionPayout:
    """
    Attributes:
        data (list[Payout]):
        livemode (bool): true : objet du mode live ; false : mode test.
    """

    data: list[Payout]
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
        from ..models.payout import Payout

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Payout.from_dict(data_item_data)

            data.append(data_item)

        livemode = d.pop("livemode")

        collection_payout = cls(
            data=data,
            livemode=livemode,
        )

        return collection_payout
