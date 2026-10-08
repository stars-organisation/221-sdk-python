from enum import StrEnum


class RefundQuoteRequestFeePayer(StrEnum):
    CUSTOMER = "customer"
    MERCHANT = "merchant"

    def __str__(self) -> str:
        return str(self.value)
