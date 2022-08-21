from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp_node = ListNode(0, head)
        prev_node = temp_node

        while head:
            # if current node and next node values are equal,continue to move pointer ahead till the values are different
            # keep maintain a previous node which is last pointer with distinct value when we found another
            # distinct value,link with previous distinct node
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                prev_node.next = head.next
            else:
                prev_node = prev_node.next

            head = head.next
        return temp_node.next
