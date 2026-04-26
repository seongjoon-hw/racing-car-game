from model.Randomgeneration import can_move

START_MAX_POSITION = 0


class Game:
    def __init__(self, cars):
        self._cars = cars

    def play_round(self):
        for car in self._cars:
            self.move_car(car)

    def move_car(self, car):
        if can_move():
            car.move()

    def round_results(self):
        return [car.race_status() for car in self._cars]

    def winner_names(self):
        leading_position = self.find_leading_position()
        return [
            car.get_name()
            for car in self._cars
            if car.is_at_position(leading_position)
        ]

    def find_leading_position(self):
        leading_position = START_MAX_POSITION

        for car in self._cars:
            if car.is_ahead_of(leading_position):
                leading_position = car.current_position()

        return leading_position
