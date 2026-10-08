from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.cle_appelante_mode import CleAppelanteMode

T = TypeVar("T", bound="CleAppelante")


@_attrs_define
class CleAppelante:
    """
    Attributes:
        mode (CleAppelanteMode):
        name (str):
        project_id (str):
        scopes (list[str] | None):
    """

    mode: CleAppelanteMode
    name: str
    project_id: str
    scopes: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        name = self.name

        project_id = self.project_id

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
                "name": name,
                "project_id": project_id,
                "scopes": scopes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = CleAppelanteMode(d.pop("mode"))

        name = d.pop("name")

        project_id = d.pop("project_id")

        def _parse_scopes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        scopes = _parse_scopes(d.pop("scopes"))

        cle_appelante = cls(
            mode=mode,
            name=name,
            project_id=project_id,
            scopes=scopes,
        )

        return cle_appelante
