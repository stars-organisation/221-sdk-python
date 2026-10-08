from enum import StrEnum


class RefundCoreReason(StrEnum):
    CUSTOMER_REQUEST = "customer_request"
    DUPLICATE = "duplicate"
    OTHER_DOCUMENTED = "other_documented"
    PRODUCT_NOT_DELIVERED = "product_not_delivered"

    def __str__(self) -> str:
        return str(self.value)
