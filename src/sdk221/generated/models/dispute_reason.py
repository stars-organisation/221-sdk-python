from enum import StrEnum


class DisputeReason(StrEnum):
    DUPLICATE = "duplicate"
    NOT_AS_DESCRIBED = "not_as_described"
    NOT_RECEIVED = "not_received"
    OTHER_DOCUMENTED = "other_documented"
    UNAUTHORIZED = "unauthorized"

    def __str__(self) -> str:
        return str(self.value)
