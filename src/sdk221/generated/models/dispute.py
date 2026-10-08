from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.dispute_currency import DisputeCurrency
from ..models.dispute_dispute_stage import DisputeDisputeStage
from ..models.dispute_dispute_status import DisputeDisputeStatus
from ..models.dispute_reason import DisputeReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dispute_evidence import DisputeEvidence


T = TypeVar("T", bound="Dispute")


@_attrs_define
class Dispute:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        challenge_required_by (datetime.datetime): Date limite pour contester.
        created_at (datetime.datetime):
        currency (DisputeCurrency):
        dispute_id (UUID):
        dispute_stage (DisputeDisputeStage):
        dispute_status (DisputeDisputeStatus):
        is_already_refunded (bool):
        livemode (bool): true : objet du mode live ; false : mode test.
        payment_id (UUID):
        project_id (UUID):
        reason (DisputeReason):
        updated_at (datetime.datetime):
        evidence (list[DisputeEvidence] | Unset): Pièces jointes ; absent des listes.
    """

    amount: str
    challenge_required_by: datetime.datetime
    created_at: datetime.datetime
    currency: DisputeCurrency
    dispute_id: UUID
    dispute_stage: DisputeDisputeStage
    dispute_status: DisputeDisputeStatus
    is_already_refunded: bool
    livemode: bool
    payment_id: UUID
    project_id: UUID
    reason: DisputeReason
    updated_at: datetime.datetime
    evidence: list[DisputeEvidence] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        challenge_required_by = self.challenge_required_by.isoformat()

        created_at = self.created_at.isoformat()

        currency = self.currency.value

        dispute_id = str(self.dispute_id)

        dispute_stage = self.dispute_stage.value

        dispute_status = self.dispute_status.value

        is_already_refunded = self.is_already_refunded

        livemode = self.livemode

        payment_id = str(self.payment_id)

        project_id = str(self.project_id)

        reason = self.reason.value

        updated_at = self.updated_at.isoformat()

        evidence: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.evidence, Unset):
            evidence = []
            for evidence_item_data in self.evidence:
                evidence_item = evidence_item_data.to_dict()
                evidence.append(evidence_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "challenge_required_by": challenge_required_by,
                "created_at": created_at,
                "currency": currency,
                "dispute_id": dispute_id,
                "dispute_stage": dispute_stage,
                "dispute_status": dispute_status,
                "is_already_refunded": is_already_refunded,
                "livemode": livemode,
                "payment_id": payment_id,
                "project_id": project_id,
                "reason": reason,
                "updated_at": updated_at,
            }
        )
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dispute_evidence import DisputeEvidence

        d = dict(src_dict)
        amount = d.pop("amount")

        challenge_required_by = datetime.datetime.fromisoformat(
            d.pop("challenge_required_by")
        )

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        currency = DisputeCurrency(d.pop("currency"))

        dispute_id = UUID(d.pop("dispute_id"))

        dispute_stage = DisputeDisputeStage(d.pop("dispute_stage"))

        dispute_status = DisputeDisputeStatus(d.pop("dispute_status"))

        is_already_refunded = d.pop("is_already_refunded")

        livemode = d.pop("livemode")

        payment_id = UUID(d.pop("payment_id"))

        project_id = UUID(d.pop("project_id"))

        reason = DisputeReason(d.pop("reason"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _evidence = d.pop("evidence", UNSET)
        evidence: list[DisputeEvidence] | Unset = UNSET
        if _evidence is not UNSET:
            evidence = []
            for evidence_item_data in _evidence:
                evidence_item = DisputeEvidence.from_dict(evidence_item_data)

                evidence.append(evidence_item)

        dispute = cls(
            amount=amount,
            challenge_required_by=challenge_required_by,
            created_at=created_at,
            currency=currency,
            dispute_id=dispute_id,
            dispute_stage=dispute_stage,
            dispute_status=dispute_status,
            is_already_refunded=is_already_refunded,
            livemode=livemode,
            payment_id=payment_id,
            project_id=project_id,
            reason=reason,
            updated_at=updated_at,
            evidence=evidence,
        )

        return dispute
