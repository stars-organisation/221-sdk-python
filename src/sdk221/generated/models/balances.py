from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.balances_gateway_mode import BalancesGatewayMode

if TYPE_CHECKING:
    from ..models.balances_rails import BalancesRails


T = TypeVar("T", bound="Balances")


@_attrs_define
class Balances:
    """
    Attributes:
        gateway_mode (BalancesGatewayMode): simulated : mode test sans argent réel ; real : opérateur réel ; not_wired :
            aucun opérateur branché.
        livemode (bool): true : objet du mode live ; false : mode test.
        rails (BalancesRails): Un solde par moyen de paiement utilisé, clé = identifiant du moyen de paiement.
    """

    gateway_mode: BalancesGatewayMode
    livemode: bool
    rails: BalancesRails

    def to_dict(self) -> dict[str, Any]:
        gateway_mode = self.gateway_mode.value

        livemode = self.livemode

        rails = self.rails.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gateway_mode": gateway_mode,
                "livemode": livemode,
                "rails": rails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.balances_rails import BalancesRails

        d = dict(src_dict)
        gateway_mode = BalancesGatewayMode(d.pop("gateway_mode"))

        livemode = d.pop("livemode")

        rails = BalancesRails.from_dict(d.pop("rails"))

        balances = cls(
            gateway_mode=gateway_mode,
            livemode=livemode,
            rails=rails,
        )

        return balances
