from enum import StrEnum


class NouvelleInvitationBodyRole(StrEnum):
    ADMIN = "admin"
    READ_ONLY = "read_only"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
