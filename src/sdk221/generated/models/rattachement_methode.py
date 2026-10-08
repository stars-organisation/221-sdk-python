from enum import StrEnum


class RattachementMethode(StrEnum):
    CENTROIDE_LE_PLUS_PROCHE = "centroide_le_plus_proche"
    CONTOUR = "contour"

    def __str__(self) -> str:
        return str(self.value)
