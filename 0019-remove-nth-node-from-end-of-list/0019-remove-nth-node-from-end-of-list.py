'''
3:00 Understand the problem
[1,2,3], n = 1
[1,2]

[1,2,3], n = 2
[1,3]

[1,2,3], n = 3
[2,3]

[1], n = 1
[]

11:30 Design a solution 
- initialize dummy node and set pointers to dummy
- link dummy to input list by setting dummy.next 
- Move the fast pointer n + 1 nodes 
- Traverse linked list until the end where fast is None
- remove node by setting slow.next = slow.next.next

d[1,2,3], n = 1
[1,2]
fast = dummy,2,3,None 
slow = dummy,1,2


d[1,2,3], n = 3
[2,3]
fast = dummy, None
slow = dummy 

d[1], n = 1
[]
fast = dummy,None 
slow = dummy


initialize dummy node
    set dummy next to input list head
    set pointers to dummy
    
    move fast pointer n + 1 nodes
    
    while fast
        incremenent fast and slow pointers
    
    set slow.next = slow.next.next
    
    return dummy.next 
    
Runtime: O(N)
Space: O(1)


Implement

d[1], n = 1
d->None
fast = dummy, None
slow = dummy, 

d[1,2,3], n = 1
[1,2]

fast = dummy,2,3,None 
slow = dummy,1,2
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
        
        # Move fast n + 1 nodes
        for _ in range(0, n + 1):
            fast = fast.next 
            
        while fast:
            fast = fast.next 
            slow = slow.next 
            
        # Remove node
        slow.next = slow.next.next
        
        return dummy.next 