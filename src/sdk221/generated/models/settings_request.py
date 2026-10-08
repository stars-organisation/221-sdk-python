from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.settings_request_refund_fee_payer_default import (
    SettingsRequestRefundFeePayerDefault,
)

T = TypeVar("T", bound="SettingsRequest")


@_attrs_define
class SettingsRequest:
    """
    Attributes:
        refund_fee_payer_default (SettingsRequestRefundFeePayerDefault):
    """

    refund_fee_payer_default: SettingsRequestRefundFeePayerDefault

    def to_dict(self) -> dict[str, Any]:
        refund_fee_payer_default = self.refund_fee_payer_default.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "refund_fee_payer_default": refund_fee_payer_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        refund_fee_payer_default = SettingsRequestRefundFeePayerDefault(
            d.pop("refund_fee_payer_default")
        )

        settings_request = cls(
            refund_fee_payer_default=refund_fee_payer_default,
        )

        return settings_request
