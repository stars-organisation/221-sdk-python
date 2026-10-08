from enum import StrEnum


class MontantCurrency(StrEnum):
    XOF = "XOF"

    def __str__(self) -> str:
        return str(self.value)
