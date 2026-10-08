from enum import StrEnum


class JourFerieDateStatus(StrEnum):
    CONFIRMEE = "confirmee"
    PREVISIONNELLE = "previsionnelle"

    def __str__(self) -> str:
        return str(self.value)
