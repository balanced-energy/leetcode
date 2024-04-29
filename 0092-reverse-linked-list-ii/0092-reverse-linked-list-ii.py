'''
Understand the problem

 cn t
 p  c
   [1], left = 1, right = 1 -> [1]

cn t
     p c
  [1,2,3], left = 1, right = 2 -> [2,1,3]
 None<1<2  3>None
 h=2>1>3>None
 h = 2
    l r 
 cn t 
      p c
 [1,2,3], left = 2, right = 3 -> [1,3,2]
 head=1> <2<3
 head=1>3>2None
 l=1
 r=2


[1,2,3], left = 1, right = 3 -> [3,2,1]

       lr
    cn t
       p c 
  [1,2,3], left = 3, right = 3 -> [1,2,3]
   1>2>3
   1>2>3>None

con = 2

l = 3,2,1
r = 3,2,1

     l   r
  cn t
         p c
  [1,2,3,4,5], left = 2, right = 4 -> [1,4,3,2,5]
  1><2<3<4 5>None

27:00 Design a solution
- We need to reverse the sublist from left to right
- We need to get pointers into position, by decrementing left and right values until left == 1 
- Perform reversal steps right # of times
- Relink nodes
    -   if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
return head

Runtime: O(N)
Space: O(1)

Implement
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        prev = None
        
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1
            
        # Establish connect node pointer and tail pointer
        con = prev
        tail = cur
        
        # Reverse right # of time
        while right:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            right -= 1
            
        if con:
            con.next = prev
        else:
            head = prev
            
        tail.next = cur
        
        return head 