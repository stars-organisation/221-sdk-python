from enum import StrEnum


class PrefixeOperateurType(StrEnum):
    FIXE = "fixe"
    MOBILE = "mobile"

    def __str__(self) -> str:
        return str(self.value)
