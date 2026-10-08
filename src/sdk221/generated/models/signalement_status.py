from enum import StrEnum


class SignalementStatus(StrEnum):
    ACCEPTE = "accepte"
    RECU = "recu"
    REFUSE = "refuse"

    def __str__(self) -> str:
        return str(self.value)
