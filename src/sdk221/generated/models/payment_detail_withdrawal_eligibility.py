from enum import StrEnum


class PaymentDetailWithdrawalEligibility(StrEnum):
    CONFIRMED = "confirmed"
    NOT_CONFIRMED = "not_confirmed"

    def __str__(self) -> str:
        return str(self.value)
