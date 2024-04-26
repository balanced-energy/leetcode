'''
3:40 Understand the problem

d[] -> []

d[1,1,2] -> [2]

  p     h
d[1,2,2] -> [1]

d[1,2,3,3,4,4,5] -> [1,2,5]

p       h
d[1,1,1] -> []

[1,1,2,3,3] -> [2]

19:50 Design a solution

- Init a dummy node, and point to head to help in the case where duplicates sublist is at the head
- prev pointer set to dummy to handle deleting sublist when traversing input list
- While we have a head pointer
    # Identify the start of a duplicates sublist by checking 
    - if head.next and head.val == head.next.val
        # move head pointer to end of that list
        - while head.next and head.val == head.next.val move head pointer
        # head is pointing to end of sublist, delete sublist
        - set prev.next = head.next 
        
    - else if we didn't find start of sublist, increment prev pointer
    - increment head pointer

- return dummy.next 

Runtime: O(N)
Space: O(1)

p   h
d[1,1,2] -> [2]

Implement

    p       h
d[1,1,1,2,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode('Dummy', head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                # Move head pointer to end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next 
                    
                # Delete duplicates sublist
                prev.next = head.next 
                
            else: 
                prev = prev.next 
                
            head = head.next 
            
        return dummy.next 
                    