from enum import StrEnum


class RotationCleBodyGrace(StrEnum):
    NOW = "now"
    VALUE_1 = "1h"
    VALUE_2 = "24h"
    VALUE_3 = "7d"

    def __str__(self) -> str:
        return str(self.value)
