class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# using the slow pointer and fast pointer method
def has_cycle(head: ListNode) -> bool:
    # make slow and fast pointer to head node
    slow_pointer, fast_pointer = head, head

    # if fast pointer and fast pointer next is not null (if it is null there is a end)
    while fast_pointer and fast_pointer.next:

        # move slow pointer by one
        slow_pointer = slow_pointer.next

        # move fast pointer by two
        fast_pointer = fast_pointer.next.next

        # if there is a cycle eventually fast pointer will meet the slow pointer inside the cycle
        if slow_pointer == fast_pointer:
            return True
    return False
