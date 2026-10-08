from enum import StrEnum


class BalancesGatewayMode(StrEnum):
    NOT_WIRED = "not_wired"
    REAL = "real"
    SIMULATED = "simulated"

    def __str__(self) -> str:
        return str(self.value)
