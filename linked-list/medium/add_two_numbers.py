class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    result = NodeList()
    current_node = result
    carry = 0
    while l1 or l2 or carry:
        value_1 = l1.val if l1 else 0
        value_2 = l2.val if l2 else 0

        val = value_1 + value_2 + carry
        carry = val//10
        val = val % 10
        current_node.next = NodeList(val)
        current_node = current_node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next