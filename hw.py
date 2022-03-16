class _Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self._root = root
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, item):
        return self._search(self._root, item) is not None

    def _search(self, subtree: _Node, target):
        if subtree is None:
            return None
        elif target < subtree.value:
            return self._search(subtree.left, target)
        elif target > subtree.value:
            return self._search(subtree.right, target)
        else:
            return subtree

    def _find_min(self, subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._find_min(subtree.left)

    def _find_max(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._find_max(subtree.right)

    def insert(self, subtree, value):
        if subtree is None:
            subtree = _Node(value)
        elif subtree.value > value:
            subtree.left = self.insert(subtree.left, value)
        elif subtree.value < value:
            subtree.right = self.insert(subtree.right, value)
        return subtree

    def delete_node(self, subtree: _Node, value):
        if subtree is None:
            return subtree
        elif subtree.value < value:
            subtree.right = self.delete_node(subtree.right, value)
            return subtree
        elif subtree.value > value:
            subtree.left = self.delete_node(subtree.left, value)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                elif subtree.right is not None:
                    return subtree.right
            else:
                successor = self._find_min(subtree.right)
                subtree.value = successor.value
                subtree.right = self.delete_node(subtree.right, successor.value)
                return subtree

    def remover(self, node):
        self._root = self.delete_node(self._root, node)


def preorder_traversal(subtree, preord=None):
    if preord is None:
        preord = list()
    if subtree is not None:
        preord.append(subtree.value)
        preorder_traversal(subtree.left, preord)
        preorder_traversal(subtree.right, preord)
    return preord


def inorder_traversal(subtree, inord=None):
    if inord is None:
        inord = list()
    if subtree is not None:
        inorder_traversal(subtree.left, inord)
        inord.append(subtree.value)
        inorder_traversal(subtree.right, inord)
    return inord
