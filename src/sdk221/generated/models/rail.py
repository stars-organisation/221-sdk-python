from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.rail_platform_state import RailPlatformState
from ..models.rail_rail import RailRail

if TYPE_CHECKING:
    from ..models.rail_fees_type_0 import RailFeesType0


T = TypeVar("T", bound="Rail")


@_attrs_define
class Rail:
    """
    Attributes:
        country (str): Code pays ISO 3166-1 alpha-2.
        country_label (str):
        enabled_for_project (bool | None): Activé sur le projet de l'appelant ; null sans identification.
        fees (None | RailFeesType0):
        label (str):
        livemode (bool): true : objet du mode live ; false : mode test.
        min_amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        operator (str):
        operator_label (str):
        otp_required (bool): true : le client compose un code et vous le passez dans customer_otp.
        platform_state (RailPlatformState): Un moyen de paiement encaisse quand il est activé sur le projet et que
            platform_state vaut open.
        rail (RailRail): Moyen de paiement : pays et opérateur (liste et état : GET /v1/rails).
    """

    country: str
    country_label: str
    enabled_for_project: bool | None
    fees: None | RailFeesType0
    label: str
    livemode: bool
    min_amount: str
    operator: str
    operator_label: str
    otp_required: bool
    platform_state: RailPlatformState
    rail: RailRail

    def to_dict(self) -> dict[str, Any]:
        from ..models.rail_fees_type_0 import RailFeesType0

        country = self.country

        country_label = self.country_label

        enabled_for_project: bool | None
        enabled_for_project = self.enabled_for_project

        fees: dict[str, Any] | None
        if isinstance(self.fees, RailFeesType0):
            fees = self.fees.to_dict()
        else:
            fees = self.fees

        label = self.label

        livemode = self.livemode

        min_amount = self.min_amount

        operator = self.operator

        operator_label = self.operator_label

        otp_required = self.otp_required

        platform_state = self.platform_state.value

        rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "country_label": country_label,
                "enabled_for_project": enabled_for_project,
                "fees": fees,
                "label": label,
                "livemode": livemode,
                "min_amount": min_amount,
                "operator": operator,
                "operator_label": operator_label,
                "otp_required": otp_required,
                "platform_state": platform_state,
                "rail": rail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rail_fees_type_0 import RailFeesType0

        d = dict(src_dict)
        country = d.pop("country")

        country_label = d.pop("country_label")

        def _parse_enabled_for_project(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        enabled_for_project = _parse_enabled_for_project(d.pop("enabled_for_project"))

        def _parse_fees(data: object) -> None | RailFeesType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_rail_fees_type_0 = RailFeesType0.from_dict(data)

                return componentsschemas_rail_fees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RailFeesType0, data)

        fees = _parse_fees(d.pop("fees"))

        label = d.pop("label")

        livemode = d.pop("livemode")

        min_amount = d.pop("min_amount")

        operator = d.pop("operator")

        operator_label = d.pop("operator_label")

        otp_required = d.pop("otp_required")

        platform_state = RailPlatformState(d.pop("platform_state"))

        rail = RailRail(d.pop("rail"))

        rail = cls(
            country=country,
            country_label=country_label,
            enabled_for_project=enabled_for_project,
            fees=fees,
            label=label,
            livemode=livemode,
            min_amount=min_amount,
            operator=operator,
            operator_label=operator_label,
            otp_required=otp_required,
            platform_state=platform_state,
            rail=rail,
        )

        return rail
