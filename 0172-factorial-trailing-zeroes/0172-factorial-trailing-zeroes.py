'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

0, 1 -> 1
2 -> 2
3 -> 6
4 -> 24
5 -> 120
6 - > 720

2. Design a Solution / Template / Runtime and Space Complexity
Calculate n!, check for leading 0's

num = 1
zeros_count = 0

for i in range(1,n+1):
    num *= i
    
# Num is n!
while n > 0:
    q, r = divmod(n, 10)
    if r == 0:
        zeros_count += 1
    else:
        break

return zeros_counts


3. Write the Code And Pass Test Cases.
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = 1
        zeros_count = 0

        for i in range(1,n+1):
            num *= i
        

        # Num is n!
        while num > 0:
            q, r = divmod(num, 10)
            if r == 0:
                zeros_count += 1
            else:
                break
            num = q
        return zeros_count
        