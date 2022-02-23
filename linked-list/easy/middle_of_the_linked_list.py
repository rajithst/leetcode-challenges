from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: ListNode) -> ListNode:
    count = 0
    current_node = head
    while current_node.next:
        count += 1
        current_node = current_node.next

    mid = (count // 2) + count % 2
    for i in range(mid):
        head = head.next
    return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        We can use the Fast & Slow pointers method such that the fast pointer is
        always twice the nodes ahead of the slow pointer.
        This way, when the fast pointer reaches the end of the LinkedList,
        the slow pointer will be pointing at the middle node.
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow