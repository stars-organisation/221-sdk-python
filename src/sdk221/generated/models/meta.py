from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """
    Attributes:
        attribution (str):
        licence (str):
        source (str):
        verified_on (None | str):
        version (None | str):
    """

    attribution: str
    licence: str
    source: str
    verified_on: None | str
    version: None | str

    def to_dict(self) -> dict[str, Any]:
        attribution = self.attribution

        licence = self.licence

        source = self.source

        verified_on: None | str
        verified_on = self.verified_on

        version: None | str
        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attribution": attribution,
                "licence": licence,
                "source": source,
                "verified_on": verified_on,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attribution = d.pop("attribution")

        licence = d.pop("licence")

        source = d.pop("source")

        def _parse_verified_on(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        verified_on = _parse_verified_on(d.pop("verified_on"))

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        meta = cls(
            attribution=attribution,
            licence=licence,
            source=source,
            verified_on=verified_on,
            version=version,
        )

        return meta
