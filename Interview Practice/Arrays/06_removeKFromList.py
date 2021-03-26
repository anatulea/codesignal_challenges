'''Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    curr = l
    while curr is not None:
        if curr.value != k:
            break
        curr = curr.next
    # first move and set the head
    new_head = curr
    print(curr.value)
    prev = None
    # move along
    while curr is not None:
        if curr.value == k:
            if prev is not None:
                prev.next = curr.next
            curr = curr.next
            continue
        prev = curr
        curr = curr.next
    return new_head