from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.next_action_type_0_type import NextActionType0Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="NextActionType0")


@_attrs_define
class NextActionType0:
    """
    Attributes:
        type_ (NextActionType0Type): Ce qu'il faut montrer en premier au client.
        message (str | Unset): Consigne à afficher (type instruction).
        qr_code (str | Unset): Code à scanner (type qr).
        url (str | Unset): Page à ouvrir (type redirect).
    """

    type_: NextActionType0Type
    message: str | Unset = UNSET
    qr_code: str | Unset = UNSET
    url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        message = self.message

        qr_code = self.qr_code

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if qr_code is not UNSET:
            field_dict["qr_code"] = qr_code
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = NextActionType0Type(d.pop("type"))

        message = d.pop("message", UNSET)

        qr_code = d.pop("qr_code", UNSET)

        url = d.pop("url", UNSET)

        next_action_type_0 = cls(
            type_=type_,
            message=message,
            qr_code=qr_code,
            url=url,
        )

        return next_action_type_0
