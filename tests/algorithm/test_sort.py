from interview.algorithm.sort import bubblesort, quicksort


def test_quicksort():
    input = ([23, 12.5, 3, 32, -3, -100, 0, 4.25, 5, 1, 83], ["c", "z", "a", "n"])
    expected = ([-100, -3, 0, 1, 3, 4.25, 5, 12.5, 23, 32, 83], ["a", "c", "n", "z"])
    for i, e in zip(input, expected):
        assert quicksort(i, inplace=False) == e


def test_quicksort_inplace():
    input = [23, 12.5, 3, 32, -3, -100, 0, 4.25, 5, 1, 83]
    quicksort(input, low=3, high=7)
    assert input == [23, 12.5, 3, -100, -3, 0, 4.25, 32, 5, 1, 83]


def test_bubblesort():
    input = [12, 3, 1, -1, 30, 14, 12, 0, 25, 9, 4]
    assert bubblesort(input) == [-1, 0, 1, 3, 4, 9, 12, 12, 14, 25, 30]
