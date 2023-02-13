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

# Checks sum >= 10, sets carry flag, sets new node with sum value to cur_node.next 
check_carry(num_sum, prev_carry, cur_node):
    carry = False
    
    if prev_carry:
        num_sum = num_sum + 1
    
    if num_sum >= 10
        carry = True
        rem = num_sum % 10
        create new node with value rem append to output list 
        cur_node.next = new_node
    
    else:
        create new node with value num_sum
        cur_node.next = new_node
    
    return carry, new_node

#Initialize a new linked list 
l3 = None
cur_l3 = None
carry = False


# Traverse lists
while num_1 and num_2:
    
    num_sum = num_1.val + num_2.val
    carry, new_node = check_carry(num_sum, carry, cur_l3)
    
    if l3 is None:
        l3 = new_node
    cur_l3 = new_node

    num_1 = num_1.next
    num_2 = num_2.next

# One list longer, check which and handle remaining numbers
while num_1:
    check_carry(num_1.val, carry, cur_l3)
    num_1 = num_1.next 

while num_2:
    check_carry(num_2.val, carry, cur_l3)
    num_2 = num_2.next

return l3
4. Write the Code And Pass Test Cases.
'''
# Checks sum >= 10, sets carry flag, sets new node with sum value to cur_node.next 
def check_carry(num_sum, prev_carry, cur_node):
    carry = False
    
    if prev_carry:
        num_sum = num_sum + 1
    
    if num_sum >= 10:
        carry = True
        rem = num_sum % 10
        new_node = ListNode(rem)
        # Check if node exists 
        if cur_node:
            cur_node.next = new_node
        else: 
            cur_node = new_node
    
    else:
        new_node = ListNode(num_sum)
        # Check if node exists 
        if cur_node:
            cur_node.next = new_node
        else: 
            cur_node = new_node

    
    return carry, new_node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Initialize a new linked list 
        l3 = None
        cur_l3 = None
        carry = False

        # Traverse lists
        while l1 and l2:
            
            num_sum = l1.val + l2.val
            carry, new_node = check_carry(num_sum, carry, cur_l3)
            
            # Get pointer to head of output list
            if l3 is None:
                l3 = new_node
        
            cur_l3 = new_node

            # Move to next Nodes in Linked List
            l1 = l1.next
            l2 = l2.next

        # One list longer, check which and handle remaining numbers
        while l1:
            carry, new_node = check_carry(l1.val, carry, cur_l3)
           
            cur_l3 = new_node
            l1 = l1.next 

        while l2:
            carry, new_node = check_carry(l2.val, carry, cur_l3)
          
            cur_l3 = new_node
            l2 = l2.next

        # if none check for carry value append appropriate node value
        if carry:
            cur_l3.next = ListNode(1)
        return l3
            