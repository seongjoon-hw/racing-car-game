NAME_LENGTH_ERROR_GUIDE = "이름은 1자 이상 5자 이하여야 합니다"
EMPTY_NAME_ERROR_GUIDE = "자동차 이름은 비어 있을 수 없습니다"
ROUND_TYPE_ERROR_GUIDE = "시도 횟수는 숫자여야 합니다"
ROUND_COUNT_ERROR_GUIDE = "시도 횟수는 1 이상이어야 합니다"
NAME_LENGTH_LIMIT = 5
MINIMUM_NUMBER_OF_ROUNDS = 1


def name_error_summary(names):
    normalized_names = [name.strip() for name in names]
    empty_name_validation(normalized_names)
    name_length_validation(normalized_names)
    return normalized_names


def round_error_summary(rounds):
    try:
        round_count = int(rounds)
    except ValueError as error:
        raise ValueError(ROUND_TYPE_ERROR_GUIDE) from error

    handling_round_exceptions(round_count)
    return round_count


def empty_name_validation(names):
    if any(not name for name in names):
        raise ValueError(EMPTY_NAME_ERROR_GUIDE)


def name_length_validation(names):
    for name in names:
        if len(name) > NAME_LENGTH_LIMIT:
            raise ValueError(NAME_LENGTH_ERROR_GUIDE)


def handling_round_exceptions(rounds):
    if rounds < MINIMUM_NUMBER_OF_ROUNDS:
        raise ValueError(ROUND_COUNT_ERROR_GUIDE)
