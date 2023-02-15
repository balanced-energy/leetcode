'''
Workflow Timestamps
1. 0:00 - 7:40 Make Sure You Understand the Problem
2. 7:40 - 15:40 Design a Solution / Runtime and Space Complexity
3. 15:40 - 17:35 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

Test Cases:

tokens = [1] -> 1
tokens = [+] 'any expression only token' -> 0


2. Design a Solution / Runtime and Space Complexity
- Initialize a stack. 
- Loop through string checking each char. 
- If char is an int, push to stack, 
- else an operand pop twice from stack and evaluate operation, and push new value on stack.
- return last element from stack

Runtime: O(N)
Space: O(N)

tokens = ["2","1","+","3","*"]

stack = [9]
char = 2,1,+,3,* = 9
return stack[-1]
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Initialize stack
    stack = []
    
    #Loop through string checking each char. 
    for c in tokens:
        check if char or operand 
            if char append to stack
            else evaluate and push new value to stack
    
    return stack[-1]
4. Write the Code And Pass Test Cases.
'''
import math
def perform_operation(char, num_1, num_2):
    
     
    return new_value

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize stack
        stack = []

        #Loop through string checking each char.
        new_value = None
        for c in tokens:
            # Check if int or operand
            if c == '+':
                num_1 = stack.pop()
                num_2 = stack.pop()
                operand = c
                new_value = int(num_2) + int(num_1)
                stack.append(new_value)
               
        
            elif c == '-':
                num_1 = stack.pop()
                num_2 = stack.pop()
                operand = c
                new_value = int(num_2) - int(num_1)
                stack.append(new_value)
             
        
            elif c == '*':
                num_1 = stack.pop()
                num_2 = stack.pop()
                operand = c
                new_value = int(num_2) * int(num_1)
                stack.append(new_value)
             
        
            elif c == '/':
                num_1 = stack.pop()
                num_2 = stack.pop()
                operand = c
                new_value = int(num_2) / int(num_1)
                if new_value < 0:
                    new_val = math.ceil(new_value)
                else:
                    math.floor(new_value)
                stack.append(new_value)
             
        
            else:
                stack.append(c)
            
                
        return int(stack[-1])

            
            
            
            
            
            
            
            
            
            