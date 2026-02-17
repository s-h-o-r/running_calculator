import pytest

from domain.pace import *

@pytest.mark.parametrize(
    "minutes,expected_seconds",
    [
        (0, 0),
        (1, 60),
        (2, 120),
        (1.5, 90),
        (1.99, 119)
    ]
)
def test_tempo_from_minutes(minutes, expected_seconds):
    tempo = Tempo.fromMinutes(minutes)
    assert tempo.getInSeconds() == expected_seconds
    assert tempo.getOnlyMinutes() == int(expected_seconds / SECONDS_IN_MINUTE)
    assert tempo.getOnlySeconds() == int(expected_seconds % SECONDS_IN_MINUTE)