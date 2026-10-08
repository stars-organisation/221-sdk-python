from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from .. import types
from ..models.dispute_evidence_upload_evidence_type import (
    DisputeEvidenceUploadEvidenceType,
)
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="DisputeEvidenceUpload")


@_attrs_define
class DisputeEvidenceUpload:
    """
    Attributes:
        evidence_type (DisputeEvidenceUploadEvidenceType):
        file (File): JPEG, PNG ou PDF, 5 Mo au plus : le type est vérifié sur le contenu du fichier.
        dispute_id (UUID | Unset): Facultatif ; doit être celui de l'URL.
    """

    evidence_type: DisputeEvidenceUploadEvidenceType
    file: File
    dispute_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        evidence_type = self.evidence_type.value

        file = self.file.to_tuple()

        dispute_id: str | Unset = UNSET
        if not isinstance(self.dispute_id, Unset):
            dispute_id = str(self.dispute_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "evidence_type": evidence_type,
                "file": file,
            }
        )
        if dispute_id is not UNSET:
            field_dict["dispute_id"] = dispute_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(
            (
                "evidence_type",
                (None, str(self.evidence_type.value).encode(), "text/plain"),
            )
        )

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.dispute_id, Unset):
            files.append(("dispute_id", (None, str(self.dispute_id), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        evidence_type = DisputeEvidenceUploadEvidenceType(d.pop("evidence_type"))

        file = File(payload=BytesIO(d.pop("file")))

        _dispute_id = d.pop("dispute_id", UNSET)
        dispute_id: UUID | Unset
        if isinstance(_dispute_id, Unset):
            dispute_id = UNSET
        else:
            dispute_id = UUID(_dispute_id)

        dispute_evidence_upload = cls(
            evidence_type=evidence_type,
            file=file,
            dispute_id=dispute_id,
        )

        return dispute_evidence_upload
