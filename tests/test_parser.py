import pytest

from domain.pace import Speed, Tempo
from parsers.pace_parser import ParsedInput

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