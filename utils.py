import random
import time


def randomArray(n: int, **kwargs):
    min = -1_000_000 if "min" not in kwargs.keys() else kwargs["min"]
    max = 1_000_000 if "max" not in kwargs.keys() else kwargs["max"]

    if "unique" in kwargs.keys() and kwargs["unique"] and max-min+1<n:
        raise ValueError("Not enough items to fill array")

    isInt = not ("floating" in kwargs and kwargs["floating"])

    arr = []
    i = 0
    while i < n:
        num = random.randint(min, max) if isInt else round(random.uniform(min, max), 2)
        while "unique" in kwargs.keys() and kwargs["unique"] and num in arr:
            num = random.randint(min, max) if isInt else round(random.uniform(min, max), 2)
        arr.append(num)
        i += 1

    return arr


def stats(func):
    def wrapper(*args, **kwargs):
        print(f"args: {args}, kwargs: {kwargs}")
        start = time.time()
        wynik = func(*args, **kwargs)
        koniec = time.time()
        print(f"time: {koniec-start:.5f}s")
        print(f"result: {wynik}")
        return wynik
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = func(*args, **kwargs)
        koniec = time.time()
        print(f"time: {koniec-start:.5f}s")
        return wynik
    return wrapper

