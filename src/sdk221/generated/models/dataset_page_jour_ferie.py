from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.jour_ferie import JourFerie
    from ..models.pagination import Pagination


T = TypeVar("T", bound="DatasetPageJourFerie")


@_attrs_define
class DatasetPageJourFerie:
    """
    Attributes:
        data (list[JourFerie]):
        pagination (Pagination):
    """

    data: list[JourFerie]
    pagination: Pagination

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "pagination": pagination,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.jour_ferie import JourFerie
        from ..models.pagination import Pagination

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = JourFerie.from_dict(data_item_data)

            data.append(data_item)

        pagination = Pagination.from_dict(d.pop("pagination"))

        dataset_page_jour_ferie = cls(
            data=data,
            pagination=pagination,
        )

        return dataset_page_jour_ferie
