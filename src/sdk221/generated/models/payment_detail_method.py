from enum import StrEnum


class PaymentDetailMethod(StrEnum):
    ORANGE = "orange"
    WAVE = "wave"

    def __str__(self) -> str:
        return str(self.value)
