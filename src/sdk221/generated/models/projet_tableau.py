from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abonnement import Abonnement
    from ..models.appel_journal import AppelJournal
    from ..models.cle_api import CleApi
    from ..models.consommation import Consommation
    from ..models.payments_calls import PaymentsCalls
    from ..models.quota import Quota


T = TypeVar("T", bound="ProjetTableau")


@_attrs_define
class ProjetTableau:
    """
    Attributes:
        calls (list[AppelJournal] | None):
        created_at (datetime.datetime):
        id (str):
        keys (list[CleApi] | None):
        live_enabled (bool): Mode live activé : les clés live peuvent être créées.
        name (str):
        quota (Quota):
        slug (str):
        usage (list[Consommation] | None):
        webhook_secret (str):
        webhooks (list[Abonnement] | None):
        payments_calls (PaymentsCalls | Unset):
    """

    calls: list[AppelJournal] | None
    created_at: datetime.datetime
    id: str
    keys: list[CleApi] | None
    live_enabled: bool
    name: str
    quota: Quota
    slug: str
    usage: list[Consommation] | None
    webhook_secret: str
    webhooks: list[Abonnement] | None
    payments_calls: PaymentsCalls | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        calls: list[dict[str, Any]] | None
        if isinstance(self.calls, list):
            calls = []
            for calls_type_0_item_data in self.calls:
                calls_type_0_item = calls_type_0_item_data.to_dict()
                calls.append(calls_type_0_item)

        else:
            calls = self.calls

        created_at = self.created_at.isoformat()

        id = self.id

        keys: list[dict[str, Any]] | None
        if isinstance(self.keys, list):
            keys = []
            for keys_type_0_item_data in self.keys:
                keys_type_0_item = keys_type_0_item_data.to_dict()
                keys.append(keys_type_0_item)

        else:
            keys = self.keys

        live_enabled = self.live_enabled

        name = self.name

        quota = self.quota.to_dict()

        slug = self.slug

        usage: list[dict[str, Any]] | None
        if isinstance(self.usage, list):
            usage = []
            for usage_type_0_item_data in self.usage:
                usage_type_0_item = usage_type_0_item_data.to_dict()
                usage.append(usage_type_0_item)

        else:
            usage = self.usage

        webhook_secret = self.webhook_secret

        webhooks: list[dict[str, Any]] | None
        if isinstance(self.webhooks, list):
            webhooks = []
            for webhooks_type_0_item_data in self.webhooks:
                webhooks_type_0_item = webhooks_type_0_item_data.to_dict()
                webhooks.append(webhooks_type_0_item)

        else:
            webhooks = self.webhooks

        payments_calls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payments_calls, Unset):
            payments_calls = self.payments_calls.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "calls": calls,
                "created_at": created_at,
                "id": id,
                "keys": keys,
                "live_enabled": live_enabled,
                "name": name,
                "quota": quota,
                "slug": slug,
                "usage": usage,
                "webhook_secret": webhook_secret,
                "webhooks": webhooks,
            }
        )
        if payments_calls is not UNSET:
            field_dict["payments_calls"] = payments_calls

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.abonnement import Abonnement
        from ..models.appel_journal import AppelJournal
        from ..models.cle_api import CleApi
        from ..models.consommation import Consommation
        from ..models.payments_calls import PaymentsCalls
        from ..models.quota import Quota

        d = dict(src_dict)

        def _parse_calls(data: object) -> list[AppelJournal] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                calls_type_0 = []
                _calls_type_0 = data
                for calls_type_0_item_data in _calls_type_0:
                    calls_type_0_item = AppelJournal.from_dict(calls_type_0_item_data)

                    calls_type_0.append(calls_type_0_item)

                return calls_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AppelJournal] | None, data)

        calls = _parse_calls(d.pop("calls"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = d.pop("id")

        def _parse_keys(data: object) -> list[CleApi] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keys_type_0 = []
                _keys_type_0 = data
                for keys_type_0_item_data in _keys_type_0:
                    keys_type_0_item = CleApi.from_dict(keys_type_0_item_data)

                    keys_type_0.append(keys_type_0_item)

                return keys_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CleApi] | None, data)

        keys = _parse_keys(d.pop("keys"))

        live_enabled = d.pop("live_enabled")

        name = d.pop("name")

        quota = Quota.from_dict(d.pop("quota"))

        slug = d.pop("slug")

        def _parse_usage(data: object) -> list[Consommation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                usage_type_0 = []
                _usage_type_0 = data
                for usage_type_0_item_data in _usage_type_0:
                    usage_type_0_item = Consommation.from_dict(usage_type_0_item_data)

                    usage_type_0.append(usage_type_0_item)

                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Consommation] | None, data)

        usage = _parse_usage(d.pop("usage"))

        webhook_secret = d.pop("webhook_secret")

        def _parse_webhooks(data: object) -> list[Abonnement] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                webhooks_type_0 = []
                _webhooks_type_0 = data
                for webhooks_type_0_item_data in _webhooks_type_0:
                    webhooks_type_0_item = Abonnement.from_dict(
                        webhooks_type_0_item_data
                    )

                    webhooks_type_0.append(webhooks_type_0_item)

                return webhooks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Abonnement] | None, data)

        webhooks = _parse_webhooks(d.pop("webhooks"))

        _payments_calls = d.pop("payments_calls", UNSET)
        payments_calls: PaymentsCalls | Unset
        if isinstance(_payments_calls, Unset):
            payments_calls = UNSET
        else:
            payments_calls = PaymentsCalls.from_dict(_payments_calls)

        projet_tableau = cls(
            calls=calls,
            created_at=created_at,
            id=id,
            keys=keys,
            live_enabled=live_enabled,
            name=name,
            quota=quota,
            slug=slug,
            usage=usage,
            webhook_secret=webhook_secret,
            webhooks=webhooks,
            payments_calls=payments_calls,
        )

        return projet_tableau
