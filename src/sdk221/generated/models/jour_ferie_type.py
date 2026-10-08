from enum import StrEnum


class JourFerieType(StrEnum):
    CIVILE = "civile"
    RELIGIEUSE = "religieuse"

    def __str__(self) -> str:
        return str(self.value)
