from enum import StrEnum


class NouvelleCleBodyScopesType0Item(StrEnum):
    DATA = "data"
    PAYMENTS = "payments"

    def __str__(self) -> str:
        return str(self.value)
