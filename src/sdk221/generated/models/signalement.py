from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.signalement_status import SignalementStatus

T = TypeVar("T", bound="Signalement")


@_attrs_define
class Signalement:
    """
    Attributes:
        created_at (datetime.datetime):
        dataset (str):
        decided_at (datetime.datetime):
        issue_url (None | str): Issue GitHub publique ; null tant qu’elle n’a pas pu être créée.
        numero (str): Numéro de suivi.
        status (SignalementStatus): recu, puis accepte ou refuse.
    """

    created_at: datetime.datetime
    dataset: str
    decided_at: datetime.datetime
    issue_url: None | str
    numero: str
    status: SignalementStatus

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset = self.dataset

        decided_at = self.decided_at.isoformat()

        issue_url: None | str
        issue_url = self.issue_url

        numero = self.numero

        status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "dataset": dataset,
                "decided_at": decided_at,
                "issue_url": issue_url,
                "numero": numero,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        dataset = d.pop("dataset")

        decided_at = datetime.datetime.fromisoformat(d.pop("decided_at"))

        def _parse_issue_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        issue_url = _parse_issue_url(d.pop("issue_url"))

        numero = d.pop("numero")

        status = SignalementStatus(d.pop("status"))

        signalement = cls(
            created_at=created_at,
            dataset=dataset,
            decided_at=decided_at,
            issue_url=issue_url,
            numero=numero,
            status=status,
        )

        return signalement
