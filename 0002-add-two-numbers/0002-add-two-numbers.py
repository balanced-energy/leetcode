# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Workflow Timestamps
1. 0:00 - 7:05 Make Sure You Understand the Problem
2. 7:05 - 14:30 Design a Solution
3. 14:30 - 38:30 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 38:30 - 49:41 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
output = [8,9,9,9,0,0,0,1]
Input: l1 = [9,9,9,9,9,9,9], 
l2 =              [9,9,9,9]
out = 9 + 9 = 18 % 10, carry 1, = [8]
9 + 9 + carry = 19 carry 1 = [8, 9]
9 + 9 + carry = 19 carry 1 = [8, 9, 9]
9 + 9 + carry = 19 carry 1 = [8, 9, 9, 9]
9 + carry (1) = 10 carry 1 = [8, 9, 9, 9, 0]
9 + carry (1) = 10 carry 1 = [8, 9, 9, 9, 0, 0]
9 + carry (1) = 10 carry 1 = [8, 9, 9, 9, 0, 0, 0]
carry (1) = 1 =              [8, 9, 9, 9, 0, 0, 0, 1]


test cases:
1.)
l1 = [9], l2 = [1] -> [0, 1]

2.) 
l1 = [1, 1] =, l2 = [9] -> [0, 2]


2. Design a Solution
Traverse lists. Check if both nodes exist, if only one, if none check for carry value append appropriate node value
summing values through traversal, checking sum >= 10. Handle carry value, create new node append to output list

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Initialize a new linked list 
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            val_sum = l1Val + l2Val + carry
            carry = val_sum // 10
            newNode = ListNode(val_sum % 10)
            cur.next = newNode
            cur = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
            