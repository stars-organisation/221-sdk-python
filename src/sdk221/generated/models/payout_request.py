from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PayoutRequest")


@_attrs_define
class PayoutRequest:
    """
    Attributes:
        quote_hash (str):
    """

    quote_hash: str

    def to_dict(self) -> dict[str, Any]:
        quote_hash = self.quote_hash

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quote_hash": quote_hash,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        quote_hash = d.pop("quote_hash")

        payout_request = cls(
            quote_hash=quote_hash,
        )

        return payout_request
