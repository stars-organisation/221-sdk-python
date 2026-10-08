from enum import StrEnum


class AnswerOnboardingQuestion(StrEnum):
    CONNU = "connu"
    FIN = "fin"
    FLOW_ACCOUNT = "flow_account"
    FLOW_FIRST_REQUEST = "flow_first_request"
    FLOW_KEY = "flow_key"
    FLOW_PROJECT = "flow_project"
    PROFIL = "profil"
    SPECIALITE = "specialite"

    def __str__(self) -> str:
        return str(self.value)
