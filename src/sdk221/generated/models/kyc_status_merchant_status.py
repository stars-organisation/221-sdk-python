from enum import StrEnum


class KycStatusMerchantStatus(StrEnum):
    ACTIVE = "active"
    CLOSED = "closed"
    PENDING = "pending"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
