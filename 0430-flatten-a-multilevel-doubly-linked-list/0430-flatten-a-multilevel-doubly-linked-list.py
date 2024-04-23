'''
4:45 Understand the problem
The nodes in the list must have all of their child pointers set to null.

[] -> []

[1] -> [1]

1 -> 1,2,3
|
2
|
3
|
4


24:15 Design a solution
Recursive function that takes in prev, curr and resturns tail
Base case when we don't have a curr, return prev
Set pointers
calling recursive function on curr.child
call on curr.next with tail returned from child call 


if not head return none

- intialize dummy node and set next to head
- call recursive function passing in flatten_dfs(dummy, head)
- dummy.next.prev = None

- return dummy.head 

-flatten_dffs(prev, curr)
    if not curr:
        return prev
        
    # set pointers
    curr.prev = prev
    prev.next = curr
    
    # Need to save curr.next in temp
    temp = curr.next
    
    tail = self.flatten_dfs(curr, curr.child)
    curr.child = None
    
    return self.flatten_dfs(tail, curr.next)



d>1<>2<>3<>7<>8<>11<>12<>9<>10<>4<>5<>6
prev = 3,7,8
curr = 7,8,11

Runtime: O(N)
Space: O(N)

Implement
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
        def flatten_dfs(prev, curr):
            if not curr:
                return prev 

            # Set pointers 
            prev.next = curr
            curr.prev = prev

            temp = curr.next
            tail = flatten_dfs(curr, curr.child)
            curr.child = None

            return flatten_dfs(tail, temp)

        if not head:
            return None

        dummy = Node('Dummy', None, head, None)

        flatten_dfs(dummy, head)

        dummy.next.prev = None

        return dummy.next

        
       