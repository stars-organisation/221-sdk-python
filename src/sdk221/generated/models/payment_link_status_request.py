from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payment_link_status_request_status import PaymentLinkStatusRequestStatus

T = TypeVar("T", bound="PaymentLinkStatusRequest")


@_attrs_define
class PaymentLinkStatusRequest:
    """
    Attributes:
        status (PaymentLinkStatusRequestStatus): Un lien expiré ne peut pas être réactivé.
    """

    status: PaymentLinkStatusRequestStatus

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
        status = PaymentLinkStatusRequestStatus(d.pop("status"))

        payment_link_status_request = cls(
            status=status,
        )

        return payment_link_status_request
