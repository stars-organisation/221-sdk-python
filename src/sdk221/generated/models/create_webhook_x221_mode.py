from enum import StrEnum


class CreateWebhookX221Mode(StrEnum):
    LIVE = "live"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
