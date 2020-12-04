'''
Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
'''
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

class LinkedList: 
    def __init__(self): 
        self.head = None
  
    # Method to display the list 
    def printList(self): 
        temp = self.head 
        while temp: 
            print(temp.value, end=" ") 
            temp = temp.next
  
    # Method to add element to list 
    def addToList(self, newData): 
        newNode = ListNode(newData) 
        if self.head is None: 
            self.head = newNode 
            return
  
        last = self.head 
        while last.next: 
            last = last.next
  
        last.next = newNode 
  


# Function to merge the lists 
# Takes two lists which are sorted 
# joins them to get a single sorted list 
def mergeTwoLinkedLists(l1, l2):
    dummyNode = ListNode(0) # A dummy node to store the result 
    tail = dummyNode # Tail stores the last node
    while True:
        # If any of the list gets completely empty 
        # directly join all the elements of the other list 
        if l1 is None:
            tail.next=l2
            break

        if l2 is None:
            tail.next= l1
            break

        # Compare the value of the lists and whichever is smaller is 
        # appended to the last of the merged list and the head is changed 
        if l1.value <= l2.value:
            tail.next =  l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        # Advance the tail 
        tail =  tail.next
    # Returns the head of the merged list 
    return dummyNode.next
    
''' RECURSIVE WAY
def mergeTwoLinkedLists(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.value<=l2.value:
        temp= l1
        temp.next =  mergeTwoLinkedLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeTwoLinkedLists(l1, l2.next)
    return temp
'''

# Create 2 lists
l1=LinkedList()
l2=LinkedList()

# Add elements to the list in sorted order 
l1.addToList(1)
l1.addToList(4)
l1.addToList(9)

l2.addToList(3)
l2.addToList(5)
l2.addToList(6)

# Call the merge function
l1.head = mergeTwoLinkedLists(l1.head, l2.head) 
  
# Display merged list 
print("Merged Linked List is:") 
l1.printList() 