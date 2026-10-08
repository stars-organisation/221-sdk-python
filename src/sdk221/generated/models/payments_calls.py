from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.payments_calls_day import PaymentsCallsDay


T = TypeVar("T", bound="PaymentsCalls")


@_attrs_define
class PaymentsCalls:
    """
    Attributes:
        errors_today (int):
        last_14_days (list[PaymentsCallsDay] | None): Du plus ancien au jour courant.
        today (int):
    """

    errors_today: int
    last_14_days: list[PaymentsCallsDay] | None
    today: int

    def to_dict(self) -> dict[str, Any]:
        errors_today = self.errors_today

        last_14_days: list[dict[str, Any]] | None
        if isinstance(self.last_14_days, list):
            last_14_days = []
            for last_14_days_type_0_item_data in self.last_14_days:
                last_14_days_type_0_item = last_14_days_type_0_item_data.to_dict()
                last_14_days.append(last_14_days_type_0_item)

        else:
            last_14_days = self.last_14_days

        today = self.today

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "errors_today": errors_today,
                "last_14_days": last_14_days,
                "today": today,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.payments_calls_day import PaymentsCallsDay

        d = dict(src_dict)
        errors_today = d.pop("errors_today")

        def _parse_last_14_days(data: object) -> list[PaymentsCallsDay] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                last_14_days_type_0 = []
                _last_14_days_type_0 = data
                for last_14_days_type_0_item_data in _last_14_days_type_0:
                    last_14_days_type_0_item = PaymentsCallsDay.from_dict(
                        last_14_days_type_0_item_data
                    )

                    last_14_days_type_0.append(last_14_days_type_0_item)

                return last_14_days_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PaymentsCallsDay] | None, data)

        last_14_days = _parse_last_14_days(d.pop("last_14_days"))

        today = d.pop("today")

        payments_calls = cls(
            errors_today=errors_today,
            last_14_days=last_14_days,
            today=today,
        )

        return payments_calls
