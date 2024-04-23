'''
6:45 Understand the problem

'()s' -> '()s'

'' -> ''

'(as' -> 'as'

'())' -> '()'

'()sd(dss)(' -> '()sd(dss)'

'(((((' -> ''

16:00 Design a solution
stack to track open
set to store indices to delete from final string

loop through s matching opens with closes and identifying any invalild chars

for idx, ch in enumerate(s):
    if ch == '(':
        stack.append(idx)
    
    elif not stack:
        deletes.add(idx)
    
    else:
        stack.pop()

# Add any remaining opens to deletes set
deletes.union(set(stack))

# Rebuild result string
string_list = []

for idx, ch in enumerate(s):
    if idx not in deletes:
        string_list.append(ch)
        
return ''.join(string_list)


Runtime: O(N)
Space: O(N)


Implement
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        deletes = set()
        
        for idx, ch in enumerate(s):
            
            if ch.isalpha():
                continue 
                
            if ch == '(':
                stack.append(idx)
                
            elif not stack:
                deletes.add(idx)
                
            else:
                stack.pop()
                
        deletes = deletes.union(set(stack))
        
        # Rebuild string
        list_string = []
        
        for idx, ch in enumerate(s):
            if idx not in deletes:
                list_string.append(ch)
                
        return ''.join(list_string)