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
        ('7:43f', ParsedInput(value=None, error='')),
        ('f7:43 ', ParsedInput(value=None, error='')),
        ('5:61', ParsedInput(value=None, error='')),
        ('5:60', ParsedInput(value=None, error='')),
        ('03:50', ParsedInput(value=Tempo(seconds=230), error=None)),
        ('03:5', ParsedInput(value=None, error='')),
        ('12::50', ParsedInput(value=None, error='')),
        ('-4:42', ParsedInput(value=None, error='')),
        ('12.2', ParsedInput(value=Speed(12.2), error=None)),
        ('8,15', ParsedInput(value=Speed(8.15), error=None)),
        ('8,1.5', ParsedInput(value=None, error='')),
        ('8.1.5', ParsedInput(value=None, error='')),
        ('20.', ParsedInput(value=Speed(20.0), error=None)),
        ('  .5    ', ParsedInput(value=Speed(0.5), error=None)),
        ('IV:XX', ParsedInput(value=None, error='')),
    ]
)
def test_parse_speed_or_tempo(raw_input, expected_parsed_input):
    parsed_input = parse_speed_or_tempo(raw_input)
    assert parsed_input.is_valid() == expected_parsed_input.is_valid()
    assert parsed_input.value == expected_parsed_input.value
    assert type(parsed_input.error) == type(expected_parsed_input.error)