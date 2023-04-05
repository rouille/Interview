class Node:
    """Single element of linked list. Each node has two different fields, *'data'*
    containing the value to be stored in the node and *'next'* containing a reference
    to the next element in the list.

    :param str/int/float data: value of the node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class SinglyLinkedList:
    """Linked list as a collection of nodes. First element of the linked list is called
    '*head*'.
    """

    def __init__(self):
        self.head = None

    def create(self, data=None):
        """Create linked list with some elements.

        :param list data: initial element(s) to create linked list.
        """
        if data:
            for d in data:
                self.append(d)

    def append(self, data):
        """Add node at end of linked list.

        :param str/int/float data: value of the node to be added.
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            for n in self:
                pass
            n.next = node

    def insert(self, data, position=None):
        """Add node to the linked list

        :param str/int/float data: value of the node to be inserted.
        :param int position: position where the node will be inserted. If set to None,
            the node will be added at the end of the linked list.
        :raises ValueError: if ``position`` is incorrect.
        """
        node = Node(data)
        if position is None:
            self.append(data)
        elif position == 0:
            node.next = self.head
            self.head = node
        elif self.head is None and position > 0:
            raise ValueError("position is out of range. Linked list is empty")
        else:
            for i, n in enumerate(self):
                if n and i == (position - 1):
                    node.next = n.next
                    n.next = node
                    return
            raise ValueError(
                f"position is out of range. Linked list has {i+1} elements"
            )

    def remove(self, position):
        """Remove node in the linked list.

        :param int position: position of the node to remove.
        :raises ValueError: if ``position``  is incorrect.
        """
        if self.head is None:
            raise ValueError("Linked list is empty")
        elif position == 0:
            self.head = self.head.next
        else:
            for i, n in enumerate(self):
                if n.next and i == (position - 1):
                    n.next = n.next.next
                    return
            raise ValueError(
                f"position is out of range. Linked list has {i+1} elements"
            )

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
