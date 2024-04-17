'''
Understand the problem

[9,9,9,9,9,9,9]
[9,9,9,9]
[8,9,9,9,0,0,0,1]

[1,0,4,1]
[2,3]


[1]
[9]
[0,1]

[8]
[1]
[9]

[7]
[5]
[3,1]

13 % 10 = 3
13 % 10 = 1

Design a solution 
- Traverse through each node in the two lists while pointers aren't none 
- summing node values tracking if there is a carry value
- creating new node from sum
- adding carry value to next iteration 

    
    initialize head node for lists_sum list
    set carry = 0 
    set curr pointer to head of lists_sum 
    
    while l1 or l2:
        
        check l1 and l2 values, if values set as val1 and val2
        compute sum as val1 + val2 + carry 

            
        sum % 10 for node remainder
        sum // 10 for carry 
        
        create new node from remainder 
        set curr.next to remainder node    
        set curr to curr.next in lists_sum
        
        check if l1, then move pointer
        check if l2, then move pointer
        
        



l1= [1,0,4,1]
l2= [2,3]
    [3,3,4,1]

l1 = [8,1,4]
l2 = [3,2]
     [1,4,4]
     
     418 + 23 = 441
     
28:00 Test and code 

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        lists_sum = ListNode(None)
        carry = 0
        curr = lists_sum
        
        while l1 or l2:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            
            nodes_sum = val1 + val2 + carry
            remainder = nodes_sum % 10
            carry = nodes_sum // 10
            
            # Create new node and link
            new_node = ListNode(remainder)
            curr.next = new_node 
            curr = curr.next 
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next 
            
            if carry != 0:
                curr.next = ListNode(carry)
                
            
        return lists_sum.next 