from enum import StrEnum


class NouvelleCleBodyExpiresIn(StrEnum):
    NEVER = "never"
    VALUE_1 = "30d"
    VALUE_2 = "90d"
    VALUE_3 = "1y"

    def __str__(self) -> str:
        return str(self.value)
