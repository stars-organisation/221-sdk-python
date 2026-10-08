from enum import StrEnum


class KycCaptureName(StrEnum):
    BACK = "back"
    FRONT = "front"
    SELFIE = "selfie"

    def __str__(self) -> str:
        return str(self.value)
