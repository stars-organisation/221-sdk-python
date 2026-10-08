from enum import StrEnum


class QuotaTier(StrEnum):
    STANDARD = "standard"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
