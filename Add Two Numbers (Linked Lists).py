# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = current = ListNode(0)    #create temp linked list
        x = 0                           #create temp variable

        while l1 or l2 or x:            #while there is a number in l1, l2, or x
            if l1:                      #if l1, then sum the value to x and move to next list element
                x += l1.val
                l1 = l1.next
            if l2:                      #if l2, then sum value to x and move to next list element
                x += l2.val
                l2 = l2.next
            current.next = ListNode(x%10)   #set next element in temp list to the remainder of x % 10
            current = current.next          #advance temp linked list
            x //=10                         #floor divide x by 10
        return temp.next                    #return temp linked list
