from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    if not head:
        return head

    main_head = head
    previous_node = None
    while head:
        next_node = head.next
        if head.val == val:
            if not previous_node:
                main_head = next_node
            else:
                previous_node.next = next_node
        else:
            previous_node = head
        head = next_node
    return main_head
