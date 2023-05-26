class Node:
    """Single element of binary search tree. Each node has three different fields,
    '*data*' which acts as the key to be provided, '*left*' and '*right*' denominating
    both children of the node.

    :param str/int/float data: value of the node.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data


class BinarySearchTree:
    """Binary search tree as a collection of nodes organized in an ordered manner.
    Each node has a value greater than all of its left child nodes and less than all
    of its right child nodes.
    """

    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert node(s) in tree.

        :param int/list/tuple/set data: value(s) of nodes to insert in tree.
        """
        if isinstance(data, int):
            data = [data]

        for d in data:
            self.root = self._insert(self.root, d)

    def _insert(self, node, data):
        """Insert node in tree.

        :param Node node: current node.
        :param int data: value of the node to be added to tree.
        :return: (*Node*) -- inserted node.
        """
        if node is None:
            node = Node(data)
        elif node.data > data:
            node.left = self._insert(node.left, data)
        elif node.data < data:
            node.right = self._insert(node.right, data)

        return node

    def exist(self, value):
        """Check if a value is in tree.

        :param int value: value of the node.
        :return: (**bool**) -- is ``value`` in tree.
        """
        if self.root is None:
            print("Tree is empty")
            return False

        return self._exist(self.root, value)

    def _exist(self, node, data):
        """Check if value is in Tree

        :param Node node: current node.
        :param int data: value of the node to look for.
        """
        if node is None:
            return False
        elif node.data == data:
            return True
        elif node.data > data:
            return self._exist(node.left, data)
        else:
            return self._exist(node.right, data)

    def get_min(self):
        """Return min value in tree"""
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def get_max(self):
        """Return min value in tree"""
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def in_order_traversal(self):
        """Visit left branch, then the current node, and finally the right branch.

        :return: (*list*) -- values of nodes.
        """
        return self._in_order_traversal(self.root)

    def pre_order_traversal(self):
        """Visit current node, then left branch, and finally right branch.

        :return: (*list*) -- values of nodes.
        """
        return self._pre_order_traversal(self.root)

    def post_order_traversal(self):
        """Visit left branch, then right branch, and finally current node.

        :return: (*list*) -- values of nodes.
        """
        return self._post_order_traversal(self.root)

    def _in_order_traversal(self, node):
        """Visit left branch, then the current node, and finally the right branch.

        :param Node node: current node.
        :return: (*list*) -- values of nodes.
        """
        values = []
        if node.left:
            values += self._in_order_traversal(node.left)
        if node.data:
            values.append(node.data)
        if node.right:
            values += self._in_order_traversal(node.right)

        return values if len(values) > 0 else print("Tree is empty")

    def _pre_order_traversal(self, node):
        """Visit current node, then left branch, and finally right branch.

        :param Node node: current node.
        :return: (*list*) -- values of nodes.
        """
        values = []
        if node.data:
            values.append(node.data)
        if node.left:
            values += self._pre_order_traversal(node.left)
        if node.right:
            values += self._pre_order_traversal(node.right)

        return values if len(values) > 0 else print("Tree is empty")

    def _post_order_traversal(self, node):
        """Visit left branch, then right branch, and finally current node.

        :param Node node: current node.
        :return: (*list*) -- values of nodes.
        """
        values = []
        if node.left:
            values += self._post_order_traversal(node.left)
        if node.right:
            values += self._post_order_traversal(node.right)
        if node.data:
            values.append(node.data)

        return values if len(values) > 0 else print("Tree is empty")
