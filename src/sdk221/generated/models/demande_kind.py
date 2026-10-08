from enum import StrEnum


class DemandeKind(StrEnum):
    API = "api"
    DONNEES = "donnees"

    def __str__(self) -> str:
        return str(self.value)
