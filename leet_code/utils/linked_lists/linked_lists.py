import unittest
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def unpack_nodes(head: ListNode):
    current_node = head
    data = []
    while current_node:
        data.append(current_node.val)
        current_node = current_node.next
    return data

def setup_nodes(node_values):
    head = None
    prev_node = None
    for node_val in node_values:
        if not head:
            head = ListNode(node_val)
            prev_node = head
            continue
        current_node = ListNode(node_val)
        prev_node.next = current_node
        prev_node = current_node
    return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.node_func = setup_nodes
        self.unpack_nodes = unpack_nodes

    def test_test_setup_nodes(self):
        node_values = [1, 2, 3, 4]
        current_node = self.node_func(node_values)
        test_vals = self.unpack_nodes(current_node)
        self.assertListEqual(node_values, test_vals)

if __name__ == "__main__":
    unittest.main()