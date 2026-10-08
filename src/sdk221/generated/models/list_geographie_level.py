from enum import StrEnum


class ListGeographieLevel(StrEnum):
    ARRONDISSEMENT = "arrondissement"
    COMMUNE = "commune"
    DEPARTEMENT = "departement"
    REGION = "region"
    VILLE = "ville"

    def __str__(self) -> str:
        return str(self.value)
