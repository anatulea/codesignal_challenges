'''Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;

For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(head):
    slow = head
 
    # Declare a stack
    stack = []
     
    ispalin = True
 
    # Push all elements of the list
    # to the stack
    while slow != None:
        stack.append(slow.value)
         
        # Move ahead
        slow = slow.next
 
    # Iterate in the list again and
    # check by popping from the stack
    while head != None:
 
        # Get the top most element
        i = stack.pop()
         
        # Check if data is not
        # same as popped element
        if head.value == i:
            ispalin = True
        else:
            ispalin = False
            break
 
        # Move ahead
        head = head.next
         
    return ispalin

