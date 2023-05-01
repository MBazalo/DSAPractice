class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def add_two_numbers(l1, l2):
    """
    Given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list also stored in reversed order.
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    output = ListNode()
    output.val = (l1.val + l2.val) % 10
    carried = (l1.val + l2.val) // 10
    current = output
    current_1 = l1
    current_2 = l2
    while current_1.next is not None or current_2.next is not None or carried:
        total = 0
        if current_1.next is not None:
            total += current_1.next.val
            current_1 = current_1.next
        if current_2.next is not None:
            total += current_2.next.val
            current_2 = current_2.next
        total += carried
        carried = total // 10
        current.next = ListNode(total % 10)
        current = current.next
    return output
