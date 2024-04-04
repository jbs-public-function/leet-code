from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def make_nodes(node_vals: List[Optional[int]]) -> Optional[ListNode]:
    current_node = None
    while node_vals:
        node = ListNode(node_vals.pop())
        if current_node is None:
            current_node = node
            continue
        node.next = current_node
        current_node = node
    return current_node


def unpack_nodes(root: Optional[ListNode]) -> List[Optional[int]]:
    if not root:
        return []
    nodes_data = []
    while root:
        nodes_data.append(root.val)
        root = root.next
    return nodes_data
