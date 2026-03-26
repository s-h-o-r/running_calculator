from parsers.pace_parser import parse_speed_or_tempo
from domain.pace import Tempo, Speed
from calculator.tempo_calculator import *

def convert_pace_or_tempo(raw_message: str) -> str:
    parsedInput = parse_speed_or_tempo(raw_message)
    if parsedInput.error is not None or not parsedInput.is_valid():
        return 'Неверный формат скорости или темпа. Попробуйте снова. Пример: 7:15, 10, 8.5, 9,3'
    
    if isinstance(parsedInput.value, Speed):
        convertedTempo = convertSpeedToTempo(parsedInput.value)
        return f'{parsedInput.value.getTreadmillSpeed()} км/ч = {convertedTempo.str()} мин/км'

    if isinstance(parsedInput.value, Tempo):
        convertedSpeed = convertTempoToSpeed(parsedInput.value)
        return f'{parsedInput.value.str()} мин/км = {convertedSpeed.getTreadmillSpeed()} км/ч'
    
    return 'Ошибка сервера'