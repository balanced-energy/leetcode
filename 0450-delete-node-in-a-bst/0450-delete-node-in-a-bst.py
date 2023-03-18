'''
Workflow Timestamps
1. 0:00 - 3:00 Make Sure You Understand the Problem
2. 3:00 - 9:40 Design a Solution / Runtime and Space Complexity
3. 9:40 - 25:50 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
           8
       5      10 
    2    7   9    11
  1    6 
  
2. Design a Solution / Runtime and Space Complexity
- Find node to delete by traversing tree until finding value. 
- Then handle choosing correct child to replace node.
- Find lowest value in right tree and replace with node to delete.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
return _delete_node(root,key)

_delete_node(root, val)
    if root is None:
        None
        
    if root.val > val:
        root.left = _delete_node(root.left, val)
    
    if root.val < val:
        root.right = _delete_node(root.right, val)
        
    if root.val == val
    # At node to delete
    # No children
        return None
    # One child
        return which child exists
    # Two children
        find lowest value in tree
        set deletion nodes children to be children of lowest node 
        return lowest node 
  
  return root

4. Write the Code And Pass Test Cases.

          50
      30     70
       40   60  80
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def _delete_node(root, val):
    if root is None:
        return None
    
    # Move left
    if root.val > val:
        root.left = _delete_node(root.left, val)
        
    # Move right
    if root.val < val:
        root.right = _delete_node(root.right, val)
        
    # If found node to delete
    if root.val == val:
        # No children
        if root.left is None and root.right is None:
            return None
        
        elif root.left and root.right:
            # Two children
            # Get smallest value from right subtree
            smallest = get_smallest(root.right)
            # Delete smallest node
            root.right = _delete_node(root.right, smallest.val)
            # set deletion nodes children to be children of lowest node 
            if root.right != smallest:
                smallest.right = root.right

            smallest.left = root.left
            return smallest
        # One child
        else:
            if root.left:
                return root.left
            else:
                return root.right

    return root
        
def get_smallest(root):
    if root is None:
        return None
    while(root.left):
        root = root.left
    
    return root

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return _delete_node(root, key)
    
    