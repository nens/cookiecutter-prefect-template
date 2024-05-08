# Pytest will automatically pick up functions called "test_*" in modules called
# "test_*".
# See https://docs.prefect.io/latest/guides/testing/ for prefect testing hints.

from tasks import uppercase_the_text


def test_uppercase_the_text():
    assert uppercase_the_text("Reinout") == "REINOUT"
