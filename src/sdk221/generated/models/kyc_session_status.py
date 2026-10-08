from enum import StrEnum


class KycSessionStatus(StrEnum):
    PENDING = "pending"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
