import random


def gen_random_record():
    return [random.randint(1, 40) for _ in range(3)]


def gen_phone_number():
    a = [str(random.randint(1, 9)) for x in range(9)]
    return int(''.join(a))
