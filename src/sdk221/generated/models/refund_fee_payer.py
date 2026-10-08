from enum import StrEnum


class RefundFeePayer(StrEnum):
    CUSTOMER = "customer"
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
