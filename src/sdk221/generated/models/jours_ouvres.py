from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="JoursOuvres")


@_attrs_define
class JoursOuvres:
    """
    Attributes:
        business_days (int):
        from_ (str):
        holidays (list[str] | None):
        to (str):
        warnings (list[str] | None):
    """

    business_days: int
    from_: str
    holidays: list[str] | None
    to: str
    warnings: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        business_days = self.business_days

        from_ = self.from_

        holidays: list[str] | None
        if isinstance(self.holidays, list):
            holidays = self.holidays

        else:
            holidays = self.holidays

        to = self.to

        warnings: list[str] | None
        if isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "business_days": business_days,
                "from": from_,
                "holidays": holidays,
                "to": to,
                "warnings": warnings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        business_days = d.pop("business_days")

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

        to = d.pop("to")

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

        jours_ouvres = cls(
            business_days=business_days,
            from_=from_,
            holidays=holidays,
            to=to,
            warnings=warnings,
        )

        return jours_ouvres
