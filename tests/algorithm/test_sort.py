import pytest

from interview.algorithm.sort import bubblesort, quicksort


@pytest.fixture
def input():
    return ([23, 12.5, 3, 32, -3, -100, 0, 4.25, 5, 1, 83], ["c", "z", "a", "n"])


@pytest.fixture
def output():
    return ([-100, -3, 0, 1, 3, 4.25, 5, 12.5, 23, 32, 83], ["a", "c", "n", "z"])


def test_quicksort(input, output):
    for i, o in zip(input, output):
        assert quicksort(i, inplace=False) == o


def test_quicksort_inplace(input, output):
    for i, o in zip(input, output):
        quicksort(i)
        assert i == o


def test_bubblesort(input, output):
    for i, o in zip(input, output):
        assert bubblesort(i) == o
