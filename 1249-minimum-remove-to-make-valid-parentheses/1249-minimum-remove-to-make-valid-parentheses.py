'''
8:30 Understand the problem

'())' -> '()'
[]
(2)
Any closed ')' BEFORE an open '(' is automatically invalid

'a)' -> 'a'

Open doesn't have a matched close AFTER it
'(a' -> 'a'

')(' -> ''

'()s' -> '()s'

'(())('

'((((('

''

Design a solution
Utilize a stack to track open parenthesis needing to be closed


delete = set()

for idx, ch in enumerate(s):
    if ch == '(':
        stack.append(idx)
    
    elif ch == ')':
        if stack:
            stack.pop()
        else:
           delete.add(idx)
           

# Add invalid indices to delete set 
if stack:
    while stack:
        delete.add(stack.pop())


# Rebuild string without indices in delete set
string = []

for idx, ch in enumerate(s):
    if idx not in delete:
        string.append(ch)
        
# List with chars for result string
return ''.join(string)




        
 s = "lee(t(c)o)de)"
 [l,e,e,(,t,(c,),o),d,e]
 lee(t(c)o)de
 (12)
 
 Runtime: O(N)
 Space: O(N)

'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        deletes = set()
        
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)

            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    deletes.add(idx)
                    
        # Add unmatched open parenthesis to deletes list
        if stack:
            while stack:
                deletes.add(stack.pop())
                
        string_list = []
        
        for idx, ch in enumerate(s):
            if idx not in deletes:
                string_list.append(ch)
        
        return ''.join(string_list)
                    