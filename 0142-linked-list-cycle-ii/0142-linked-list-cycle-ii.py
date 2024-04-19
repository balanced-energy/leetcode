'''
3:30 Understand the problem
Return None if no cycle

[] -> None
[(1,None)] -> None
(val, next index pointer)
[(1,0)] -> (1,0)

[(1,1),(2,None)] -> None
[(1,1),(2,0)] -> (1,1)
[(1,1),(2,2),(3,1)] -> (2,2)


16:00 Design a solution
- Fast and slow pointers initialized to head
- while fast and fast.next incremenet fast by 2 and slow by 1, checking if they're equal then break
- if not fast or not fast.next return None
- reset fast to head and then increment both until equal 
- return slow

  (val, next index)
              Meet(b)
[(1,1),(2,2),(3,1)] -> (2,2)
s = 1,2,3,3,2
f = 1,3,3,1,2
  Meet
[(1,1),(2,0)] -> (1,1)
s = 1,2,1
f = 1,1,1,1

[(1,0)]
s = 1,1
f = 1,1,1 -> (1,0)

[(1,1),(2,None)] -> None

s = 1,2
f = 1,None
           m
[1,2,3,4,5,1] -> 2

s = 1,2,3,4,5,1,2
f = 1,3,5,2,4,1,1,2

Runtime: O(N)
Space: O(1)
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
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
        
        if not fast or not fast.next:
            return None
        
        fast = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow