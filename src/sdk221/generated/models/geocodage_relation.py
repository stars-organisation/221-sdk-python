from enum import StrEnum


class GeocodageRelation(StrEnum):
    A_COTE_DE = "a_cote_de"
    DERRIERE = "derriere"
    EN_FACE_DE = "en_face_de"
    PRES_DE = "pres_de"

    def __str__(self) -> str:
        return str(self.value)
