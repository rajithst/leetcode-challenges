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
