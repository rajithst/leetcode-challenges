# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def __lt__(self, other):
    return self.val < other.val


ListNode.__lt__ = __lt__

import heapq as heap


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []
        for l in lists:
            if l:
                heap.heappush(pq, (l.val, l))

        prev = None
        newhead = None
        while pq:
            v, node = heap.heappop(pq)
            if not prev:
                prev = node
                newhead = node
            else:
                prev.next = node
                prev = prev.next

            if node.next:
                heap.heappush(pq, (node.next.val, node.next))
        return newhead
