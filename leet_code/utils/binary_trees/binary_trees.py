from collections import deque
import unittest
from typing import *


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_arbitrary_trees(trees: Optional[List[Optional[int]]]) -> Optional[BinaryTree]:

    if not trees:
        return None

    if trees[0] is None:
        return None

    root = BinaryTree(trees[0])
    idx = 1
    q = deque([root])
    while q:
        k = len(q)
        limit = 2 * k + idx
        while idx < limit:
            parent = q.pop()

            if idx >= len(trees):
                return root

            left_tree = None if not trees[idx] else BinaryTree(trees[idx])
            parent.left = left_tree
            idx += 1
            if left_tree:
                q.appendleft(left_tree)

            if idx + 1 >= len(trees):
                return root

            right_tree = None if not trees[idx] else BinaryTree(trees[idx])
            parent.right = right_tree
            idx += 1

            if right_tree:
                q.appendleft(right_tree)

        idx = limit
    return root


def breadth_first_search(root: Optional[BinaryTree]) -> List[Optional[List[int]]]:
    if root is None:
        return []

    data = []
    q = deque([root])
    child_q = deque([])
    while q:
        child_data = []
        while q:
            parent = q.pop()
            child_data.append(parent.val)
            if parent.left:
                child_q.appendleft(parent.left)
            if parent.right:
                child_q.appendleft(parent.right)
        data.append(child_data)

        tmp_q = q
        q = child_q
        child_q = tmp_q

    return data


def printTree(root):
    if not root:
        print("None")
        return
    printTree(root.left)
    print("", root.val, end=" ")
    printTree(root.right)


# trees = make_arbitrary_trees([1, None, 3, 4])
"""
            1
        None         3
                4        None
"""
# trees = make_trees([1, 2, 3, 4, 5, 6, 6, 6, 6])
trees = make_arbitrary_trees([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
trees = make_arbitrary_trees([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(breadth_first_search(trees))
"""
                           1
                2                      3
            4       5            6           6
        6      6
"""
