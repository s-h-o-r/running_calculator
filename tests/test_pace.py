import pytest

from domain.pace import Tempo

data = [
    (0, '0:00', 0, 0, 0),
    (2, '2:00', 120, 2, 0),
    (2.5, '2:30', 150, 2, 30),
    (5.2, '5:12', 312, 5, 12),
    (5.2, '5:12', 312, 5, 12),
    (7.75, '7:48', 468, 7, 48),
    ('10', '10:00', 600, 10, 0),
]

@pytest.mark.parametrize("minutes,expected_str,expected_seconds,expected_minutes,expected_only_seconds", data)
def test_from_minutes(minutes, expected_str, expected_seconds, expected_minutes, expected_only_seconds):
    tempo = Tempo.fromMinutes(minutes)
    assert(tempo.getInSeconds() == expected_seconds)
    assert(tempo.getOnlyMinutes() == expected_minutes)
    assert(tempo.getOnlySeconds() == expected_only_seconds)
    assert(tempo.str() == expected_str)


@pytest.mark.parametrize("_,minutes_str,expected_seconds,expected_minutes,expected_only_seconds", data)
def test_from_str(_, minutes_str, expected_seconds, expected_minutes, expected_only_seconds):
    tempo = Tempo.fromStrPace(minutes_str)
    assert(tempo.getInSeconds() == expected_seconds)
    assert(tempo.getOnlyMinutes() == expected_minutes)
    assert(tempo.getOnlySeconds() == expected_only_seconds)
    assert(tempo.str() == minutes_str)