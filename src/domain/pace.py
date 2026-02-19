from dataclasses import dataclass

SECONDS_IN_MINUTE: int = 60

# Скорость бега в км/ч
@dataclass(slots=True)
class Speed:
    speed: float = 0.

    def getSpeed(self) -> float:
        return round(self.speed, 1)

    def setSpeed(self, speed: int|float) -> None:
        self.speed = round(speed, 1)

# Темп бега в минутах на километр
@dataclass(frozen=True, slots=True)
class Tempo:
    seconds: int

    @staticmethod
    def fromMinutes(minutes: int|float):
        minutes = round(minutes, 1) if isinstance(minutes, float) else int(minutes)
        return Tempo(int(minutes * SECONDS_IN_MINUTE))

    @staticmethod
    def fromStrPace(strPace: str):
        if(not isinstance(strPace, str)):
            raise ValueError('Expected string')
        elif(strPace[0] == ':' or 0 >= strPace.count(':') > 1):
            raise ValueError('Expected string formatting as "min:sec"')

        delim_pos = strPace.find(':')
        minutes = int(strPace[:delim_pos])
        seconds = int(strPace[delim_pos + 1:])
        if(minutes < 0 or seconds < 0):
            raise ValueError('Minutes and seconds in tempo str cannot be negative')
        if(seconds >= SECONDS_IN_MINUTE):
            raise ValueError(f'Max value of seconds is 59, but you type {seconds}')
        return Tempo(seconds + minutes * SECONDS_IN_MINUTE)

    def getOnlyMinutes(self) -> int:
        return int(self.seconds / SECONDS_IN_MINUTE) 

    def getInSeconds(self) -> int:
        return self.seconds
    
    def getOnlySeconds(self) -> int:
        return int(self.seconds % SECONDS_IN_MINUTE)

    def str(self) -> str:
        return f'{self.getOnlyMinutes()}' + ':' + f'{self.getOnlySeconds()}'.rjust(2, '0')

string = '10'
print(Tempo.fromMinutes(string))
