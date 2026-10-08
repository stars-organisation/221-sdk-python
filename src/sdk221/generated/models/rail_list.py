from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.rail_list_currency import RailListCurrency

if TYPE_CHECKING:
    from ..models.rail import Rail


T = TypeVar("T", bound="RailList")


@_attrs_define
class RailList:
    """
    Attributes:
        currency (RailListCurrency):
        data (list[Rail]):
        livemode (bool): true : objet du mode live ; false : mode test.
    """

    currency: RailListCurrency
    data: list[Rail]
    livemode: bool

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency.value

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        livemode = self.livemode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "data": data,
                "livemode": livemode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rail import Rail

        d = dict(src_dict)
        currency = RailListCurrency(d.pop("currency"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Rail.from_dict(data_item_data)

            data.append(data_item)

        livemode = d.pop("livemode")

        rail_list = cls(
            currency=currency,
            data=data,
            livemode=livemode,
        )

        return rail_list
