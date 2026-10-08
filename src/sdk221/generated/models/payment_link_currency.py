from enum import StrEnum


class PaymentLinkCurrency(StrEnum):
    XOF = "XOF"

    def __str__(self) -> str:
        return str(self.value)
