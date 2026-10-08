from enum import StrEnum


class KycStatusWithdrawalsBlockedReason(StrEnum):
    KYC_REQUIRED = "kyc_required"
    MERCHANT_SUSPENDED = "merchant_suspended"

    def __str__(self) -> str:
        return str(self.value)
