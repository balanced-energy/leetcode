
'''
1. Make Sure You Understand the Problem
  0               1
  1            2     3
  2         4   5   6  
  3       8  9

2. Design a Solution / Runtime and Space Complexity
Have a levels outout list
next_level queue with our root in it 

while there is a root and next_level. Set cur_level = next_level. Reset next level as new queue
append a new list to levels.

Want to add each node in cur_levels to levels output list. Then add each of their children to our next_level queue

return reverse levels list

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
next level initialized with root node
levels output list

while root and next_level:
    cur_level = next_level
    reset next level
    append new list to output levels list

    # Append node to last list in output list
    for node in cur_levels
        levels[-1].append(node)

    if left child add to next level
    if right child add to next level


return reversed levels list
4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Level order
        next_level = deque()
        next_level.append(root)
        
        answer = []

        while root and next_level:
            cur_level = next_level
            next_level = deque()
            answer.append([]) 
            
            # Add each node in current level
            for node in cur_level:
                answer[-1].append(node.val)
            
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
        answer.reverse()
        return answer
        