'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem


        1
      2    3
         4   5


Serialize:
ser_arr = [1,2,None,None,3,4,None,None,5,None,None]

2. Design a Solution / Template / Runtime and Space Complexity
Pre-order traversal creating string output
Process string creating new tree structure
3. Write the Code And Pass Test Cases.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'
        return ','.join([str(root.val),self.serialize(root.left), self.serialize(root.right)])


        

    def deserialize(self, data):
        q = deque(data.split(','))
        root = self.deserialize_helper(q)
        return root
        
    def deserialize_helper(self, queue):
        val = queue.popleft()
        if val == '#':
            return None
        node = TreeNode(int(val)) 
        node.left = self.deserialize_helper(queue)
        node.right = self.deserialize_helper(queue)
        return node
       
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))