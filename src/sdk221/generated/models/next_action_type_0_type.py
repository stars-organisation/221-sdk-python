from enum import StrEnum


class NextActionType0Type(StrEnum):
    INSTRUCTION = "instruction"
    QR = "qr"
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)
