'''
3:00 Understand the problem

d[1], n = 1
[]

  s   f
d[1,2], n = 1
[1]

s       f
d[1,2,3], n = 3
d[2,3]
   s     f
 d[1,2,3], n = 2
[1,3]

Design a Solution
- Init a dummy node and point it to head
- Use two pointers fast and slow set to dummy

- Move fast n + 1 position ahead of slow
- Move both at same speed until fast is None (while fast:)
- At this point slow will point to the node prev to the node we want to delete
- set slow.next = slow.next.next 
- return dummy.next 

Runtime: O(N)
Space: O(1)
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
        dummy = ListNode('Dummy', head)
        fast, slow = dummy, dummy
        
        for _ in range(n + 1):
            fast = fast.next
            
        while fast:
            fast = fast.next 
            slow = slow.next
            
        # Slow is one node before the node to delete
        slow.next = slow.next.next 
        
        return dummy.next 
    