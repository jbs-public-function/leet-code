# python std library
import unittest
from collections import deque
from typing import *

# internal
from leet_code.data_structures import make_arbitrary_trees, TreeNode


class Solution:
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

class TestTreeInorderTraversal(unittest.TestCase):
    # https://leetcode.com/problems/binary-tree-inorder-traversal/

    def test_case_1(self):
        test_case = [1, None, 2, 3]
        root = make_arbitrary_trees(test_case)
        soln = Solution().inorderTraversal(root)
        assert soln == [1, 3, 2]
