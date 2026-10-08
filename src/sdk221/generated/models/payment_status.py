from enum import StrEnum


class PaymentStatus(StrEnum):
    CONFIRMED = "confirmed"
    CREATED = "created"
    EXPIRED = "expired"
    FAILED = "failed"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
