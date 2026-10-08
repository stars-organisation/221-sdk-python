from enum import StrEnum


class RefundCoreStatus(StrEnum):
    FAILED = "failed"
    PROCESSING = "processing"
    REQUESTED = "requested"
    SUCCEEDED = "succeeded"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
