from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.kyc_session_request_document_type import KycSessionRequestDocumentType

T = TypeVar("T", bound="KycSessionRequest")


@_attrs_define
class KycSessionRequest:
    """
    Attributes:
        country (str): Pays émetteur de la pièce, parmi ceux de GET /v1/kyc/documents.
        document_type (KycSessionRequestDocumentType):
    """

    country: str
    document_type: KycSessionRequestDocumentType

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        document_type = self.document_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "document_type": document_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        country = d.pop("country")

        document_type = KycSessionRequestDocumentType(d.pop("document_type"))

        kyc_session_request = cls(
            country=country,
            document_type=document_type,
        )

        return kyc_session_request
