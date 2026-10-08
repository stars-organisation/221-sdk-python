from enum import StrEnum


class PayoutReceiptDestinationType(StrEnum):
    BANK = "bank"
    MOBILE = "mobile"

    def __str__(self) -> str:
        return str(self.value)
