from enum import StrEnum


class DisputeDisputeStatus(StrEnum):
    ACCEPTED = "accepted"
    CHALLENGED = "challenged"
    LOST = "lost"
    OPENED = "opened"
    UNDER_REVIEW = "under_review"
    WON = "won"

    def __str__(self) -> str:
        return str(self.value)
