from enum import StrEnum


class TypeEvenementProduct(StrEnum):
    DATA = "data"
    PAYMENTS = "payments"

    def __str__(self) -> str:
        return str(self.value)
