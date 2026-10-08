from enum import StrEnum


class ReportInputBodyLang(StrEnum):
    EN = "en"
    FR = "fr"

    def __str__(self) -> str:
        return str(self.value)
