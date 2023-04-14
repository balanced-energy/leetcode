'''
Mock - 45m
Workflow Timestamps
1. 1:40 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
19 -> true
1 + 9 = 82
8 + 2 = 68
6 + 8 = 100
1 + 0 + 0 = 1

Potentially false
12 -> False
1^2 + 2^2 = 5
5^2 = 25
2 + 5 = 29
2 + 9 = 85
8 + 5 = 89
8 + 9 = 155
1 + 5 + 5 = 51
5 + 1 = 26
2 + 6 = 40
4 + 0 = 16
1 + 6 = 37 
3 + 7 = 58 
5 + 8 = 

15 % 10
divmod(a,b)
(1, 5) 
We know we will either reach 1 or a previously seen number 

2. Design a Solution / Template / Runtime and Space Complexity
Track seen numbers in seen set. 
Perform operation that squares each digit and calculates total sum
if sum in seen:
    return False
if sum == 1
    return True

# Tracks seen sums
seen = set()
# Get digits
get_sum(n)
    sum = 0
    while n > 0:
        q, r = divmod(n, 10)
        n = q
        sum += r
    return sum 

while True:
    sum = get_sum(n)

    if sum in seen:
        return False
    
    if sum == 1:
        return True
    
    seen.add(sum)


3. Write the Code And Pass Test Cases.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def get_sum(n):
            total_sum = 0
            while n > 0:
                q, r = divmod(n, 10)
                n = q
                total_sum += r**2
            return total_sum 
            
        while True:
            cur_sum = get_sum(n)
            
            # Found cycle
            if cur_sum in seen:
                return False

            # Reached 1
            if cur_sum == 1:
                return True

            seen.add(cur_sum)
            n = cur_sum