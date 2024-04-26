'''
4:20 Understand the problem
[], x=? 
[]

b
d>None

a
d>None

[1,2,3], x = 5
[1,2,3]

                  b
before_head=d>1>2>3>None
           a
after_head=d>None


[1,2,3], x = -1
[1,2,3]
              b
before_head = d>1>2>3>None
after_head = d>1>2>3>None

[1,4,3,2,5,2], x = 3
[1,2,2,4,3,5]

[2,1,1,1,1], x = 2
[1,1,1,1,2]

Design a solution
- Create two separate lists both with dummy head nodes before_head and after_head
- Use before, and after pointers to traverse each list setting them equal to the heads to start
- Traverse input list and move node to appropriate list whether it's strictly less than x or not
- after.next = None
- link the two lists by setting before.next = after_head.next 
- return before_head.next 
              b
before -d>1>2>2
              a
after - d>4>3>5>None

Runtime: O(N)
Space: O(1)

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before_head = ListNode('before', None)
        after_head = ListNode('after', None)
        
        before = before_head
        after = after_head
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
                
            else:
                after.next = head
                after = after.next 
            
            head = head.next 
            
        after.next = None
        
        # Link the lists
        before.next = after_head.next 
        
        return before_head.next 