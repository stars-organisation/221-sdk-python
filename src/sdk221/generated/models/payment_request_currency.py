from enum import StrEnum


class PaymentRequestCurrency(StrEnum):
    XOF = "XOF"

    def __str__(self) -> str:
        return str(self.value)
