from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.kyc_capture_name import KycCaptureName

T = TypeVar("T", bound="KycCapture")


@_attrs_define
class KycCapture:
    """
    Attributes:
        content_types (list[str]):
        expires_at (datetime.datetime):
        max_bytes (int):
        method (str):
        name (KycCaptureName):
        url (str): Lien d'envoi signé : l'image part directement du navigateur ou du téléphone.
    """

    content_types: list[str]
    expires_at: datetime.datetime
    max_bytes: int
    method: str
    name: KycCaptureName
    url: str

    def to_dict(self) -> dict[str, Any]:
        content_types = self.content_types

        expires_at = self.expires_at.isoformat()

        max_bytes = self.max_bytes

        method = self.method

        name = self.name.value

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content_types": content_types,
                "expires_at": expires_at,
                "max_bytes": max_bytes,
                "method": method,
                "name": name,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        content_types = cast(list[str], d.pop("content_types"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        max_bytes = d.pop("max_bytes")

        method = d.pop("method")

        name = KycCaptureName(d.pop("name"))

        url = d.pop("url")

        kyc_capture = cls(
            content_types=content_types,
            expires_at=expires_at,
            max_bytes=max_bytes,
            method=method,
            name=name,
            url=url,
        )

        return kyc_capture
