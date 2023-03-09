import pytest

from integration_tests.client import Client

_test_key = """-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIIVEl1i9xtby2IlXDjrlvRNHcNkRXh3U1TNU99sb7uvaoAoGCCqGSM49
AwEHoUQDQgAE3Ez3CzfCzPo3xHaVf/hYDnGrA+aV+iz0kwixt+CN+hyxsgmo7GZ6
t2dglgM+cLzvkhzq1ULE5xoT6JI2/D5NRQ==
-----END EC PRIVATE KEY-----"""
_test_key_fingerprint = "143edb698bd97dff684bf6b21b4ea18436930914"


@pytest.fixture
def client() -> Client:
    return Client("http://localhost:3000", key=_test_key, key_fingerprint=_test_key_fingerprint)
