from enum import StrEnum


class PayErrorLimitType(StrEnum):
    DAILY = "daily"
    DAILY_AMOUNT = "daily_amount"
    DAILY_COUNT = "daily_count"
    MONTHLY = "monthly"
    MONTHLY_AMOUNT = "monthly_amount"
    PER_WITHDRAWAL = "per_withdrawal"

    def __str__(self) -> str:
        return str(self.value)
