from enum import StrEnum


class SettingsRefundFeePayerDefault(StrEnum):
    CUSTOMER = "customer"
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
