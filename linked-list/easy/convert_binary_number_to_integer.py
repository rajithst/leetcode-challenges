class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_decimal_value(head: ListNode) -> int:
    binary_str = head.val
    while head.next:
        current_node = current_node.next
    return int(binary_str, 2)
