# python std library
import unittest
from collections import deque
from typing import *

# internal
from leet_code.data_structures import make_arbitrary_trees, TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return max_depth

        q = deque([root])
        child_q = deque([])

        while q:
            max_depth += 1
            while q:
                parent = q.pop()
                if parent.left:
                    child_q.append(parent.left)
                if parent.right:
                    child_q.append(parent.right)
            tmp_q = q
            q = child_q
            child_q = tmp_q
        return max_depth

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []

        def depth_first_search(root: Optional[TreeNode]):
            if not root:
                return
            depth_first_search(root.left)
            data.append(root.val)
            depth_first_search(root.right)

        depth_first_search(root)
        return data


class TestTrees(unittest.TestCase):
    """
    Binary tree related tasks
    """
    def test_case_max_depth(self):
        test_case = [3, 9, 20, None, None, 15, 7]
        root = make_arbitrary_trees(test_case)
        depth = Solution().maxDepth(root)

        assert depth == 3

    def test_case_inorder_tree_traversal(self):
        test_case = [1, None, 2, 3]
        root = make_arbitrary_trees(test_case)
        soln = Solution().inorderTraversal(root)
        assert soln == [1, 3, 2]
