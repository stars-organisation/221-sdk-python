from enum import StrEnum


class OfferBenefitType(StrEnum):
    FIXED = "fixed"
    PERCENT = "percent"

    def __str__(self) -> str:
        return str(self.value)
