'''
3:15 Understand the problem 

d[]
d[]
prev = d
head = None
head.next = None 

  p h
d[1]
d[1]
prev = d
head = 1
head.next = None

  p     h
d[1,1,2]
d[2]
prev = d
head = 1,1
head.next = 1,2 

  p   h 
d[1,2,2]
d[1]
prev = d
head = 1,2
head.next = 2,2 

p   h
d[1,1,2,3,3]
  p   h
d[2,3,3]
d[2]
prev = d
head = 1,2,3
head.next = 1,3,3 

[1,1,1,2,3]
[2,3]

[1,2,3,3,3]
[1,2]

p     h
d[1,1,1,2,3,3,3]
p         h
d[2,3,3,3]
p
d[2]
prev = d,
head = 1,1,1,2,3
head.next = 1,1,2,3,3 

Design a solution
- initialize dummy node and point it to head
- Traverse linked list checking head.val and head.next.val
- if values are equal, then move head pointer to end of duplicates sublist 
    - prev.next to head.next
- else
    - increment prev
- increment head


psedocode:
    - initialize dummy set next to head
    - prev = dummy
    
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val 
                - increment head pointer
            
            # Delete sublist
            prev.next = head.next
        else
            prev = prev.next
            
        # increment head
        head = head.next

    return dummy.next 
    

return dummy.next 

Runtime: O(N)
Space: (1)
25:30 Implement code
p     h
d[1,1,1,2,3]
p     h  
d[2,3]
prev = d
head = 1
head.next = 1

p   h  
d[1,1,2,3,3]
  p h
d[2]
prev = d,2
head = 1,2
head.next = 1,3
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(None, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            
                # Delete sublist of duplicates
                prev.next = head.next
            
            else:
                prev = prev.next
            
            # Increament head
            head = head.next 
            
        return dummy.next
    