from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="WebhookRequest")


@_attrs_define
class WebhookRequest:
    """
    Attributes:
        body (Any): Corps envoyé à votre endpoint.
        headers (Any): En-têtes envoyés, signature comprise.
    """

    body: Any
    headers: Any

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        headers = self.headers

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "body": body,
                "headers": headers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        body = d.pop("body")

        headers = d.pop("headers")

        webhook_request = cls(
            body=body,
            headers=headers,
        )

        return webhook_request
