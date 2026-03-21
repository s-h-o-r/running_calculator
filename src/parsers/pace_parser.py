from dataclasses import dataclass
from typing import Optional, Union
from domain.pace import Speed, Tempo, SECONDS_IN_MINUTE

@dataclass(frozen=True)
class ParsedInput:
    value: Union[Speed, Tempo, None] = None
    error: Optional[str] = None

    def is_valid(self) -> bool:
        return self.error is None and self.value is not None

@dataclass(frozen=True)
class ParsedPace:
    minutes: int = None
    seconds: int = None

    def is_valid(self):
        return (self.minutes is not None 
                and self.seconds is not None 
                and self.seconds <= 60)


def parse_pace(raw_pace: str, delim_pos: int = None) -> ParsedPace:
    if(raw_pace is None):
        return ParsedPace()
    
    delim_pos = delim_pos if delim_pos is None else raw_pace.find(':')
    if(delim_pos == -1):
        return ParsedPace()

    left_part = raw_pace[:delim_pos]
    right_part = raw_pace[delim_pos + 1:]
    minutes = int(left_part) if left_part.isdecimal() else None
    seconds = int(right_part) if right_part.isdecimal() else None

    return ParsedPace(minutes, seconds)

def parse_speed_or_tempo(raw: str = '') -> ParsedInput:
    raw = raw.strip() if raw is not None else ''
    if(raw == ''):
        return ParsedInput(error='Input is empty')

    delim_pos = raw.find(':')
    if(delim_pos != -1):
        parsed_pace: ParsedPace = parse_pace(raw, delim_pos)

        if(parsed_pace.is_valid()):
            return ParsedInput(value=Tempo(parsed_pace.minutes * SECONDS_IN_MINUTE + parsed_pace.seconds))
        else:
            return ParsedInput(error='Input looks like pace but it\'s incorrect')


    return ParsedInput(value=Speed(raw_value=10.0))