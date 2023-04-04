'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
'''
1 -> 9 base cases

22612 -> 6
2,2,6,1,2
2,2,6,12
22,6,1,2
22,6,12
2,26,1,2
2,26,12

    2 2 6 1 2 
dp [1,2,3,3,4]

dp [1,2,3,3,6]

One digit
dp[i] += dp[i-1]

two digit 
dp[i] += dp[i-2] 

    2 2 2 1
dp [1,2,3,0]
2,2,2,1
2,2,21
2,22,1
22,2,1
22,21


22612 -> 6
22 61 2
2,2 or 22 = 1+1
2,6 or 26 = 1+1
6,1 = 1
1,2 or 12 = 1+1



c = 1

4055

1. Make Sure You Understand the Problem

2. Design a Solution / Template / Runtime and Space Complexity
if first digit is zero return 0

one_back and two_back variables to hold decoding amounts 

for i in range(1, len(s)):
    current = 0
    if s[i] != 0:
        current = one_back

3. Write the Code And Pass Test Cases.
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        
        one_back = 1
        two_back = 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = one_back
                
            two_digit = int(s[i-1:i+1])
            
            if 10 <= two_digit <= 26:
                current += two_back 
                
            # Update pointers
            two_back = one_back
            one_back = current
            
        return one_back
            