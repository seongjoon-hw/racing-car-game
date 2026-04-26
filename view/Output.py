RESULT_HEADER = "실행 결과"
WINNER_HEADER = "최종 우승자 :"


def print_result_header():
    print()
    print(RESULT_HEADER)


def print_round(round_results):
    for result in round_results:
        print(result)

    print()


def print_winner(winner_names):
    print(WINNER_HEADER, ", ".join(winner_names))


# Before refactoring
# DISTANCE_TRAVEL_DISPLAY = "-"
# RESULT_HEADER = "실행 결과"
# WINNER_HEADER = "최종 우승자 :"
#
#
# def print_result_header():
#     print()
#     print(RESULT_HEADER)
#
#
# def format_car(car):
#     track = DISTANCE_TRAVEL_DISPLAY * car.position
#
#     if track:
#         return f"{car.name} : {track}"
#
#     return f"{car.name} :"
#
#
# def print_round(cars):
#     for car in cars:
#         print(format_car(car))
#
#     print()
#
#
# def print_winner(winner):
#     print(WINNER_HEADER, ", ".join(winner))
