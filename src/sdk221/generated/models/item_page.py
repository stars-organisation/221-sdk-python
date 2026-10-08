from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.pagination import Pagination


T = TypeVar("T", bound="ItemPage")


@_attrs_define
class ItemPage:
    """
    Attributes:
        data (list[Any] | None):
        pagination (Pagination):
    """

    data: list[Any] | None
    pagination: Pagination

    def to_dict(self) -> dict[str, Any]:
        data: list[Any] | None
        if isinstance(self.data, list):
            data = self.data

        else:
            data = self.data

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
        from ..models.pagination import Pagination

        d = dict(src_dict)

        def _parse_data(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = cast(list[Any], data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        data = _parse_data(d.pop("data"))

        pagination = Pagination.from_dict(d.pop("pagination"))

        item_page = cls(
            data=data,
            pagination=pagination,
        )

        return item_page
