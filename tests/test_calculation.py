import pytest

from calculator.tempo_calculator import *

data = [
    ('10:00', 600, 6.0),
    ('5:00', 300, 12.0),
    ('5:10', 310, 11.6),
    ('3:17', 197, 18.3),
    ('6:10', 370, 9.7),
    ('5:20', 320, 11.2),
    ('6:58', 418, 8.6)
]

@pytest.mark.parametrize('str_tempo,seconds_tempo,treadmill_speed', data)
def test_tempo_to_speed_converter_and_back(str_tempo, seconds_tempo, treadmill_speed):
    tempo = Tempo.fromStrPace(str_tempo)
    converted_speed: Speed = convertTempoToSpeed(tempo)
    assert(converted_speed.getTreadmillSpeed() == treadmill_speed)
    tempo = convertSpeedToTempo(converted_speed)
    assert(tempo.getInSeconds() == seconds_tempo)