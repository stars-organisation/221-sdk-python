from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.quota_tier import QuotaTier

T = TypeVar("T", bound="Quota")


@_attrs_define
class Quota:
    """
    Attributes:
        account_daily_limit (int):
        account_used (int):
        anonymous_daily_limit (int):
        key_daily_limit (int):
        key_limit (int):
        rate_limit_per_minute (int): Limite anti-abus des routes 221 Pay, par projet et par minute.
        reset (str):
        tier (QuotaTier): verified : identité vérifiée sur au moins un projet du compte.
        verified_account_daily_limit (int): Limite journalière d'un compte vérifié (palier verified).
    """

    account_daily_limit: int
    account_used: int
    anonymous_daily_limit: int
    key_daily_limit: int
    key_limit: int
    rate_limit_per_minute: int
    reset: str
    tier: QuotaTier
    verified_account_daily_limit: int

    def to_dict(self) -> dict[str, Any]:
        account_daily_limit = self.account_daily_limit

        account_used = self.account_used

        anonymous_daily_limit = self.anonymous_daily_limit

        key_daily_limit = self.key_daily_limit

        key_limit = self.key_limit

        rate_limit_per_minute = self.rate_limit_per_minute

        reset = self.reset

        tier = self.tier.value

        verified_account_daily_limit = self.verified_account_daily_limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_daily_limit": account_daily_limit,
                "account_used": account_used,
                "anonymous_daily_limit": anonymous_daily_limit,
                "key_daily_limit": key_daily_limit,
                "key_limit": key_limit,
                "rate_limit_per_minute": rate_limit_per_minute,
                "reset": reset,
                "tier": tier,
                "verified_account_daily_limit": verified_account_daily_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        account_daily_limit = d.pop("account_daily_limit")

        account_used = d.pop("account_used")

        anonymous_daily_limit = d.pop("anonymous_daily_limit")

        key_daily_limit = d.pop("key_daily_limit")

        key_limit = d.pop("key_limit")

        rate_limit_per_minute = d.pop("rate_limit_per_minute")

        reset = d.pop("reset")

        tier = QuotaTier(d.pop("tier"))

        verified_account_daily_limit = d.pop("verified_account_daily_limit")

        quota = cls(
            account_daily_limit=account_daily_limit,
            account_used=account_used,
            anonymous_daily_limit=anonymous_daily_limit,
            key_daily_limit=key_daily_limit,
            key_limit=key_limit,
            rate_limit_per_minute=rate_limit_per_minute,
            reset=reset,
            tier=tier,
            verified_account_daily_limit=verified_account_daily_limit,
        )

        return quota
