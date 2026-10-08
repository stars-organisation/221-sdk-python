from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.kyc_status_merchant_status import KycStatusMerchantStatus
from ..models.kyc_status_status import KycStatusStatus
from ..models.kyc_status_withdrawals_blocked_reason import (
    KycStatusWithdrawalsBlockedReason,
)

T = TypeVar("T", bound="KycStatus")


@_attrs_define
class KycStatus:
    """
    Attributes:
        country (None | str):
        document_type (None | str):
        livemode (bool): true : objet du mode live ; false : mode test.
        merchant_status (KycStatusMerchantStatus):
        reason_code (None | str): Motif du refus, quand status vaut rejected.
        review_eta (datetime.datetime | None): Fin prévue de l'examen, cinq jours ouvrés après l'envoi.
        status (KycStatusStatus):
        submitted (bool): true : envoyée à l'examen.
        uploaded (list[str]): Photos déjà reçues.
        verification_id (None | str): Renseigné quand la vérification est pending.
        withdrawals_blocked (bool):
        withdrawals_blocked_reason (KycStatusWithdrawalsBlockedReason):
    """

    country: None | str
    document_type: None | str
    livemode: bool
    merchant_status: KycStatusMerchantStatus
    reason_code: None | str
    review_eta: datetime.datetime | None
    status: KycStatusStatus
    submitted: bool
    uploaded: list[str]
    verification_id: None | str
    withdrawals_blocked: bool
    withdrawals_blocked_reason: KycStatusWithdrawalsBlockedReason

    def to_dict(self) -> dict[str, Any]:
        country: None | str
        country = self.country

        document_type: None | str
        document_type = self.document_type

        livemode = self.livemode

        merchant_status = self.merchant_status.value

        reason_code: None | str
        reason_code = self.reason_code

        review_eta: None | str
        if isinstance(self.review_eta, datetime.datetime):
            review_eta = self.review_eta.isoformat()
        else:
            review_eta = self.review_eta

        status = self.status.value

        submitted = self.submitted

        uploaded = self.uploaded

        verification_id: None | str
        verification_id = self.verification_id

        withdrawals_blocked = self.withdrawals_blocked

        withdrawals_blocked_reason = self.withdrawals_blocked_reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "document_type": document_type,
                "livemode": livemode,
                "merchant_status": merchant_status,
                "reason_code": reason_code,
                "review_eta": review_eta,
                "status": status,
                "submitted": submitted,
                "uploaded": uploaded,
                "verification_id": verification_id,
                "withdrawals_blocked": withdrawals_blocked,
                "withdrawals_blocked_reason": withdrawals_blocked_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_document_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        document_type = _parse_document_type(d.pop("document_type"))

        livemode = d.pop("livemode")

        merchant_status = KycStatusMerchantStatus(d.pop("merchant_status"))

        def _parse_reason_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason_code = _parse_reason_code(d.pop("reason_code"))

        def _parse_review_eta(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                review_eta_type_0 = datetime.datetime.fromisoformat(data)

                return review_eta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        review_eta = _parse_review_eta(d.pop("review_eta"))

        status = KycStatusStatus(d.pop("status"))

        submitted = d.pop("submitted")

        uploaded = cast(list[str], d.pop("uploaded"))

        def _parse_verification_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        verification_id = _parse_verification_id(d.pop("verification_id"))

        withdrawals_blocked = d.pop("withdrawals_blocked")

        withdrawals_blocked_reason = KycStatusWithdrawalsBlockedReason(
            d.pop("withdrawals_blocked_reason")
        )

        kyc_status = cls(
            country=country,
            document_type=document_type,
            livemode=livemode,
            merchant_status=merchant_status,
            reason_code=reason_code,
            review_eta=review_eta,
            status=status,
            submitted=submitted,
            uploaded=uploaded,
            verification_id=verification_id,
            withdrawals_blocked=withdrawals_blocked,
            withdrawals_blocked_reason=withdrawals_blocked_reason,
        )

        return kyc_status
