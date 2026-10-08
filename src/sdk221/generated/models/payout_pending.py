from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayoutPending")


@_attrs_define
class PayoutPending:
    """
    Attributes:
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        status (str):
        release_at (datetime.datetime | Unset): Retrait en file : le numéro vient d'être vérifié, l'envoi part à partir
            de cette date.
    """

    id: UUID
    livemode: bool
    status: str
    release_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        livemode = self.livemode

        status = self.status

        release_at: str | Unset = UNSET
        if not isinstance(self.release_at, Unset):
            release_at = self.release_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "livemode": livemode,
                "status": status,
            }
        )
        if release_at is not UNSET:
            field_dict["release_at"] = release_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        status = d.pop("status")

        _release_at = d.pop("release_at", UNSET)
        release_at: datetime.datetime | Unset
        if isinstance(_release_at, Unset):
            release_at = UNSET
        else:
            release_at = datetime.datetime.fromisoformat(_release_at)

        payout_pending = cls(
            id=id,
            livemode=livemode,
            status=status,
            release_at=release_at,
        )

        return payout_pending
