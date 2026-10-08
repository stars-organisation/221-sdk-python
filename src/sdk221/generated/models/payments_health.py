from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payments_health_gateway_mode import PaymentsHealthGatewayMode

T = TypeVar("T", bound="PaymentsHealth")


@_attrs_define
class PaymentsHealth:
    """
    Attributes:
        gateway_mode (PaymentsHealthGatewayMode): simulated : aucun argent réel ne circule.
        mode (str):
        ready (bool):
    """

    gateway_mode: PaymentsHealthGatewayMode
    mode: str
    ready: bool

    def to_dict(self) -> dict[str, Any]:
        gateway_mode = self.gateway_mode.value

        mode = self.mode

        ready = self.ready

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gateway_mode": gateway_mode,
                "mode": mode,
                "ready": ready,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gateway_mode = PaymentsHealthGatewayMode(d.pop("gateway_mode"))

        mode = d.pop("mode")

        ready = d.pop("ready")

        payments_health = cls(
            gateway_mode=gateway_mode,
            mode=mode,
            ready=ready,
        )

        return payments_health
