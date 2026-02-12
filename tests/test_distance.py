from domain.distance import Distance
import pytest

@pytest.mark.parametrize(
    "km, expected_meters",
    [
        (0, 0),
        (0.0, 0),
        (0.2, 200),
        (1, 1000),
        (1.4, 1400),
        (5.42, 5420),
        (10.687, 10687),
        (412.68724, 412687),
        (712.68754, 712688)
    ]
)


def test_positive_and_zero(km, expected_meters):
    distance = Distance.fromKm(km)
    assert distance.meters == expected_meters

def test_negative_km():
    with pytest.raises(ValueError):
        Distance.fromKm(-1)