'''
3:40 Understand the problem
[1] -> [1]

1,2 -> 1,2

1,2,3 -> 1,3,2

1,2,3,4,5,6 -> 1,6,2,5,3,4

1,2,3,4,5,6,7 -> 1,7,2,6,3,5,4

Design a solution
- Find the middle node
- Reverse from middle to end
- Merge lists

initialize fast, slow to head
- while fast and fast.next 
    - fast + 2
    - slow + 1
    
set prev None
cur = slow

- while cur
    - next = cur.next
    - cur.next = prev
    - prev = cur
    - cur = next

# Merge Lists
head, tail = head, prev
- while tail.next 
    - tmp_head = head.next
    - head.next = tail
    - head = tmp_head
    
    - tmp_tail = tail.next
    - tail.next = tmp_head
    - tail = tmp_tail
     
   
    

[1,2,3,4,5]
s=1,2,3
f=1,3,5

None<-3<-4<-5
p=None
c=3

[1,2,3,4,5]
1->5->2
h=1,2
tmp_head=2
t=5,
tmp_tail=4


1,2,3 -> 1,3,2
s=1,2
f=1,3

1->2    None<-2<-3

1->3->2
h=1
t_h = 2
t = 3,2
t_t = 2

1,2 -> 1,2
s=1,2
f=1,None


1,2->None
prev = None,2
cur = 2, None


1,2
1->2
h=1
h_n = 2

t=2
t_n = None
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev, cur = None, slow
        
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        tail = prev 
        
        
        while tail.next:
            tmp_head = head.next
            head.next = tail
            head = tmp_head
            
            tmp_tail = tail.next
            tail.next = tmp_head
            tail = tmp_tail