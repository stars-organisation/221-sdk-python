from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.bank_tier import BankTier


T = TypeVar("T", bound="Fees")


@_attrs_define
class Fees:
    """
    Attributes:
        bank_max (int): Montant maximum d'un virement bancaire, en XOF.
        bank_min (int): Montant minimum d'un virement bancaire, en XOF.
        bank_monthly_cap (int): Virements bancaires par marchand et par mois calendaire (heure de Dakar), en XOF.
        bank_tiers (list[BankTier]): Paliers des virements bancaires : le palier du montant entier donne le taux. EN:
            bank transfer tiers; the whole amount's tier gives the rate.
        livemode (bool): true : objet du mode live ; false : mode test.
    """

    bank_max: int
    bank_min: int
    bank_monthly_cap: int
    bank_tiers: list[BankTier]
    livemode: bool

    def to_dict(self) -> dict[str, Any]:
        bank_max = self.bank_max

        bank_min = self.bank_min

        bank_monthly_cap = self.bank_monthly_cap

        bank_tiers = []
        for bank_tiers_item_data in self.bank_tiers:
            bank_tiers_item = bank_tiers_item_data.to_dict()
            bank_tiers.append(bank_tiers_item)

        livemode = self.livemode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bank_max": bank_max,
                "bank_min": bank_min,
                "bank_monthly_cap": bank_monthly_cap,
                "bank_tiers": bank_tiers,
                "livemode": livemode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bank_tier import BankTier

        d = dict(src_dict)
        bank_max = d.pop("bank_max")

        bank_min = d.pop("bank_min")

        bank_monthly_cap = d.pop("bank_monthly_cap")

        bank_tiers = []
        _bank_tiers = d.pop("bank_tiers")
        for bank_tiers_item_data in _bank_tiers:
            bank_tiers_item = BankTier.from_dict(bank_tiers_item_data)

            bank_tiers.append(bank_tiers_item)

        livemode = d.pop("livemode")

        fees = cls(
            bank_max=bank_max,
            bank_min=bank_min,
            bank_monthly_cap=bank_monthly_cap,
            bank_tiers=bank_tiers,
            livemode=livemode,
        )

        return fees
