from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.nouvelle_cle_body_expires_in import NouvelleCleBodyExpiresIn
from ..models.nouvelle_cle_body_mode import NouvelleCleBodyMode
from ..models.nouvelle_cle_body_scopes_type_0_item import NouvelleCleBodyScopesType0Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="NouvelleCleBody")


@_attrs_define
class NouvelleCleBody:
    """
    Attributes:
        name (str):
        daily_limit (int | Unset):
        expires_in (NouvelleCleBodyExpiresIn | Unset): Durée de validité : never (sans expiration), 30d, 90d ou 1y.
            Default: NouvelleCleBodyExpiresIn.NEVER.
        mode (NouvelleCleBodyMode | Unset): test (par défaut) ou live, une fois le mode live du projet activé. Default:
            NouvelleCleBodyMode.TEST.
        scopes (list[NouvelleCleBodyScopesType0Item] | None | Unset): Produits autorisés ; par défaut les deux.
    """

    name: str
    daily_limit: int | Unset = UNSET
    expires_in: NouvelleCleBodyExpiresIn | Unset = NouvelleCleBodyExpiresIn.NEVER
    mode: NouvelleCleBodyMode | Unset = NouvelleCleBodyMode.TEST
    scopes: list[NouvelleCleBodyScopesType0Item] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        daily_limit = self.daily_limit

        expires_in: str | Unset = UNSET
        if not isinstance(self.expires_in, Unset):
            expires_in = self.expires_in.value

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = []
            for scopes_type_0_item_data in self.scopes:
                scopes_type_0_item = scopes_type_0_item_data.value
                scopes.append(scopes_type_0_item)

        else:
            scopes = self.scopes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if daily_limit is not UNSET:
            field_dict["daily_limit"] = daily_limit
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if mode is not UNSET:
            field_dict["mode"] = mode
        if scopes is not UNSET:
            field_dict["scopes"] = scopes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        daily_limit = d.pop("daily_limit", UNSET)

        _expires_in = d.pop("expires_in", UNSET)
        expires_in: NouvelleCleBodyExpiresIn | Unset
        if isinstance(_expires_in, Unset):
            expires_in = UNSET
        else:
            expires_in = NouvelleCleBodyExpiresIn(_expires_in)

        _mode = d.pop("mode", UNSET)
        mode: NouvelleCleBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = NouvelleCleBodyMode(_mode)

        def _parse_scopes(
            data: object,
        ) -> list[NouvelleCleBodyScopesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = []
                _scopes_type_0 = data
                for scopes_type_0_item_data in _scopes_type_0:
                    scopes_type_0_item = NouvelleCleBodyScopesType0Item(
                        scopes_type_0_item_data
                    )

                    scopes_type_0.append(scopes_type_0_item)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NouvelleCleBodyScopesType0Item] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))

        nouvelle_cle_body = cls(
            name=name,
            daily_limit=daily_limit,
            expires_in=expires_in,
            mode=mode,
            scopes=scopes,
        )

        return nouvelle_cle_body
