NAME_INPUT_PROMPT = "경주할 자동차 이름을 입력하세요.(이름은 쉼표(,) 기준으로 구분)\n"
ROUND_INPUT_PROMPT = "시도할 횟수는 몇 회인가요?\n"

def get_names():
    return input(NAME_INPUT_PROMPT).split(",")


def get_rounds():
    return input(ROUND_INPUT_PROMPT)
