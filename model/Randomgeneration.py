import random

min_random_num = 0
max_random_num = 9
baseline_value = 4

def can_move():
    return random.randint(min_random_num, max_random_num) >= baseline_value