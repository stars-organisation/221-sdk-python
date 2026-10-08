from enum import StrEnum


class PaymentDetailErrorCode(StrEnum):
    EXPIRED = "expired"
    PROVIDER_FAILED = "provider_failed"

    def __str__(self) -> str:
        return str(self.value)
