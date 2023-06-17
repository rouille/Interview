from interview.algorithm.sort import quicksort


def test_quicksort():
    input = ([23, 12.5, 3, 32, -3, -100, 0, 4.25, 5, 1, 83], ["c", "z", "a", "n"])
    expected = ([-100, -3, 0, 1, 3, 4.25, 5, 12.5, 23, 32, 83], ["a", "c", "n", "z"])
    for i, e in zip(input, expected):
        assert quicksort(i, inplace=False) == e


def test_quicksort_inplace():
    input = [23, 12.5, 3, 32, -3, -100, 0, 4.25, 5, 1, 83]
    quicksort(input, low=3, high=7)
    assert input == [23, 12.5, 3, -100, -3, 0, 4.25, 32, 5, 1, 83]
