import pytest

from interview.data_structure.binary_search_tree import BinarySearchTree


@pytest.fixture
def data():
    return [25, 15, 22, 50, 70, 90, 18, 10, 24, 12, 4, 35, 31, 44, 66]


#                     25
#            15                50
#       10        22      35        70
#     4   12    18  24  31  44    66  90


def test_init_root_node():
    bst = BinarySearchTree()
    assert bst.root == None


def test_in_order_traversal(data):
    bst = BinarySearchTree()
    for d in data:
        bst.insert(d)

    assert bst.in_order_traversal() == sorted(set(data))


def test_pre_order_traversal(data):
    bst = BinarySearchTree()
    for d in data:
        bst.insert(d)
    assert bst.pre_order_traversal() == [
        25,
        15,
        10,
        4,
        12,
        22,
        18,
        24,
        50,
        35,
        31,
        44,
        70,
        66,
        90,
    ]


def test_post_order_traversal(data):
    bst = BinarySearchTree()
    for d in data:
        bst.insert(d)
    assert bst.post_order_traversal() == [
        4,
        12,
        10,
        18,
        24,
        22,
        15,
        31,
        44,
        35,
        66,
        90,
        70,
        50,
        25,
    ]


def test_get_extremum(data):
    bst = BinarySearchTree()
    for d in data:
        bst.insert(d)

    assert min(data) == bst.get_min()
    assert max(data) == bst.get_max()


def test_check_if_node_in_tree(data):
    bst = BinarySearchTree()
    assert bst.exist(data[0]) == False
    for d in data:
        bst.insert(d)

    assert bst.exist(data[0])
    assert bst.exist(data[round(len(data) / 2)])
    assert bst.exist(data[-1])
    assert bst.exist(max(data) + 1) == False
