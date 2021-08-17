from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    #if head is not defined return
    if not head:
        return head

    #keep one pointer at the head of the linked-list for keep track of the begining of the linked-list
    head_node = head

    #while head and next node is available
    while head and head.next:
        #check if current_value and next node's value is equal
        if head.val == head.next.val:
            #if equal close the connection to next node and point to next of the next node
            #don't move the pointer to the next node,because newly created connections value could be same as current value
            #eg [1,1,1]
            head.next = head.next.next
        else:
            #if current node value is not equal to the next node value,we can say there is no duplicate (because of sorted list)
            #move the pointer to next node
            head = head.next
    return head_node
