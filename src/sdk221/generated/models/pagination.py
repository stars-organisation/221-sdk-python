from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        page (int):
        per_page (int):
        total (int):
        total_pages (int):
    """

    page: int
    per_page: int
    total: int
    total_pages: int

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        per_page = self.per_page

        total = self.total

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "page": page,
                "per_page": per_page,
                "total": total,
                "total_pages": total_pages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        page = d.pop("page")

        per_page = d.pop("per_page")

        total = d.pop("total")

        total_pages = d.pop("total_pages")

        pagination = cls(
            page=page,
            per_page=per_page,
            total=total,
            total_pages=total_pages,
        )

        return pagination
