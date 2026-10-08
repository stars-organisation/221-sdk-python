import pytest

from sdk221 import offline


def test_holidays_outside_the_snapshot_raise():
    assert offline.holidays(2026)
    with pytest.raises(ValueError, match="jours-feries"):
        offline.holidays(2099)


def test_lookups():
    assert offline.snapshot["built_at"]
    assert offline.holiday("2026-04-04")["type"] in ("civile", "religieuse")
    assert offline.operator_for("701234567")["operator"] == "Expresso Sénégal"
    assert offline.bank("K 0010 A")["id"] == "k0010a"
    assert offline.places(level="region", q="thies")[0]["name"] == "Thiès"
    assert offline.place("reg_om6lpn2l")["children"]
