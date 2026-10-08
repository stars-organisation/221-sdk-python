from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="SuiviLigne")


@_attrs_define
class SuiviLigne:
    """
    Attributes:
        created_at (datetime.datetime):
        dataset (str):
    """

    created_at: datetime.datetime
    dataset: str

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset = self.dataset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "dataset": dataset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        dataset = d.pop("dataset")

        suivi_ligne = cls(
            created_at=created_at,
            dataset=dataset,
        )

        return suivi_ligne
