METRES_IN_KILOMETERS = 1000

class Distance:
    metres: int

    def __init__(self, metres: int = 0) -> None:
        self.metres = metres

    def setDistance(self, newDistance: int|float) -> None:
        isKm: bool = (isinstance(newDistance, int) and newDistance < 100) or (isinstance(newDistance, float))
        if(isKm):
            newDistance = int(newDistance * METRES_IN_KILOMETERS)

        self.metres = int(newDistance)

    def getMetres(self) -> int:
        return self.metres

    def getKilometers(self) -> float:
        return self.metres / 1000