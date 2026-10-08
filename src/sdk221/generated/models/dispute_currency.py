from enum import StrEnum


class DisputeCurrency(StrEnum):
    XOF = "XOF"

    def __str__(self) -> str:
        return str(self.value)
