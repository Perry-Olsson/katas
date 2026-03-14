class Trip:
    def __init__(self, distance: int, next = None):
        self._distance = distance
        if next is None:
            self._incr = -2
            self._next = Trip(0, self)
        else:
            self._incr = 2
            self._next = next

    def incr(self):
        self._distance += self._incr

class Trips:
    def __init__(self, initial_distance: int):
        self.trip = Trip(initial_distance)

    def distance(self):
        if self.trip._distance == 0:
            self.trip = self.trip._next

        return self.trip._distance

    def next(self):
        self.trip = self.trip._next

    def incr(self):
        self.trip.incr()
        self.trip._next.incr()
        if self.trip._incr == 2:
            self.trip = self.trip._next

    def __str__(self):
        return f"Trip: {self.trip._distance}, Next: {self.trip._next._distance}"


class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        starting_travel_distance = 1 if num_rows == 1 else num_rows * 2 - 2
        trip = Trips(starting_travel_distance)

        result = ""
        for i in range(min(num_rows, len(s))):
            char_index = i
            while char_index < len(s):
                print(f"CharIdx: {char_index}, Char: {s[char_index]}")
                print(trip)
                result += s[char_index]
                char_index += trip.distance()
                trip.next()

            trip.incr()
        return result
