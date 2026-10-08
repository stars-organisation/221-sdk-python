from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.demande_kind import DemandeKind
from ..models.demande_status import DemandeStatus

T = TypeVar("T", bound="Demande")


@_attrs_define
class Demande:
    """
    Attributes:
        created_at (datetime.datetime):
        details (None | str):
        id (str):
        kind (DemandeKind):
        note (None | str): Explication de l’équipe 221, surtout pour « impossible ».
        status (DemandeStatus):
        title (str):
        voted (bool): Vrai si l’utilisateur connecté a voté.
        votes (int):
    """

    created_at: datetime.datetime
    details: None | str
    id: str
    kind: DemandeKind
    note: None | str
    status: DemandeStatus
    title: str
    voted: bool
    votes: int

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        details: None | str
        details = self.details

        id = self.id

        kind = self.kind.value

        note: None | str
        note = self.note

        status = self.status.value

        title = self.title

        voted = self.voted

        votes = self.votes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "details": details,
                "id": id,
                "kind": kind,
                "note": note,
                "status": status,
                "title": title,
                "voted": voted,
                "votes": votes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_details(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        details = _parse_details(d.pop("details"))

        id = d.pop("id")

        kind = DemandeKind(d.pop("kind"))

        def _parse_note(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note = _parse_note(d.pop("note"))

        status = DemandeStatus(d.pop("status"))

        title = d.pop("title")

        voted = d.pop("voted")

        votes = d.pop("votes")

        demande = cls(
            created_at=created_at,
            details=details,
            id=id,
            kind=kind,
            note=note,
            status=status,
            title=title,
            voted=voted,
            votes=votes,
        )

        return demande
