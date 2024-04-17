'''
Understand the problem

[9,9,9,9,9,9,9]
[9,9,9,9]
[8,9,9,9,0,0,0,1]


[9]
[1]
[0,1]

9 + 1 = 10

[3,1]
[2,4]
[5,5]

13 + 42 = 55


[8,2,5]
[4,2,1]
[2,5,6]

528 + 124 = 652

Design a solution 

- Traverse through the input linked lists
- summing values of nodes if not none
- find remainder using % 
- handling the carry when sum > 10 
- create new node in return list from remainder value
- move curr pointer and list pointers to next node
- handle last node if carry still exists 

    initliaze lists_sum
    set curr = lists_sum
    set carry = 0
    
    while l1 is not None and l2 is not None or carry != 0:
        set v1 and v2 values if not none
        sum v1 + v2 + carry
        get remainder with % 10
        get carry with // 10
        
        create remainder node
        set curr.next to remainder node
        
        move curr and l1 and l2 pointers
    
    return lists_sum.next 
    

l1 = [8,2,5]
l2 = [4,2,1]
     [2,5,6]
     
     528 + 124 = 652
     
[9]
[1]
[0,1]

[1,8]
[0]
[1,8]

n = length of l1
m = length of l2
Runtime: O(max(n,m))
Space: O(max(n,m)+1)
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
        curr = lists_sum
        carry = 0
        
        while l1 is not None or l2 is not None or carry != 0:
            v1 = 0 if l1 is None else l1.val
            v2 = 0 if l2 is None else l2.val
            nodes_sum = v1 + v2 + carry
            
            remainder = nodes_sum % 10
            carry = nodes_sum // 10
            
            curr.next = ListNode(remainder)
            curr = curr.next 
            
            if l1 is not None:
                l1 = l1.next 
            if l2 is not None:
                l2 = l2.next 
        
        return lists_sum.next 