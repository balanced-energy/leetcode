'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

[c,a,n]
[o,t,d]
[w,d,f]

s in string

(c:[cat,cow],a:3)
['catcowdog','cow','and']

2. Design a Solution / Template / Runtime and Space Complexity
- Create a trie where each node has a pointer to its parent node
- Perform DFS traversal on the board with backtracking
- When a word is found, attempt to prune trie branches

3. Write the Code And Pass Test Cases.
'''
class TrieNode:
    
    def __init__(self, val: str = None, parent: Optional['TrieNode'] = None):
        self.children = {}
        self.val = val
        self.parent = parent
        self.word = None
        

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(val=c, parent=node)
            node = node.children[c]
        node.word = word
        
    def prune(self, node: TrieNode) -> None:
        # remove current word from possible match later
        node.word = None

        # prune trie until we reach a node with remaining children
        # or the root
        child = node
        parent = child.parent
        while parent and len(child.children) == 0:
            del parent.children[child.val]
            child = parent
            parent = parent.parent
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        # Add answer key of words to trie
        for word in words:
            trie.addWord(word)

        ans = []

        Rows = len(board)
        Cols = len(board[0])
        seen = set()
        
        def dfs(r, c, node) -> None:
                if (r < 0 or r == Rows or c < 0 or c == Cols or
                    (r, c) in seen or board[r][c] not in node.children):
                    return

                # we can use current board position to (maybe) build a word
                seen.add((r, c))
                node = node.children[board[r][c]]

                if node.word:
                    ans.append(node.word)
                    trie.prune(node)

                if len(node.children) == 0:
                    # no more words can be built from here
                    # no need to dfs further, so we backtrack
                    seen.remove((r, c))
                    return

                # check neighbors 
                directions = [(1,0), (0,1), (-1,0), (0,-1)]
                for x,y in directions:
                    dfs(r + x, c + y, node)

                # back track
                seen.remove((r, c))

        for r in range(Rows):
            for c in range(Cols):
                dfs(r, c, trie.root)

        return ans