from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.source_verifiee_lang import SourceVerifieeLang

T = TypeVar("T", bound="SourceVerifiee")


@_attrs_define
class SourceVerifiee:
    """
    Attributes:
        lang (SourceVerifieeLang):
        official (bool):
        title (str):
        url (str):
        verified_on (datetime.date): Date de la dernière vérification de la source.
    """

    lang: SourceVerifieeLang
    official: bool
    title: str
    url: str
    verified_on: datetime.date

    def to_dict(self) -> dict[str, Any]:
        lang = self.lang.value

        official = self.official

        title = self.title

        url = self.url

        verified_on = self.verified_on.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lang": lang,
                "official": official,
                "title": title,
                "url": url,
                "verifiedOn": verified_on,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lang = SourceVerifieeLang(d.pop("lang"))

        official = d.pop("official")

        title = d.pop("title")

        url = d.pop("url")

        verified_on = datetime.date.fromisoformat(d.pop("verifiedOn"))

        source_verifiee = cls(
            lang=lang,
            official=official,
            title=title,
            url=url,
            verified_on=verified_on,
        )

        return source_verifiee
