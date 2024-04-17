'''
3:00 Understand the problem

[1,2,3], n = 1
[1,2]

[1,2,3], n = 3
[2,3]

[1,2,3], n = 2
[1,3]

[1], n = 1
[]

fast = dummy, None
slow = dummy, 

17:45 Design a solution 

- initialize dummy node and set dummy.next to head 
- Traverse input list
- Two pointers, fast and slow where fast is n + 1 ahead of slow
- When fast is None set slow.next = slow.next.next 

    initialize pointers to a dummy node
    set dummy.next as head
    move fast pointer n + 1 nodes ahead 
    
    while fast:
        increment fast and slow pointers
    
    # Remove node
    if slow.next:
        slow.next = slow.next.next 
    else:
    return []
    
    return dummy.next 

[1,2,3], n = 1
fast=dummy,2,3,None
slow=dummy,1,2
[1,2]

[1,2,3], n = 3
fast = dummy,None
slow = dummy,
[2,3]

[1], n = 1
fast = dummy, None
slow = dummy, 
[]

d[1,2,3], n = 2
fast = dummy,3,None 
slow = dummy,1 
[1,3]
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = ListNode(None)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        # Move fast pointer n + 1 nodes 
        for _ in range(0, n + 1):
            fast = fast.next 
        
        while fast:
            fast = fast.next 
            slow = slow.next    
        
        # Remove node 
        if slow.next:
            slow.next = slow.next.next
        else:
            return []
    
        return dummy.next