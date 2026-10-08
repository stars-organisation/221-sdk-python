from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="PayoutPending")


@_attrs_define
class PayoutPending:
    """
    Attributes:
        id (UUID):
        livemode (bool): true : objet du mode live ; false : mode test.
        status (str):
    """

    id: UUID
    livemode: bool
    status: str

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        livemode = self.livemode

        status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "livemode": livemode,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        livemode = d.pop("livemode")

        status = d.pop("status")

        payout_pending = cls(
            id=id,
            livemode=livemode,
            status=status,
        )

        return payout_pending
