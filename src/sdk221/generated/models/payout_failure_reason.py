from enum import StrEnum


class PayoutFailureReason(StrEnum):
    DESTINATION_INVALID = "destination_invalid"
    DESTINATION_LIMIT = "destination_limit"
    PROVIDER_UNAVAILABLE = "provider_unavailable"

    def __str__(self) -> str:
        return str(self.value)
