from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="DisputeChallengeRequest")


@_attrs_define
class DisputeChallengeRequest:
    """
    Attributes:
        file_ids (list[UUID]): Pièces déjà envoyées au litige, distinctes.
    """

    file_ids: list[UUID]

    def to_dict(self) -> dict[str, Any]:
        file_ids = []
        for file_ids_item_data in self.file_ids:
            file_ids_item = str(file_ids_item_data)
            file_ids.append(file_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file_ids": file_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_ids = []
        _file_ids = d.pop("file_ids")
        for file_ids_item_data in _file_ids:
            file_ids_item = UUID(file_ids_item_data)

            file_ids.append(file_ids_item)

        dispute_challenge_request = cls(
            file_ids=file_ids,
        )

        return dispute_challenge_request
