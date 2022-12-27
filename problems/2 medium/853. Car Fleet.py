class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [float(target-pos)/speed  for pos, speed  in sorted(zip(position, speed))]
        slowest = cars[-1]
        fleets = 1
        print(cars)
        for car in reversed(cars):
            if car > slowest:
                fleets += 1
                slowest = car
        return fleets