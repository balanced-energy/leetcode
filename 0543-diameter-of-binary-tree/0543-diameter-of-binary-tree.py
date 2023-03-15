'''
Workflow Timestamps
1. 0:00 - 3:55 Make Sure You Understand the Problem
2. 4:00 - 10:18 Design a Solution / Runtime and Space Complexity
3. 10:18 - 29:25 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
         1
      2      3
    4   5
   5      6
 7          7    -> 6 not 5
    
    
[1] -> 0
2. Design a Solution / Runtime and Space Complexity
max_diamter = 0
# Main function
Base case where if node is none or no children return 0

Otherwise we want to add up left and right childs max depths and compare to max_diameter
We need to do this for each child in the tree


3. Write a Template for Code in Logical Blocks. Aka Pseudocode

# Base case 
if root is None or root.left is None and root.right is None:
    return 0
    
# Otherwise calculate maxDepth of left and right and compare to max_diameter
max_root = node_diameter(root)

max_left = self.diameterOfBinaryTree(root.left)
max_right = self.diameterOfBinaryTree(root.right)

return max(max_root, max_left, max_right)

def node_diameter(root):

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

return left_depth + right_depth

# Max depth helper
def max_depth(root)
    if root is None:
        return 0
    
return 1 + max of maxdepth of left and right

4. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def node_diameter(root):

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return left_depth + right_depth

# Max depth helper
def max_depth(root):
    if root is None:
        return 0
    
    return 1 + max(max_depth(root.left), max_depth(root.right))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      
        # Base case 
        if root is None or (root.left is None and root.right is None):
            return 0

        # Otherwise calculate maxDepth of left and right and compare to max_diameter
        root_diameter = node_diameter(root)

        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)
        
        return max(root_diameter, left_diameter, right_diameter)