from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Projet")


@_attrs_define
class Projet:
    """
    Attributes:
        created_at (datetime.datetime):
        id (str):
        name (str):
        slug (str):
    """

    created_at: datetime.datetime
    id: str
    name: str
    slug: str

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = self.id

        name = self.name

        slug = self.slug

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "name": name,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        projet = cls(
            created_at=created_at,
            id=id,
            name=name,
            slug=slug,
        )

        return projet
