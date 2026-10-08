from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Suivi")


@_attrs_define
class Suivi:
    """
    Attributes:
        active (bool):
        created_at (datetime.datetime):
        dataset (str):
    """

    active: bool
    created_at: datetime.datetime
    dataset: str

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        created_at = self.created_at.isoformat()

        dataset = self.dataset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
                "created_at": created_at,
                "dataset": dataset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active = d.pop("active")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        dataset = d.pop("dataset")

        suivi = cls(
            active=active,
            created_at=created_at,
            dataset=dataset,
        )

        return suivi
