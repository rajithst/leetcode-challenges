from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = None
    while head:
        current_node = head
        head = head.next
        current_node.next = previous_node
        previous_node = current_node
    return previous_node
