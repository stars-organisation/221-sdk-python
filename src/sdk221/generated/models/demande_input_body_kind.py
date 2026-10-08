from enum import StrEnum


class DemandeInputBodyKind(StrEnum):
    API = "api"
    DONNEES = "donnees"

    def __str__(self) -> str:
        return str(self.value)
