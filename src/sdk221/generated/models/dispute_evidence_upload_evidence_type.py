from enum import StrEnum


class DisputeEvidenceUploadEvidenceType(StrEnum):
    CUSTOMER_COMMUNICATION = "customer_communication"
    DELIVERY_PROOF = "delivery_proof"
    OTHER = "other"
    RECEIPT = "receipt"

    def __str__(self) -> str:
        return str(self.value)
