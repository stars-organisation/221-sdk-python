from enum import StrEnum


class OfferStatus(StrEnum):
    ACTIVE = "active"
    DELETED = "deleted"
    INACTIVE = "inactive"

    def __str__(self) -> str:
        return str(self.value)
