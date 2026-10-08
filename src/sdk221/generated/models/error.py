from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_fields import ErrorFields


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        code (str):
        message (str):
        request_id (str): Identifiant de la requête, aussi dans l'en-tête X-Request-Id : à donner au support.
        fields (ErrorFields | Unset): Un message par champ refusé.
    """

    code: str
    message: str
    request_id: str
    fields: ErrorFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        request_id = self.request_id

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "request_id": request_id,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_fields import ErrorFields

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        request_id = d.pop("request_id")

        _fields = d.pop("fields", UNSET)
        fields: ErrorFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = ErrorFields.from_dict(_fields)

        error = cls(
            code=code,
            message=message,
            request_id=request_id,
            fields=fields,
        )

        error.additional_properties = d
        return error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
