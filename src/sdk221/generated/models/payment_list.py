from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.payment import Payment


T = TypeVar("T", bound="PaymentList")


@_attrs_define
class PaymentList:
    """
    Attributes:
        data (list[Payment]):
        livemode (bool): true : objet du mode live ; false : mode test.
        next_cursor (None | str): À passer en ?cursor pour la page suivante ; null quand il n'y en a plus.
        total_count (int): Nombre d'éléments pour ces filtres, toutes pages confondues.
    """

    data: list[Payment]
    livemode: bool
    next_cursor: None | str
    total_count: int

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        livemode = self.livemode

        next_cursor: None | str
        next_cursor = self.next_cursor

        total_count = self.total_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "livemode": livemode,
                "next_cursor": next_cursor,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.payment import Payment

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Payment.from_dict(data_item_data)

            data.append(data_item)

        livemode = d.pop("livemode")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        total_count = d.pop("total_count")

        payment_list = cls(
            data=data,
            livemode=livemode,
            next_cursor=next_cursor,
            total_count=total_count,
        )

        return payment_list
