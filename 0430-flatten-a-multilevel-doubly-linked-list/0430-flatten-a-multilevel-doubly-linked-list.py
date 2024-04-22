'''
6:30 Understand the problem
The nodes in the list must have all of their child pointers set to null.

[] -> []

[1] -> [1]

1 -> [1,3]
| 
3


1,2 -> [1,3,5,6,4,2]
|
3,4
|
5
|
6

stack []
d[1,3,2]
prev = d,1,3
curr= 1,3,2


s[]
d[1<>2<>3<>7<>8<>11<>12<>9<>10<>4<>5<>6]

curr=1,2,3,7,8,11,12,9,10,4,5,6
prev=d,1,2,3,7,8,11,12,9,10,4,5,6



Design a solution
DFS

Use a stack, pushing first node on stack

if not head 
    return None
    
prev = dummy node

while stack 
    - point curr.prev to prev
    - set prev.next to curr
    
    - if curr.next
        append cur.next to stack
    
    - if curr has child
        append child to stack
        curr.child = None
         
    prev = curr
    
return dummy.next 


Runtime: O(N)
Space: O(N)

32:00 Implement 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        stack = []
        stack.append(head)
        
        dummy = Node('dummy', None, None, None)
        prev = dummy
        
        
        while stack:
            curr = stack.pop()
            
            curr.prev = prev
            prev.next = curr
            
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
                curr.child = None
                
            prev = curr
        
        dummy.next.prev = None
        
        return dummy.next 