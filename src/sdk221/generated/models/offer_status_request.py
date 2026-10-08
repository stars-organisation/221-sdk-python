from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.offer_status_request_status import OfferStatusRequestStatus

T = TypeVar("T", bound="OfferStatusRequest")


@_attrs_define
class OfferStatusRequest:
    """
    Attributes:
        status (OfferStatusRequestStatus):
    """

    status: OfferStatusRequestStatus

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = OfferStatusRequestStatus(d.pop("status"))

        offer_status_request = cls(
            status=status,
        )

        return offer_status_request
