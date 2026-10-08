from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Suivi")


@_attrs_define
class Suivi:
    """
    Attributes:
        active (bool):
        created_at (datetime.datetime | None):
        dataset (str):
    """

    active: bool
    created_at: datetime.datetime | None
    dataset: str

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

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

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))

        dataset = d.pop("dataset")

        suivi = cls(
            active=active,
            created_at=created_at,
            dataset=dataset,
        )

        return suivi
