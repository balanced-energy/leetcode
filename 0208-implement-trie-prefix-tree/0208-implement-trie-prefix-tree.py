'''
Mock-45m
Workflow Timestamps
1. 0:00 - 1:40 Make Sure You Understand the Problem
2. 1:40 - 13: 17 Design a Solution / Runtime and Space Complexity
3. 13:17 - 22:10 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 22:10 - 32:25 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

            Node()
               {a,  b}
               {p}  {a}
                     {t}
               {p}
               {l}
               {e} true
            
2. Design a Solution / Runtime and Space Complexity
class Node to store children map as well as an isEnd boolean to mark the end of words.

# Insert
looping through each character in the word comparing to the childrens map of each node starting 
with the root node. Check if char is in current nodes children, if it is move to that node 
else create a new node and add to children of current node.
At last char mark isEnd as true 

# Search
Loop through each char in word, and if a path exists move to next char, otherwise return false
After looping through all chars return current node isEnd. 

# Prefix
Loop through each char, if path doesn't exist return false. Otherwise go to next char. 
if all chars have a path return true

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

class Node:
    children = {c:Node()}
    isEnd = False
    
# Init Trie
    self.root = Node()
    
# Insert
    node = self.root
    for c in word:
        if c in node.children:
            node = node.children[c]
        else
            node.children[c] = Node()
   
   # Current node is last char
   node.isEnd = True

# Search 
    for c in word:
        if c in node.children:
            node = node.children[c]
        else
            return False
            
    return node.isEnd
    
# Prefix
    for c in word:
            if c in node.children:
                node = node.children[c]
            else
                return False

        return True

            
4. Write the Code And Pass Test Cases.
'''
class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
        
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node()
                node = node.children[c]
            
        # Current node is last char in word
        node.isEnd = True
       
    def search(self, word: str) -> bool:
        node = self.root
       
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        
        return node.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)