from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="DestinationVerification")


@_attrs_define
class DestinationVerification:
    """
    Attributes:
        attempts_left (int):
        expires_at (datetime.datetime): Fin de validité du dernier code envoyé (10 minutes).
    """

    attempts_left: int
    expires_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        attempts_left = self.attempts_left

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts_left": attempts_left,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attempts_left = d.pop("attempts_left")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        destination_verification = cls(
            attempts_left=attempts_left,
            expires_at=expires_at,
        )

        return destination_verification
