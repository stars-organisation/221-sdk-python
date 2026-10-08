from enum import StrEnum


class PaymentRequestMethod(StrEnum):
    ORANGE = "orange"
    WAVE = "wave"

    def __str__(self) -> str:
        return str(self.value)
