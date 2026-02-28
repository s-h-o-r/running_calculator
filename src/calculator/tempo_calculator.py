from domain.distance import Distance, METRES_IN_KILOMETERS
from domain.pace import *

MINUTES_IN_HOUR: int = 60

def convertSpeedToTempo(speed: Speed) -> Tempo:
    return Tempo.fromMinutes(MINUTES_IN_HOUR / speed.raw_value)

def convertTempoToSpeed(tempo: Tempo) -> Speed:
    return Speed(raw_value=float(MINUTES_IN_HOUR / float(tempo.getInSeconds() / SECONDS_IN_MINUTE)))

