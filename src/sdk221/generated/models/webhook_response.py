from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="WebhookResponse")


@_attrs_define
class WebhookResponse:
    """
    Attributes:
        body (Any): Corps répondu par votre endpoint.
        error_message (None | str):
        headers (Any): Toujours vide pour l'instant.
        status_code (int | None): null si l'endpoint n'a pas répondu.
    """

    body: Any
    error_message: None | str
    headers: Any
    status_code: int | None

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        error_message: None | str
        error_message = self.error_message

        headers = self.headers

        status_code: int | None
        status_code = self.status_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "body": body,
                "error_message": error_message,
                "headers": headers,
                "status_code": status_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        body = d.pop("body")

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))

        headers = d.pop("headers")

        def _parse_status_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status_code = _parse_status_code(d.pop("status_code"))

        webhook_response = cls(
            body=body,
            error_message=error_message,
            headers=headers,
            status_code=status_code,
        )

        return webhook_response
