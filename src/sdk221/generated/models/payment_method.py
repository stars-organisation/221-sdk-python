from enum import StrEnum


class PaymentMethod(StrEnum):
    ORANGE = "orange"
    WAVE = "wave"

    def __str__(self) -> str:
        return str(self.value)
