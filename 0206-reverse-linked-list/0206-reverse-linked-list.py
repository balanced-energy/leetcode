# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Workflow Timestamps
1. 0:00 - 3:03 Make Sure You Understand the Problem
2. 3:15 - 16:38 Design a Solution
3. 16:45 - 22:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 16:45 - 26:00 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

test 3:
head = [1] -> [1]

Example 1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

prev = 1 , prev.next = None
            
cur = 2,   cur.next = prev
           prev = cur
next = 3   cur = next
           next = next.next

1 -> 2 -> 3 -> 4 -> 5 -> None

Iterations
1st - None <- 1 <- 2  3 - > 4 -> 5

prev = 2
cur = 3 , cur.next = prev
next = 4

prev = cur 
cur = next
next = next.next

2n2 - None <- 1 <- 2 <- 3 <- 4 <- 5
2. Design a Solution
Start with three pointers prev, cur, next. While traversing the list set cur.next to prev. Handle first iteration setting prev to None, and traverse until cur is None.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Check for empty list
    if empty list:
        return 
    
    prev = head 
    cur = head.next 
    next = head.next.next
    
    # set reversed head.next to None
    prev.next = None
    
    while cur:
        cur.next = prev
        prev = cur
        cur = next 
        if next:
            next = next.next
        
1 -> 2 -> 3 -> 4 -> 5 -> None

prev = 1, 2, 3, 4, 5
cur = 2, 3, 4, 5, None
next = 3, 4, 5, None

    return prev

None <- 1 <- 2 <- 3 <- 4 <- 5  None
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check for empty list 
        if not head:
            return
        
        prev = head
        cur = head.next
        if head.next:
            next = head.next.next
        else:
            next = None
        
        # Set reversed head to None
        prev.next = None
        
        # Traverse list reversing pointers along list
        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next 
                
        return prev
        