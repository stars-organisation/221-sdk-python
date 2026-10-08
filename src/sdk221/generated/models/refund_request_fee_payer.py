from enum import StrEnum


class RefundRequestFeePayer(StrEnum):
    CUSTOMER = "customer"
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
