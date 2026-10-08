from enum import StrEnum


class DemandeStatus(StrEnum):
    EN_COURS = "en_cours"
    IMPOSSIBLE = "impossible"
    OUVERTE = "ouverte"
    PUBLIEE = "publiee"

    def __str__(self) -> str:
        return str(self.value)
