from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.offer_benefit_type import OfferBenefitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferBenefit")


@_attrs_define
class OfferBenefit:
    """
    Attributes:
        type_ (OfferBenefitType):
        value (str): percent : de 1 à 100 ; fixed : montant en XOF.
        max_amount (None | str | Unset): Plafond de la remise, pour un pourcentage seulement.
    """

    type_: OfferBenefitType
    value: str
    max_amount: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        max_amount: None | str | Unset
        if isinstance(self.max_amount, Unset):
            max_amount = UNSET
        else:
            max_amount = self.max_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )
        if max_amount is not UNSET:
            field_dict["max_amount"] = max_amount

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = OfferBenefitType(d.pop("type"))

        value = d.pop("value")

        def _parse_max_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_amount = _parse_max_amount(d.pop("max_amount", UNSET))

        offer_benefit = cls(
            type_=type_,
            value=value,
            max_amount=max_amount,
        )

        return offer_benefit
