# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
Workflow Timestamps
1. 0:00 - 3:27 Make Sure You Understand the Problem
2. 3:27 - 8:10 Design a Solution
3. 8:30 - 12:25 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 12:25 - 16:45 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
if empty return false

2. Design a Solution
Traverse list with fast and slow pointer. Check if fast.next.next exists. If not return false. 
Fast increments by 2 positions, slow by 1. 
If fast catches slow, there is a cycle, otherwise if fast is none. No cycle

head = [3,2,0,-4] pos = 1, -4 -> 2

fast = 3,0,2,-4
slow = 3,2,0,-4

head = [1], pos = -1

fast = 1
slow = 1

head = [1,2,3,4]

slow = 1, 2, 3
fast = 1, 3, None

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

    fast = head
    slow = head

    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
        
    return Fasle
4. Write the Code And Pass Test Cases.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        fast = head 
        slow = head
        
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next 
            else:   
                return False

            if slow is fast:
                return True
        
        return False
     
        