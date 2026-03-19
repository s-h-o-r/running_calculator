from dataclasses import dataclass
from typing import Optional, Union
from domain.pace import Speed, Tempo

@dataclass(frozen=True)
class ParsedInput:
    value: Union[Speed, Tempo, None] = None
    error: Optional[str] = None

    def is_valid(self) -> bool:
        return self.error is None or self.value is not None


def parse_speed_or_tempo(raw: str) -> ParsedInput:
    pass