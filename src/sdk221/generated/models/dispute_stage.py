from enum import StrEnum


class DisputeStage(StrEnum):
    DISPUTE = "dispute"
    PRE_DISPUTE = "pre_dispute"

    def __str__(self) -> str:
        return str(self.value)
