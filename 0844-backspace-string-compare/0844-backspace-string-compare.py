'''
Workflow Timestamps
1. 0:00 - 3:35 Make Sure You Understand the Problem
2. 3:35 - 8:02 Design a Solution / Runtime and Space Complexity
3. 8:02 - 20:55 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 20:55 - 26:09 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
s = "#" t = "a#" -> true

s = '' t = '' -> true

s = '##'

s = 'ab#c' t = 'ad#c'

s = '' t = 'a#' -> true
s_stack = [a,c]
t_stack = [a,c]
2. Design a Solution / Runtime and Space Complexity
Using two stacks, loop through each string. Check if the current character is equal to #. If there are elements in  stack, pop from it, 
else add char to stack. Loop through both stacks comparing each char. If s[char] not equal t[char] false, else true.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
 
 # Checks for # sign and pops from stack otherwise appends char
 def string_stack(s):
    stack = []
    for c in s:
        if c == '#':
            if stack:
                stack.pop()
        else: 
            stack.append(c)
    return stack

def main(s, t):
   # Initializing stacks

        s_stack = string_stack(s)
        t_stack = string_stack(t)
    
        # Compare stacks 
        if len(s_stack) != len(t_stack):
            return False
        for i in range(len(s_stack)):
            if s_stack[i] != t_stack[i]:
                return False
        
        return True

Runtime = O(N+M)
Space Complexity = O(N+M)
4. Write the Code And Pass Test Cases.
'''
def string_stack(stack, s):
    for c in s:
        if c == '#':
            if stack:
                stack.pop()
        else: 
            stack.append(c)
    return stack
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Initializing stacks
        s_stack = []
        t_stack = []

        s_stack = string_stack(s_stack,s)
        t_stack = string_stack(t_stack,t)
    
        # Compare stacks 
        if len(s_stack) != len(t_stack):
            return False
        for i in range(len(s_stack)):
            if s_stack[i] != t_stack[i]:
                return False
        
        return True
