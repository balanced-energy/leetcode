'''
Workflow Timestamps
1. 0:00 - 2:15 Make Sure You Understand the Problem
2. 2:15 - 9:25 Design a Solution / Runtime and Space Complexity
3. 9:25 - 13:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 13:00 - 17:08 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
Tests:

s = '({[]})' -> true
s = '[' -> false
s = '[(])' -> false

2. Design a Solution / Runtime and Space Complexity
Create a map of close:open symbols and a stack. Loop through s checking each char. If char is opening symbol append it to the stack.
If char is closing symbol check if char in map then pop from stack and compare popped symbol to map[char]. 
If not equal return false. After looping through s if stack empty return true else False

Runtime = O(N)
Space = O(N)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

symbol_map = {close:open} of each symbol

open_symbols_stack = []
for c in s:
    if c not in symbol_map:
        open_symbols_stack.append(c)
    elif symbol_map[c] != open_symbols_stack.pop():
        return False

# If stack not empty open symbol not matched
if open_symbols_stack:
    return False

return True
4. Write the Code And Pass Test Cases.
'''

class Solution:
    def isValid(self, s: str) -> bool:
      
        symbol_map = {')':'(', ']':'[', '}':'{'}

        open_symbols_stack = []
        for c in s:
            if c not in symbol_map:
                open_symbols_stack.append(c)
            # Need open symbol for current closed symbol
            elif not open_symbols_stack:
                return False
            elif symbol_map[c] != open_symbols_stack.pop():
                return False
            
        # If stack not empty open symbol not matched
        if open_symbols_stack:
            return False

        return True