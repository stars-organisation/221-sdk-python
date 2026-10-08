from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.offer_status import OfferStatus

if TYPE_CHECKING:
    from ..models.offer_benefit import OfferBenefit


T = TypeVar("T", bound="Offer")


@_attrs_define
class Offer:
    """
    Attributes:
        benefit (OfferBenefit):
        created_at (datetime.datetime):
        description (str):
        end_time (datetime.datetime | None):
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        max_order_amount (None | str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        min_order_amount (None | str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni
            décimale.
        offer_code (str):
        start_time (datetime.datetime | None):
        status (OfferStatus): deleted : réponse du DELETE ; l'offre n'est plus listée ni lisible.
        title (str):
        usage_count (int):
    """

    benefit: OfferBenefit
    created_at: datetime.datetime
    description: str
    end_time: datetime.datetime | None
    id: UUID
    livemode: bool
    max_order_amount: None | str
    min_order_amount: None | str
    offer_code: str
    start_time: datetime.datetime | None
    status: OfferStatus
    title: str
    usage_count: int

    def to_dict(self) -> dict[str, Any]:
        benefit = self.benefit.to_dict()

        created_at = self.created_at.isoformat()

        description = self.description

        end_time: None | str
        if isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        id = str(self.id)

        livemode = self.livemode

        max_order_amount: None | str
        max_order_amount = self.max_order_amount

        min_order_amount: None | str
        min_order_amount = self.min_order_amount

        offer_code = self.offer_code

        start_time: None | str
        if isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        status = self.status.value

        title = self.title

        usage_count = self.usage_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "benefit": benefit,
                "created_at": created_at,
                "description": description,
                "end_time": end_time,
                "id": id,
                "livemode": livemode,
                "max_order_amount": max_order_amount,
                "min_order_amount": min_order_amount,
                "offer_code": offer_code,
                "start_time": start_time,
                "status": status,
                "title": title,
                "usage_count": usage_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.offer_benefit import OfferBenefit

        d = dict(src_dict)
        benefit = OfferBenefit.from_dict(d.pop("benefit"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        def _parse_end_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = datetime.datetime.fromisoformat(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        end_time = _parse_end_time(d.pop("end_time"))

        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        def _parse_max_order_amount(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        max_order_amount = _parse_max_order_amount(d.pop("max_order_amount"))

        def _parse_min_order_amount(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        min_order_amount = _parse_min_order_amount(d.pop("min_order_amount"))

        offer_code = d.pop("offer_code")

        def _parse_start_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = datetime.datetime.fromisoformat(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        start_time = _parse_start_time(d.pop("start_time"))

        status = OfferStatus(d.pop("status"))

        title = d.pop("title")

        usage_count = d.pop("usage_count")

        offer = cls(
            benefit=benefit,
            created_at=created_at,
            description=description,
            end_time=end_time,
            id=id,
            livemode=livemode,
            max_order_amount=max_order_amount,
            min_order_amount=min_order_amount,
            offer_code=offer_code,
            start_time=start_time,
            status=status,
            title=title,
            usage_count=usage_count,
        )

        return offer
