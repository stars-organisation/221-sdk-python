from enum import StrEnum


class RefundCurrency(StrEnum):
    XOF = "XOF"

    def __str__(self) -> str:
        return str(self.value)
