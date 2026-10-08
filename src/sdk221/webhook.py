import hmac
import time
from hashlib import sha256


def verify_webhook(
    secret: str,
    timestamp_header: str,
    raw_body: str | bytes,
    signature_header: str,
    max_age_seconds: int = 300,
) -> bool:
    """X-221-Signature is `v1=` + hex HMAC-SHA256 of `<timestamp>.<raw body>`; X-221-Timestamp is in Unix seconds.

    Pass the body exactly as received, before any JSON parsing.
    """
    if not timestamp_header.isascii() or not timestamp_header.isdigit():
        return False
    if abs(time.time() - int(timestamp_header)) > max_age_seconds:
        return False
    body = raw_body.encode() if isinstance(raw_body, str) else raw_body
    digest = hmac.new(secret.encode(), timestamp_header.encode() + b"." + body, sha256).hexdigest()
    return hmac.compare_digest(signature_header.encode(), f"v1={digest}".encode())
