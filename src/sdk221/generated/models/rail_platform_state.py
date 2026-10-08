from enum import StrEnum


class RailPlatformState(StrEnum):
    INCIDENT = "incident"
    NOT_OPEN = "not_open"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
