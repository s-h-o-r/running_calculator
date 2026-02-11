from dataclasses import dataclass

METRES_IN_KILOMETERS: float = 1000.0

@dataclass(frozen=True, slots=True)
class Distance:
    meters: int

    @staticmethod
    def fromKm(km: float) -> 'Distance':
        return Distance(int(km * 1000))

    @staticmethod
    def fromMeters(meters: int) -> 'Distance':
        return Distance(meters)

    def toKm(self) -> float:
        return round(self.meters / METRES_IN_KILOMETERS, 2)

    def rawKm(self) -> int:
        return int(self.meters / 1000)

# make tests with pytest with this code
distance = Distance.fromMeters(1234)
print(distance.meters)
print(distance.toKm())
print(distance.rawKm())
