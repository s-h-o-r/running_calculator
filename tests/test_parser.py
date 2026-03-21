import pytest

from domain.pace import Speed, Tempo
from parsers.pace_parser import ParsedInput, parse_speed_or_tempo

@pytest.mark.parametrize(
    'value, error, expected_result',
    [
        (None, None, False),
        (Speed(), None, True),
        (Tempo(seconds=0), None, True),
        (None, 'error', False),
        (None, '', False)
    ]
)
def test_is_valid_input(value, error, expected_result):
    input = ParsedInput(value=value, error=error)
    assert input.is_valid() == expected_result

# In this test error message doesn't matter
@pytest.mark.parametrize(
    'raw_input, expected_parsed_input',
    [
        (None, ParsedInput(value=None, error='')),
        ('', ParsedInput(value=None, error='')),
        ('10', ParsedInput(value=Speed(raw_value=10.0), error=None)),
        ('  ', ParsedInput(value=None, error='')),
        ('10:00', ParsedInput(value=Tempo(seconds=600), error=None)),
        (' 5:47 ', ParsedInput(value=Tempo(seconds=347), error=None)),
        ('5:61', ParsedInput(value=None, error=''))
    ]
)
def test_parse_speed_or_tempo(raw_input, expected_parsed_input):
    parsed_input = parse_speed_or_tempo(raw_input)
    assert parsed_input.is_valid() == expected_parsed_input.is_valid()
    assert parsed_input.value == expected_parsed_input.value
    assert type(parsed_input.error) == type(expected_parsed_input.error)