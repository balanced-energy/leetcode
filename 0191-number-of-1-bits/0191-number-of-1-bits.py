'''
Mock - 45m
Workflow Timestamps
1. 1:15 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
n is an int

bits = str(n)

Don't use str(), //, or %. 

n is binary number 

n 01
  00


    

2. Design a Solution / Template / Runtime and Space Complexity
Traverse through each bit in n, increment ones_count counter if bit is a one.
return ones_count


3. Write the Code And Pass Test Cases.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        ones_count = 0
        while n:
            if n & 1:
                ones_count += 1
            n >>= 1
        
        return ones_count
        