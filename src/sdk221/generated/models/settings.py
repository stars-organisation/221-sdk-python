from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.settings_rails_enabled_item import SettingsRailsEnabledItem
from ..models.settings_refund_fee_payer_default import SettingsRefundFeePayerDefault
from ..types import UNSET, Unset

T = TypeVar("T", bound="Settings")


@_attrs_define
class Settings:
    """
    Attributes:
        livemode (bool): true : objet du mode live ; false : mode test.
        refund_fee_payer_default (SettingsRefundFeePayerDefault):
        rails_enabled (list[SettingsRailsEnabledItem] | Unset): Moyens de paiement activés (absent de la réponse du
            PUT). Se modifie par PUT /v1/rails/{id}/enabled.
        rate_limit_per_minute (int | Unset): Requêtes autorisées par minute et par projet (absent de la réponse du PUT)
            ; au-delà : RATE_LIMITED.
    """

    livemode: bool
    refund_fee_payer_default: SettingsRefundFeePayerDefault
    rails_enabled: list[SettingsRailsEnabledItem] | Unset = UNSET
    rate_limit_per_minute: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        livemode = self.livemode

        refund_fee_payer_default = self.refund_fee_payer_default.value

        rails_enabled: list[str] | Unset = UNSET
        if not isinstance(self.rails_enabled, Unset):
            rails_enabled = []
            for rails_enabled_item_data in self.rails_enabled:
                rails_enabled_item = rails_enabled_item_data.value
                rails_enabled.append(rails_enabled_item)

        rate_limit_per_minute = self.rate_limit_per_minute

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "livemode": livemode,
                "refund_fee_payer_default": refund_fee_payer_default,
            }
        )
        if rails_enabled is not UNSET:
            field_dict["rails_enabled"] = rails_enabled
        if rate_limit_per_minute is not UNSET:
            field_dict["rate_limit_per_minute"] = rate_limit_per_minute

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        livemode = d.pop("livemode")

        refund_fee_payer_default = SettingsRefundFeePayerDefault(
            d.pop("refund_fee_payer_default")
        )

        _rails_enabled = d.pop("rails_enabled", UNSET)
        rails_enabled: list[SettingsRailsEnabledItem] | Unset = UNSET
        if _rails_enabled is not UNSET:
            rails_enabled = []
            for rails_enabled_item_data in _rails_enabled:
                rails_enabled_item = SettingsRailsEnabledItem(rails_enabled_item_data)

                rails_enabled.append(rails_enabled_item)

        rate_limit_per_minute = d.pop("rate_limit_per_minute", UNSET)

        settings = cls(
            livemode=livemode,
            refund_fee_payer_default=refund_fee_payer_default,
            rails_enabled=rails_enabled,
            rate_limit_per_minute=rate_limit_per_minute,
        )

        return settings
