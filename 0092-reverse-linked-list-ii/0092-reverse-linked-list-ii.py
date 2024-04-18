'''
4:15 Understand the problem
[5] -> [5]

[1,2,3], l = 1, r = 3
[3,2,1]

[1,2,3] l = 2, r = 3
[1,3,2]

[1,2,3] l = 1, r = 2
[2,1,3]

[1,2,3,4,5] l = 2, r = 4
[1,4,3,2,5]


Design a solution
initialize prev = None and curr = head
First move prev and curr pointer while left > 1 times reducing left and right counts

set start, tail pointers where start = prev and tail = cur

we reverse nodes while right:
    - next = curr.next
    - curr.next = prev
    - prev = curr
    - curr = next
    - reduce right count
    
Relink the reversed sublist
    - if start
        start.next = prev 
    else
        head = prev
    
    tail.next = cur
    
return head 
  
  s t
        p c n
 [1,2,3,4,5] l = 2,1, r = 4,3,2,1
 1-><-2<-3<-4->5->None
 1->4->3->2->5->None
prev = none
cur = 1

s t
    p c n
 [1,2,3] l = 1, r = 2 ->  [2,1,3]
        h
   3<-1<-2
prev = None
cur = 1

  s t
      p c
 [1,2,3] l = 2,1 r = 3,2 [1,3,2]
  1<-2<-3 
  1->3->2->None
prev = None
cur = 1

Runtime: O(N)
Space:(1)

Implement 
  
  s t
        p c n
 [1,2,3,4,5], left = 2,1 right = 4,3,2,1 ->[1,4,3,2,5]
  1<-2<-3<-4
  1->4->3->2->5->None
prev
cur
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        prev = None
        cur = head
        
        # Move pointers to correct start
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1
            
        start = prev
        tail = cur
        
        # Reverses sublist
        while right:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            right -= 1
            
        # Relink
        if start:
            start.next = prev
        else:
            head = prev
            
        tail.next = cur
        
        return head