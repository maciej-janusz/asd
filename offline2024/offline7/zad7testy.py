# zad7testy.py
from testy import *
from zad7test_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg(arg):
    return deepcopy(arg)


def printarg(*arg):
    print(f'L = {limit(arg[0])}')


def printhint(hint):
    print("Poprawny wynik: ", limit(hint))


def printsol(sol):
    print("Otrzymany wynik: ", limit(sol))


def check(hint, sol):
    return hint == sol


def generate_tests(num_tests=None):
    global TEST_SPEC
    TESTS = []

    L = ['....', '..#.', '..#.', '....']
    newtest = {}
    newtest["arg"] = [L]
    newtest["hint"] = 12
    TESTS.append(newtest)

    L = ['......', '#..#..', '.#..#.', '##..#.', '......', '......']
    newtest = {}
    newtest["arg"] = [L]
    newtest["hint"] = 12
    TESTS.append(newtest)

    L = ['....#...##', '...#....##', '#.........', '.......#..', '.......##.', '...#....#.', '#....#....', '##.....#.#',
         '..........', '......#...']
    newtest = {}
    newtest["arg"] = [L]
    newtest["hint"] = 40
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)

    return TESTS


def runtests(f, all_tests=True):
    internal_runtests(copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME)