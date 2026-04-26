from model.Car import Car
from model.Game import Game
from utils import Validator
from view import Input
from view import Output


# Current refactored code
class Race:
    def run(self):
        try:
            names = Validator.name_error_summary(Input.get_names())
            rounds = Validator.round_error_summary(Input.get_rounds())

            game = self.create_game(names)
            Output.print_result_header()
            self.play(game, rounds)
            self.finish(game)
        except ValueError as error:
            print(error)

    @staticmethod
    def create_game(names):
        cars = [Car(name) for name in names]
        return Game(cars)

    @staticmethod
    def play(game, rounds):
        for _ in range(rounds):
            game.play_round()
            Output.print_round(game.round_results())

    @staticmethod
    def finish(game):
        Output.print_winner(game.winner_names())
