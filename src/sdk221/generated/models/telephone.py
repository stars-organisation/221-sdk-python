from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.operateur_telephone_type_0 import OperateurTelephoneType0


T = TypeVar("T", bound="Telephone")


@_attrs_define
class Telephone:
    """
    Attributes:
        country (None | str):
        e164 (str):
        input_ (str):
        international (str):
        national (str):
        notice (str):
        operator (None | OperateurTelephoneType0):
        senegalese (bool):
        type_ (None | str):
        valid (bool):
    """

    country: None | str
    e164: str
    input_: str
    international: str
    national: str
    notice: str
    operator: None | OperateurTelephoneType0
    senegalese: bool
    type_: None | str
    valid: bool

    def to_dict(self) -> dict[str, Any]:
        from ..models.operateur_telephone_type_0 import (
            OperateurTelephoneType0,
        )

        country: None | str
        country = self.country

        e164 = self.e164

        input_ = self.input_

        international = self.international

        national = self.national

        notice = self.notice

        operator: dict[str, Any] | None
        if isinstance(self.operator, OperateurTelephoneType0):
            operator = self.operator.to_dict()
        else:
            operator = self.operator

        senegalese = self.senegalese

        type_: None | str
        type_ = self.type_

        valid = self.valid

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "e164": e164,
                "input": input_,
                "international": international,
                "national": national,
                "notice": notice,
                "operator": operator,
                "senegalese": senegalese,
                "type": type_,
                "valid": valid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.operateur_telephone_type_0 import (
            OperateurTelephoneType0,
        )

        d = dict(src_dict)

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        e164 = d.pop("e164")

        input_ = d.pop("input")

        international = d.pop("international")

        national = d.pop("national")

        notice = d.pop("notice")

        def _parse_operator(data: object) -> None | OperateurTelephoneType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operateur_telephone_type_0 = (
                    OperateurTelephoneType0.from_dict(data)
                )

                return componentsschemas_operateur_telephone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OperateurTelephoneType0, data)

        operator = _parse_operator(d.pop("operator"))

        senegalese = d.pop("senegalese")

        def _parse_type_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        type_ = _parse_type_(d.pop("type"))

        valid = d.pop("valid")

        telephone = cls(
            country=country,
            e164=e164,
            input_=input_,
            international=international,
            national=national,
            notice=notice,
            operator=operator,
            senegalese=senegalese,
            type_=type_,
            valid=valid,
        )

        return telephone
