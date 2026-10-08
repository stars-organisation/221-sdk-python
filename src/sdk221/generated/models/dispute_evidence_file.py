from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="DisputeEvidenceFile")


@_attrs_define
class DisputeEvidenceFile:
    """
    Attributes:
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
    """

    id: UUID
    livemode: bool

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        livemode = self.livemode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "livemode": livemode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        dispute_evidence_file = cls(
            id=id,
            livemode=livemode,
        )

        return dispute_evidence_file
