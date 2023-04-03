import pytest

from interview.data_structure.singly_linked_list import Node, SinglyLinkedList


@pytest.fixture
def data():
    return ["a", 33, 12.5, "ABC"]


def test_init_node():
    n = Node("a")
    assert n.data == "a"
    assert n.next is None


def test_init_singly_linked_list():
    sll = SinglyLinkedList()
    assert sll.head is None


def test_create_singly_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    assert str(sll) == " -> ".join(map(str, data)) + " -> None"


def test_traverse_singly_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    for n, d in zip(sll, data):
        assert n.data == d


def test_add_node_at_beginning_of_singly_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    sll.insert("first", position=0)
    for n, d in zip(sll, ["first"] + data):
        assert n.data == d


def test_add_node_at_beginning_of_empty_singly_linked_list():
    sll = SinglyLinkedList()
    sll.insert("new", position=0)
    assert str(sll) == "new -> None"


def test_add_node_at_end_of_singly_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    sll.append("last")
    for n, d in zip(sll, data + ["last"]):
        assert n.data == d


def test_add_node_at_end_of_empty_singly_linked_list():
    sll = SinglyLinkedList()
    sll.append("new")
    assert str(sll) == "new -> None"


def test_add_node_at_middle_of_singly_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    sll.insert("middle", position=3)
    data.insert(3, "middle")
    for n, d in zip(sll, data):
        assert n.data == d


def test_add_node_at_wrong_position_of_empty_linked_list():
    sll = SinglyLinkedList()
    with pytest.raises(
        ValueError, match="position is out of range. Linked list is empty"
    ):
        assert sll.insert("new", position=3)


def test_add_node_at_wrong_position_of_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    with pytest.raises(
        ValueError,
        match=f"position is out of range. Linked list has {len(data)} elements",
    ):
        assert sll.insert("new", position=10)


def test_remove_node_in_empty_linked_list():
    sll = SinglyLinkedList()
    with pytest.raises(ValueError, match="Linked list is empty"):
        assert sll.remove(2)


def test_remove_first_node_in_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    sll.remove(0)
    for n, d in zip(sll, data[1:]):
        assert n.data == d


def test_remove_last_node_in_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    sll.remove(len(data) - 1)
    for n, d in zip(sll, data[:-1]):
        assert n.data == d


def test_remove_node_in_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    sll.remove(2)
    data.pop(2)
    for n, d in zip(sll, data):
        assert n.data == d


def test_remove_node_at_wrong_position_in_linked_list(data):
    sll = SinglyLinkedList()
    sll.create(data)
    with pytest.raises(
        ValueError,
        match=f"position is out of range. Linked list has {len(data)} elements",
    ):
        assert sll.remove(20)
