from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.kyc_session_status import KycSessionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kyc_capture import KycCapture


T = TypeVar("T", bound="KycSession")


@_attrs_define
class KycSession:
    """
    Attributes:
        livemode (bool): true : objet du mode live ; false : mode test.
        status (KycSessionStatus):
        captures (list[KycCapture] | Unset): Photos à envoyer.
        expires_at (datetime.datetime | Unset):
        handoff_url (str | Unset): Lien à ouvrir sur un téléphone pour prendre les photos.
        submitted (bool | Unset):
        uploaded (list[str] | Unset):
        verification_id (str | Unset):
    """

    livemode: bool
    status: KycSessionStatus
    captures: list[KycCapture] | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    handoff_url: str | Unset = UNSET
    submitted: bool | Unset = UNSET
    uploaded: list[str] | Unset = UNSET
    verification_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        livemode = self.livemode

        status = self.status.value

        captures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.captures, Unset):
            captures = []
            for captures_item_data in self.captures:
                captures_item = captures_item_data.to_dict()
                captures.append(captures_item)

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        handoff_url = self.handoff_url

        submitted = self.submitted

        uploaded: list[str] | Unset = UNSET
        if not isinstance(self.uploaded, Unset):
            uploaded = self.uploaded

        verification_id = self.verification_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "livemode": livemode,
                "status": status,
            }
        )
        if captures is not UNSET:
            field_dict["captures"] = captures
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if handoff_url is not UNSET:
            field_dict["handoff_url"] = handoff_url
        if submitted is not UNSET:
            field_dict["submitted"] = submitted
        if uploaded is not UNSET:
            field_dict["uploaded"] = uploaded
        if verification_id is not UNSET:
            field_dict["verification_id"] = verification_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.kyc_capture import KycCapture

        d = dict(src_dict)
        livemode = d.pop("livemode")

        status = KycSessionStatus(d.pop("status"))

        _captures = d.pop("captures", UNSET)
        captures: list[KycCapture] | Unset = UNSET
        if _captures is not UNSET:
            captures = []
            for captures_item_data in _captures:
                captures_item = KycCapture.from_dict(captures_item_data)

                captures.append(captures_item)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        handoff_url = d.pop("handoff_url", UNSET)

        submitted = d.pop("submitted", UNSET)

        uploaded = cast(list[str], d.pop("uploaded", UNSET))

        verification_id = d.pop("verification_id", UNSET)

        kyc_session = cls(
            livemode=livemode,
            status=status,
            captures=captures,
            expires_at=expires_at,
            handoff_url=handoff_url,
            submitted=submitted,
            uploaded=uploaded,
            verification_id=verification_id,
        )

        return kyc_session
