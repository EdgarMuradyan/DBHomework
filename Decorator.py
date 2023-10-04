import math
from datetime import datetime, timedelta


def decorator(func):
    def wrapper(a):
        current_time = datetime.now()
        func(a)
        result = datetime.now() - current_time
        print("time = ", result.microseconds)

    return wrapper


@decorator
def my_function(n):
    for i in range(n):
        print(i, end=", ")
    print("\n")


# stex pordzel em decoratorov is_prime functioni jamanaky chapem
# @decorator
def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    # print(n)
    return True


def prime_numbers():
    n = 0
    while n < 10:
        n += 1
        if is_prime(n):
            print(n)


if __name__ == '__main__':
    prime_numbers()
    my_function(100)
