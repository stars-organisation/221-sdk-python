from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="AppelJournal")


@_attrs_define
class AppelJournal:
    """
    Attributes:
        created_at (datetime.datetime):
        duration_ms (int):
        id (int):
        key_id (str):
        method (str):
        path (str):
        prefix (str):
        status (int):
    """

    created_at: datetime.datetime
    duration_ms: int
    id: int
    key_id: str
    method: str
    path: str
    prefix: str
    status: int

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        duration_ms = self.duration_ms

        id = self.id

        key_id = self.key_id

        method = self.method

        path = self.path

        prefix = self.prefix

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "duration_ms": duration_ms,
                "id": id,
                "key_id": key_id,
                "method": method,
                "path": path,
                "prefix": prefix,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        duration_ms = d.pop("duration_ms")

        id = d.pop("id")

        key_id = d.pop("key_id")

        method = d.pop("method")

        path = d.pop("path")

        prefix = d.pop("prefix")

        status = d.pop("status")

        appel_journal = cls(
            created_at=created_at,
            duration_ms=duration_ms,
            id=id,
            key_id=key_id,
            method=method,
            path=path,
            prefix=prefix,
            status=status,
        )

        return appel_journal
