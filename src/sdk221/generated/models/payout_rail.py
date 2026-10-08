from enum import StrEnum


class PayoutRail(StrEnum):
    BF_MOOV = "bf_moov"
    BF_ORANGE = "bf_orange"
    BF_WAVE = "bf_wave"
    BJ_MOOV = "bj_moov"
    BJ_MTN = "bj_mtn"
    CI_MOOV = "ci_moov"
    CI_MTN = "ci_mtn"
    CI_ORANGE = "ci_orange"
    CI_WAVE = "ci_wave"
    SN_ORANGE = "sn_orange"
    SN_WAVE = "sn_wave"
    TG_MOOV = "tg_moov"
    TG_TOGOCELL = "tg_togocell"

    def __str__(self) -> str:
        return str(self.value)
