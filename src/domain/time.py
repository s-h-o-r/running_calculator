SECONDS_IN_MINUTE: int = 60

# Скорость бега в км/ч
class Speed:
    speed: float

    def __init__(self, speed: float = 0.) -> None:
        self.speed = speed

    def getSpeed(self) -> float:
        return round(self.speed, 2)
    
    def setSpeed(self, newSpeed: float) -> None:
        self.speed = newSpeed

# Темп бега в минутах на километр
class Tempo:
    minutes: int
    seconds: int

    def __init__(self, minutes: int = 0, seconds: int = 0) -> None:
        self.minutes = minutes
        self.seconds = seconds

    def setMinutes(self, minutes: int) -> None:
        self.minutes = minutes

    def setSeconds(self, seconds: int) -> None:
        self.minutes = int(seconds / SECONDS_IN_MINUTE)
        self.seconds = seconds % SECONDS_IN_MINUTE

    def getMinutes(self) -> int:
        return self.minutes

    def getSeconds(self) -> int:
        return self.seconds

    def getTempoInSeconds(self) -> int:
        return self.getSeconds() + self.getMinutes() * SECONDS_IN_MINUTE
