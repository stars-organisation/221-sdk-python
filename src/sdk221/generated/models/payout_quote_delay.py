from enum import StrEnum


class PayoutQuoteDelay(StrEnum):
    VALUE_0 = "3-5 business days"

    def __str__(self) -> str:
        return str(self.value)
