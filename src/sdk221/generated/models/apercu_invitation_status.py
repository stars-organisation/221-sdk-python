from enum import StrEnum


class ApercuInvitationStatus(StrEnum):
    EXPIRED = "expired"
    PENDING = "pending"
    USED = "used"

    def __str__(self) -> str:
        return str(self.value)
