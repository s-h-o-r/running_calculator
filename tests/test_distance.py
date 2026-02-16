from domain.distance import Distance
import pytest

# fromKm(km) test

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

# toKm(meters) test

@pytest.mark.parametrize(
    "meters, expected_km",
    [
        (900, 0.9),
        (1, 0.001),
        (999, 0.999),
        (1000, 1.0),
        (1001, 1.001),
        (1101, 1.101),
        (99999, 99.999)
    ]
)
def test_toKm_conversion(meters, expected_km):
    distance = Distance.fromMeters(meters)
    assert distance.toKm() == expected_km

# rawKm(meters) test

@pytest.mark.parametrize(
    "meters, expected_raw_km",
    [
        (900, 0),
        (1, 0),
        (999, 0),
        (1000, 1),
        (1001, 1),
        (1101, 1),
        (99999, 99)
    ]
)
def test_rawKm_conversion(meters, expected_raw_km):
    distance = Distance.fromMeters(meters)
    assert distance.rawKm() == expected_raw_km