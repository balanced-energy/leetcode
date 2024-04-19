'''
8:50 Understand the problem

[] -> -1
[(1,None)] -> -1
[(1,0)] -> (1,0)

(val, next idx)
[(1,1),(2,0)] -> (1,1)

[(1,1),(2,2),(3,1)] -> (2,2)


Design a solution

Two pointer approach
fast and slow pointers, fast increments by two slow by one
when fast == slow we detect a cycle

while fast and fast != slow

               pos
               s      f
[(3,1),(2,2),(0,3),(-4,1)]

         pos
   fs
[(1,1),(2,0)]

(next pointer)
       hit
f       s                 
1,2,3,4,5,1
s=4,5,0,1
f=0,2,4,1
s=4,5,0,1,2
f=5,1,3,5,2


Second idea not optimal space
store nodes seen in map
while head, traverse linked list
if head in seen return head

return -1

{3,2,0,-4}
[3,2,0,-4]

Runtime: O(N)
Space: O(N)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        
        return None