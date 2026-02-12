from dataclasses import dataclass

METRES_IN_KILOMETERS: float = 1000.0

@dataclass(frozen=True, slots=True)
class Distance:
    meters: int

    @staticmethod
    def fromKm(km: float) -> 'Distance':
        if km < 0:
            raise ValueError("Distance can't be negative")
        return Distance(int(round(km * 1000)))

    @staticmethod
    def fromMeters(meters: int) -> 'Distance':
        return Distance(meters)

    def toKm(self) -> float:
        return round(self.meters / METRES_IN_KILOMETERS, 2)

    def rawKm(self) -> int:
        return int(self.meters / 1000)
