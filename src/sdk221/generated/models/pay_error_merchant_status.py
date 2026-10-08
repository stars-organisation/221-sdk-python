from enum import StrEnum


class PayErrorMerchantStatus(StrEnum):
    CLOSED = "closed"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
