class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    top_list = l1
    down_list = l2
    main_list = None

    # check if linked list are empty or not
    if not top_list:
        return down_list
    if not down_list:
        return top_list

    # if linked lists are not empty
    if top_list and down_list:
        # check if top list value is less than down list
        if top_list.val <= down_list.val:
            # if top value is less than down value
            # main linked list starts with top linked list
            main_list = top_list
            # move head to the next of the list (in case we have to break the connection we have to keep track on the linked list)
            top_list = main_list.next

            # check if linked list is over (which means has only one value)
            if not top_list:
                # if has only one value link main list to the down list
                main_list.next = down_list
        else:
            # if top value is bigger than the down value,main list starts with the down list
            main_list = down_list

            # move head to the next of the list (in case we have to break the connection we have to keep track on the linked list)
            down_list = main_list.next

            # if down list is is over(which means has only one node)
            if not down_list:
                # if has only one value link main list to the top list
                main_list.next = top_list

        # keep new head at memory
        new_head = main_list

    # if top list and down list are not finished
    while top_list and down_list:

        # if top_list value is less than the down list value
        if top_list.val <= down_list.val:

            # create the main list next connection to the top list current pointer
            main_list.next = top_list
            # move main list current pointer to the top list current pointer
            main_list = top_list

            # move top list pointer to the next node of the main_list
            top_list = main_list.next
        else:
            main_list.next = down_list
            main_list = down_list
            down_list = main_list.next
        if not top_list:
            main_list.next = down_list
        if not down_list:
            main_list.next = top_list
    return new_head
