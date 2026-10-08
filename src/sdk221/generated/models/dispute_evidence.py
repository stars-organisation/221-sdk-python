from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.dispute_evidence_evidence_type import DisputeEvidenceEvidenceType

T = TypeVar("T", bound="DisputeEvidence")


@_attrs_define
class DisputeEvidence:
    """
    Attributes:
        created_at (datetime.datetime):
        evidence_type (DisputeEvidenceEvidenceType):
        file_name (str):
        id (UUID):
        size (int): Octets.
    """

    created_at: datetime.datetime
    evidence_type: DisputeEvidenceEvidenceType
    file_name: str
    id: UUID
    size: int

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        evidence_type = self.evidence_type.value

        file_name = self.file_name

        id = str(self.id)

        size = self.size

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "evidence_type": evidence_type,
                "file_name": file_name,
                "id": id,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        evidence_type = DisputeEvidenceEvidenceType(d.pop("evidence_type"))

        file_name = d.pop("file_name")

        id = UUID(d.pop("id"))

        size = d.pop("size")

        dispute_evidence = cls(
            created_at=created_at,
            evidence_type=evidence_type,
            file_name=file_name,
            id=id,
            size=size,
        )

        return dispute_evidence
