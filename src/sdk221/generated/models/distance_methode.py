from enum import StrEnum


class DistanceMethode(StrEnum):
    VOL_OISEAU = "vol_oiseau"

    def __str__(self) -> str:
        return str(self.value)
