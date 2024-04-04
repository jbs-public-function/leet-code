import unittest
from leet_code.data_structures import (
    make_arbitrary_trees,
    breadth_first_search,
    BinaryTree,
    make_nodes,
    unpack_nodes,
    ListNode
)


class TestDataStructures(unittest.TestCase):
    def test_make_even_trees_bfs(self):
        root = make_arbitrary_trees([1, 2, 3, None, 4, 5, 6, 7])
        search = breadth_first_search(root)
        assert search == [[1], [2, 3], [4, 5, 6], [7]]

    def test_make_odd_trees_bfs(self):
        root = make_arbitrary_trees([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        search = breadth_first_search(root)
        assert search == [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]]

    def test_unpack_no_nodes(self):
        assert unpack_nodes(None) == []

    def test_unpack_one_nodes(self):
        root = ListNode(1)
        assert unpack_nodes(root) == [1]

    def test_unpack_odd_nodes(self):
        root = ListNode(1)
        root.next = ListNode(2)
        root.next.next = ListNode(3)
        assert unpack_nodes(root) == [1, 2, 3]

    def test_unpack_even_nodes(self):
        root = ListNode(1)
        root.next = ListNode(None)
        root.next.next = ListNode(3)
        root.next.next.next = ListNode(None)
        assert unpack_nodes(root) == [1, None, 3, None]

    def test_no_nodes(self):
        assert make_nodes([]) is None

    def test_none_nodes(self):
        assert make_nodes(None) is None

    def test_none_first(self):
        root = make_nodes([None])
        assert root.next is None
        assert root.val is None

    def test_odd_list(self):
        root = make_nodes([1, 2, 3])
        assert root.val == 1
        assert root.next.val == 2
        assert root.next.next.val == 3
        assert root.next.next.next is None

    def test_even_list(self):
        root = make_nodes([1, 2, 3, 4])
        assert root.val == 1
        assert root.next.val == 2
        assert root.next.next.val == 3
        assert root.next.next.next.val == 4
        assert root.next.next.next.next is None

    def test_mixed_list(self):
        root = make_nodes([1, None, 'x'])
        assert root.val == 1
        assert root.next.val is None
        assert root.next.next.val == 'x'
        assert root.next.next.next is None

    def test_bfs_no_tree(self):
        assert breadth_first_search(None) == []

    def test_bfs_none_tree(self):
        assert breadth_first_search(BinaryTree(None)) == [[None]]

    def test_bfs_even_tree(self):
        root = make_arbitrary_trees([1, 2, 3, 4])
        assert breadth_first_search(root) == [[1], [2, 3], [4]]

    def test_bfs_odd_tree(self):
        root = make_arbitrary_trees([1, 2, 3])
        assert breadth_first_search(root) == [[1], [2, 3]]

    def test_bfs_one_child_tree(self):
        root = make_arbitrary_trees([1])
        assert breadth_first_search(root) == [[1]]

    def test_bfs_two_child_tree(self):
        root = make_arbitrary_trees([1, 2])
        assert breadth_first_search(root) == [[1], [2]]

    def test_bfs_3_levels(self):
        root = make_arbitrary_trees([1, 2, 3, 4, 5, 6, 7])
        expected = [[1], [2, 3], [4, 5, 6, 7]]
        assert breadth_first_search(root) == expected

    def test_no_tree(self):
        test_tree = make_arbitrary_trees([])
        assert test_tree is None

    def test_none_tree(self):
        test_tree = make_arbitrary_trees(None)
        assert test_tree is None

    def test_no_children_tree(self):
        root = BinaryTree(1)
        test_tree = make_arbitrary_trees([1])
        assert test_tree.val == root.val
        assert test_tree.left is None
        assert test_tree.right is None

    def test_odd_tree(self):
        parent = BinaryTree(val=1)
        lchild = BinaryTree(val=2)
        rchild = BinaryTree(val=3)
        parent.left = lchild
        parent.right = rchild

        test_tree = make_arbitrary_trees([1, 2, 3])
        assert test_tree.val == parent.val
        assert test_tree.left.val == parent.left.val
        assert test_tree.right.val == parent.right.val

    def test_even_tree(self):
        parent = BinaryTree(val=1)
        lchild = BinaryTree(val=2)
        rchild = BinaryTree(val=3)

        lchild_rchild = BinaryTree(val=4)
        lchild.left = lchild_rchild

        parent.left = lchild
        parent.right = rchild
        test_tree = make_arbitrary_trees([1, 2, 3, 4])
        assert test_tree.val == parent.val
        assert test_tree.left.val == parent.left.val
        assert test_tree.right.val == parent.right.val
        assert test_tree.left.left.val == lchild_rchild.val

    def test_none_stub(self):
        parent = BinaryTree(val=1)
        rchild = BinaryTree(val=3)
        parent.right = rchild

        rchild_lchild = BinaryTree(4)
        rchild.left = BinaryTree(4)

        test_tree = make_arbitrary_trees([1, None, 3, 4])

        assert test_tree.val == parent.val
        assert test_tree.left is None
        assert test_tree.right.val == parent.right.val
        assert test_tree.right.left.val == rchild_lchild.val
