from enum import StrEnum


class KycStatusStatus(StrEnum):
    NOT_STARTED = "not_started"
    PENDING = "pending"
    REJECTED = "rejected"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
