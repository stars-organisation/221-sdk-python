from enum import StrEnum


class CountTelechargementType(StrEnum):
    OUVERTURE = "ouverture"
    TELECHARGEMENT = "telechargement"

    def __str__(self) -> str:
        return str(self.value)
