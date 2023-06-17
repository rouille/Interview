def quicksort(array, low=0, high=None, inplace=True):
    """Sort array in ascending order. Time complexity is Nlog(N).

    :param list array: unordered list of numbers/letters.
    :param int low: leftmost index of array for sorting.
    :param int high: rightmost index of array for sorting.
    :param bool inplace: done in place, space complexity is O(1).
    :return: (*list*) -- ordered list of numbers/letters when ``inplace`` is False.
    """
    if inplace:
        high = len(array) - 1 if high is None else high

        if low < high:
            # Get pivot index
            pi = partition(array, low, high)
            # Sort left of pivot
            quicksort(array, low, pi - 1)
            # Sort right of pivot
            quicksort(array, pi + 1, high)
    else:
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            return (
                quicksort([x for x in array[1:] if x < pivot], inplace=False)
                + [pivot]
                + quicksort([x for x in array[1:] if x > pivot], inplace=False)
            )


def partition(array, low, high):
    """Find partition position

    :param int low: leftmost index of array for partitioning.
    :param int high: rightmost index of array for partitioning.
    :return: (*int*) -- index of pivot
    """
    # Set pivot value and initialize partition boundary
    pivot = array[low]
    pb = low + 1

    # Traverse array, compare all elements with pivot, send elements with small value
    # to the left of the boundary
    for i in range(pb, high + 1):
        if array[i] < pivot:
            swap(array, i, pb)
            pb += 1

    # Put pivot value between two sides of partition and return position
    swap(array, low, pb - 1)
    return pb - 1


def swap(array, i, j):
    """Swap two elements in an array.

    :param list array: list of numbers/letters.
    :param int i: index of element to be swapped with ``j``
    :param int j: index of element to be swapped with ``i``
    """
    array[i], array[j] = array[j], array[i]
