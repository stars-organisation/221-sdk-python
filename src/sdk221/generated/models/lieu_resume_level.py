from enum import StrEnum


class LieuResumeLevel(StrEnum):
    ARRONDISSEMENT = "arrondissement"
    COMMUNE = "commune"
    DEPARTEMENT = "departement"
    LOCALITE = "localite"
    REGION = "region"
    VILLE = "ville"

    def __str__(self) -> str:
        return str(self.value)
