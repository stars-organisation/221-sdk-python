from enum import StrEnum


class PaymentLinkStatus(StrEnum):
    ACTIVE = "active"
    EXPIRED = "expired"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
