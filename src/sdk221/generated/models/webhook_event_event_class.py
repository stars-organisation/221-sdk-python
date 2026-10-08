from enum import StrEnum


class WebhookEventEventClass(StrEnum):
    DISPUTES = "disputes"
    PAYMENTS = "payments"
    PAYOUTS = "payouts"
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
