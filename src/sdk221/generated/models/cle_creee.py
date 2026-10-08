from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.cle_creee_mode import CleCreeeMode

T = TypeVar("T", bound="CleCreee")


@_attrs_define
class CleCreee:
    """
    Attributes:
        created_at (datetime.datetime):
        daily_limit (int):
        disabled_at (datetime.datetime): Désactivation par un administrateur (usage abusif).
        disabled_reason (None | str):
        expires_at (datetime.datetime): Fin de validité ; null : sans expiration.
        id (str):
        last_used_at (datetime.datetime):
        mode (CleCreeeMode): test : aucun argent réel ; live : argent réel.
        name (str):
        prefix (str):
        revoked_at (datetime.datetime):
        rotated_from (None | str): Clé remplacée par celle-ci lors d'une rotation ; null sinon.
        scopes (list[str] | None): Produits que la clé peut appeler : payments, data.
        secret (str): À conserver : il ne sera plus jamais affiché.
    """

    created_at: datetime.datetime
    daily_limit: int
    disabled_at: datetime.datetime
    disabled_reason: None | str
    expires_at: datetime.datetime
    id: str
    last_used_at: datetime.datetime
    mode: CleCreeeMode
    name: str
    prefix: str
    revoked_at: datetime.datetime
    rotated_from: None | str
    scopes: list[str] | None
    secret: str

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        daily_limit = self.daily_limit

        disabled_at = self.disabled_at.isoformat()

        disabled_reason: None | str
        disabled_reason = self.disabled_reason

        expires_at = self.expires_at.isoformat()

        id = self.id

        last_used_at = self.last_used_at.isoformat()

        mode = self.mode.value

        name = self.name

        prefix = self.prefix

        revoked_at = self.revoked_at.isoformat()

        rotated_from: None | str
        rotated_from = self.rotated_from

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        secret = self.secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "daily_limit": daily_limit,
                "disabled_at": disabled_at,
                "disabled_reason": disabled_reason,
                "expires_at": expires_at,
                "id": id,
                "last_used_at": last_used_at,
                "mode": mode,
                "name": name,
                "prefix": prefix,
                "revoked_at": revoked_at,
                "rotated_from": rotated_from,
                "scopes": scopes,
                "secret": secret,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        daily_limit = d.pop("daily_limit")

        disabled_at = datetime.datetime.fromisoformat(d.pop("disabled_at"))

        def _parse_disabled_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabled_reason"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        id = d.pop("id")

        last_used_at = datetime.datetime.fromisoformat(d.pop("last_used_at"))

        mode = CleCreeeMode(d.pop("mode"))

        name = d.pop("name")

        prefix = d.pop("prefix")

        revoked_at = datetime.datetime.fromisoformat(d.pop("revoked_at"))

        def _parse_rotated_from(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rotated_from = _parse_rotated_from(d.pop("rotated_from"))

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

        secret = d.pop("secret")

        cle_creee = cls(
            created_at=created_at,
            daily_limit=daily_limit,
            disabled_at=disabled_at,
            disabled_reason=disabled_reason,
            expires_at=expires_at,
            id=id,
            last_used_at=last_used_at,
            mode=mode,
            name=name,
            prefix=prefix,
            revoked_at=revoked_at,
            rotated_from=rotated_from,
            scopes=scopes,
            secret=secret,
        )

        return cle_creee
