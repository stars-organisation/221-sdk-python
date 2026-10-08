from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Source")


@_attrs_define
class Source:
    """
    Attributes:
        licence (str):
        official (bool):
        title (str):
        url (str):
    """

    licence: str
    official: bool
    title: str
    url: str

    def to_dict(self) -> dict[str, Any]:
        licence = self.licence

        official = self.official

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "licence": licence,
                "official": official,
                "title": title,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        licence = d.pop("licence")

        official = d.pop("official")

        title = d.pop("title")

        url = d.pop("url")

        source = cls(
            licence=licence,
            official=official,
            title=title,
            url=url,
        )

        return source
