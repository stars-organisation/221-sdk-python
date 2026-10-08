from enum import StrEnum


class AnswerOnboardingQuestion(StrEnum):
    CONNU = "connu"
    FIN = "fin"
    PROFIL = "profil"
    SPECIALITE = "specialite"

    def __str__(self) -> str:
        return str(self.value)
