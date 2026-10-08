from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Delai")


@_attrs_define
class Delai:
    """
    Attributes:
        date (str):
        days (int):
        from_ (str):
        holidays (list[str] | None):
        warnings (list[str] | None):
    """

    date: str
    days: int
    from_: str
    holidays: list[str] | None
    warnings: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        days = self.days

        from_ = self.from_

        holidays: list[str] | None
        if isinstance(self.holidays, list):
            holidays = self.holidays

        else:
            holidays = self.holidays

        warnings: list[str] | None
        if isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "days": days,
                "from": from_,
                "holidays": holidays,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = d.pop("date")

        days = d.pop("days")

        from_ = d.pop("from")

        def _parse_holidays(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                holidays_type_0 = cast(list[str], data)

                return holidays_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        holidays = _parse_holidays(d.pop("holidays"))

        def _parse_warnings(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        warnings = _parse_warnings(d.pop("warnings"))

        delai = cls(
            date=date,
            days=days,
            from_=from_,
            holidays=holidays,
            warnings=warnings,
        )

        return delai
