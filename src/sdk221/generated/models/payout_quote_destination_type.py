from enum import StrEnum


class PayoutQuoteDestinationType(StrEnum):
    BANK = "bank"

    def __str__(self) -> str:
        return str(self.value)
