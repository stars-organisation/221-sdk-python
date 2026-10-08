from enum import StrEnum


class PayErrorKycStatus(StrEnum):
    NOT_STARTED = "not_started"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
