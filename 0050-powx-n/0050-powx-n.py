'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem


Idea 1: Time limit exceeded
  if n == 0:
            return 1
        num = x
        if n < 0:
            num = 1/x
            x = 1/x
            
        for i in range(1,abs(n)):
            num *= x
            
        return num
        
Idea 2:

    
    
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

-2
1/2
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Setup
        if n == 0:
            return 1
        
        # Handle negative case setup
        if n < 0:
            x = 1/x
           
        return x**abs(n)
      
#         for i in range(1,abs(n)):
#             num *= x
            
#         return num