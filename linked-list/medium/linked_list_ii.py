from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
        1) Find if cycle is exist in the linked list
        2) If cycle is exist,find the length of the cycle (K=cycle length)
        3) define two pointers and move one pointer K nodes from head
        4) finally move both pointers one step ahead till they meet.
            i) since pointer 1,K nodes ahead of the pointer 2
            ii) when they meet each other,still pointer 1 K nodes ahead pointer 2
            iii) since cycle length is K,meeting point is the start of the cycle
    """

    def find_cycle_length(slow):
        length = 0
        current = slow
        while True:
            current = current.next
            length += 1
            if current == slow:
                break
        return length

    def starting_point(cycle_len):
        p1, p2 = head, head
        while cycle_len > 0:
            p1 = p1.next
            cycle_len -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    slow_pointer, fast_pointer = head, head
    cycle_len = 0
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            cycle_len = find_cycle_length(slow_pointer)
            break
    return None if cycle_len == 0 else starting_point(cycle_len)


class Solution:
    pass
