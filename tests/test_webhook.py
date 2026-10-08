import hmac
import time
from hashlib import sha256

from sdk221 import verify_webhook

SECRET = "whsec_test"
BODY = '{"id":"evt_1","type":"payment.succeeded"}'


def sign(timestamp: str) -> str:
    return "v1=" + hmac.new(SECRET.encode(), f"{timestamp}.{BODY}".encode(), sha256).hexdigest()


def test_accepts_a_fresh_signed_delivery():
    ts = str(int(time.time()))
    assert verify_webhook(SECRET, ts, BODY, sign(ts))
    assert verify_webhook(SECRET, ts, BODY.encode(), sign(ts))


def test_rejects_tampering_malformed_headers_and_stale_timestamps():
    ts = str(int(time.time()))
    assert not verify_webhook(SECRET, ts, BODY + " ", sign(ts))
    assert not verify_webhook("autre", ts, BODY, sign(ts))
    assert not verify_webhook(SECRET, ts, BODY, "v1=00")
    assert not verify_webhook(SECRET, ts, BODY, "")
    assert not verify_webhook(SECRET, "abc", BODY, sign(ts))
    old = str(int(ts) - 301)
    assert not verify_webhook(SECRET, old, BODY, sign(old))
    assert verify_webhook(SECRET, old, BODY, sign(old), max_age_seconds=600)
