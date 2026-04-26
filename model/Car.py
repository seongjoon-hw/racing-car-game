START_CAR_POSITION = 0
TRAVEL_DISTANCE = 1
TRACK_SYMBOL = "-"


class Car:
    def __init__(self, name):
        self._name = name
        self._position = START_CAR_POSITION

    def move(self):
        self._position += TRAVEL_DISTANCE

    def get_name(self):
        return self._name

    def current_position(self):
        return self._position

    def is_at_position(self, position):
        return self._position == position

    def is_ahead_of(self, position):
        return self._position > position

    def race_status(self):
        track = TRACK_SYMBOL * self._position

        if track:
            return f"{self._name} : {track}"

        return f"{self._name} :"
