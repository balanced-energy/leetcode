'''
1. Make Sure You Understand the Problem
temps = [70] -> 0

potential max outputs =         [4,3,2,1,0]
temps = [70, 30, 40, 50, 80] -> [4,1,1,1,0]


2. Design a Solution / Runtime and Space Complexity
Use a stack that keeps track of daily temperatures indices in decreasing order of their temperatures

Looping through the days, if there are elements on the stack compare them to the current day's temperature.
if the current temp < top of the stack temp, add it to the stack as new lowest temp
if the current temp > top of the stack temp 
    pop from stack
    set answer[popped day index] = current day - popped day index

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize answer array and stack
answer = []
# Stores (day index, temperature) on stack
stack = []

for i, temp in temperatures:
  if there are elements on stack
    if current temp <= top of stack temp
        append current temp to stack
    else
        while stack remove temps from stack until finding one greater than current temp
        then calculate days difference and set as answer[i] 
 
 return answers
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for day, temp in enumerate(temperatures):  
            # While current is greater than top, pop top temp off
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append(day)
        
        return answer