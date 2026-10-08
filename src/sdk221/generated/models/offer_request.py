from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.offer_benefit import OfferBenefit


T = TypeVar("T", bound="OfferRequest")


@_attrs_define
class OfferRequest:
    """
    Attributes:
        benefit (OfferBenefit):
        offer_code (str): Mis en majuscules ; unique par projet.
        title (str):
        description (str | Unset):
        end_time (datetime.datetime | None | Unset): Postérieure à start_time.
        max_order_amount (None | str | Unset): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans
            espace ni décimale.
        min_order_amount (None | str | Unset): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans
            espace ni décimale.
        start_time (datetime.datetime | None | Unset):
    """

    benefit: OfferBenefit
    offer_code: str
    title: str
    description: str | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    max_order_amount: None | str | Unset = UNSET
    min_order_amount: None | str | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        benefit = self.benefit.to_dict()

        offer_code = self.offer_code

        title = self.title

        description = self.description

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        max_order_amount: None | str | Unset
        if isinstance(self.max_order_amount, Unset):
            max_order_amount = UNSET
        else:
            max_order_amount = self.max_order_amount

        min_order_amount: None | str | Unset
        if isinstance(self.min_order_amount, Unset):
            min_order_amount = UNSET
        else:
            min_order_amount = self.min_order_amount

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "benefit": benefit,
                "offer_code": offer_code,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if max_order_amount is not UNSET:
            field_dict["max_order_amount"] = max_order_amount
        if min_order_amount is not UNSET:
            field_dict["min_order_amount"] = min_order_amount
        if start_time is not UNSET:
            field_dict["start_time"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.offer_benefit import OfferBenefit

        d = dict(src_dict)
        benefit = OfferBenefit.from_dict(d.pop("benefit"))

        offer_code = d.pop("offer_code")

        title = d.pop("title")

        description = d.pop("description", UNSET)

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_max_order_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_order_amount = _parse_max_order_amount(d.pop("max_order_amount", UNSET))

        def _parse_min_order_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        min_order_amount = _parse_min_order_amount(d.pop("min_order_amount", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        offer_request = cls(
            benefit=benefit,
            offer_code=offer_code,
            title=title,
            description=description,
            end_time=end_time,
            max_order_amount=max_order_amount,
            min_order_amount=min_order_amount,
            start_time=start_time,
        )

        return offer_request
