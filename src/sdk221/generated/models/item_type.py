from enum import StrEnum


class ItemType(StrEnum):
    DRIVING_LICENCE = "driving_licence"
    NATIONAL_ID = "national_id"
    PASSPORT = "passport"
    RESIDENCE_PERMIT = "residence_permit"

    def __str__(self) -> str:
        return str(self.value)
