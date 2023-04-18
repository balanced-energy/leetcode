'''
Mock - 45m
Workflow Timestamps
1. 2:00 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity

# Two pointer
['l',"leet","code"]

if current subtstring from start to end is in dictionary
    list of potential split indices for start and end pointers
     [(0,0),(0,3)]
 
        e
 s
 leetcode
 
 # Recursion
 if we found substring in dict, then return rest of string

["leet","code"]
word_break(s, dict)

i = 1
       i      
s = leetcode

if len(s) == 0:
    return True

for i in range(1, len(s)-1):
    if s[:i] in dict:
        if word_break(s[i:]):
            return True
return False

["cats","og","and","cat"]
"catsandog"
 
3. Write the Code And Pass Test Cases.
'''

def word_break(s, word_dict, memo):
    if len(s) == 0:
        return True
    
    if s in memo:
        return memo[s]
    
    for word in word_dict:
        if s[:len(word)] == word and word_break(s[len(word):], word_dict, memo):
            memo[s] = True
            return True
    
    memo[s] = False
            
    return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return word_break(s, wordDict, memo)
        