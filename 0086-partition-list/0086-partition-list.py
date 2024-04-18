'''
7:30 Understand the problem

[] -> [], [1]->[1], [1,1,1] -> [1,1,1]

[1,2,3], x = 4
[1,2,3]

[1,2,2,3], x = 3
[1,2,2,3]

[3,4,5], x = 2
[3,4,5]

[1,2,3], x = 3
[1,2,3]



[1,3,1,2], x = 3
[1,1,2,3]

[3,1,2], x = 3
[1,2,3]

[1,5,2,3], x = 4
[1,2,3,5]


22:00 Desgin a solution
[1,5,2,3], x = 4
[1,2,3,5]
before - 123
after - 5->None
1235None


[1,3,1,2], x = 3
[1,1,2,3]

before = 112 
after = 3None
1123None

                     h
[1,4,3,2,5,2,1,5,5,1], x = 3
[1,2,2,1,1,4,3,5,5]
before = 12211
after = 43555None
122143555None

- Traverse through input list, moving each node to the correct split list
- before list contains any value less than x, else put node in after list
- set after.next to None
- link before and after list
- return before_head

    initialize before,before_head, after,after_head to dummy nodes

    while head:
        - if node.val < x
            - put node in before list
        - else
            - put node in after list
            
        increment head pointer
        
    - set after.next to None
    - Link before and after lists
    
    return before_head.next
    
Runtime: O(N)
Space:O(1)

Implement

           h
[1,4,3,2,5,2], x = 3
before = 122
after = 435None
122435None
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
        before = before_head = ListNode(None)        
        after = after_head = ListNode(None)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
        
        after.next = None
        
        # Link lists
        before.next = after_head.next
        
        return before_head.next