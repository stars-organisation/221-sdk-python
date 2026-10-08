from enum import StrEnum


class DisputeDisputeStage(StrEnum):
    DISPUTE = "dispute"
    PRE_DISPUTE = "pre_dispute"

    def __str__(self) -> str:
        return str(self.value)
