'''
Workflow Timestamps
1. 0:00 - 1:50 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

k = 0,1,2
i = 0,1,2,3
cur = [1]

[1,2,3,4]

[]
 x    x                   x                          x
[1],[1,2],[1,3],[1,4],[1,2,3],[1,2,4],[1,3,4],[1,2,3,4]
[2],[2,3],[2,4],[2,3,4]
[3],[3,4]
[4]

2. Design a Solution / Runtime and Space Complexity
We call our backtrack function n+1 times. Once for the empty set then every index. 

# Backtrack
backtrack function will first check if the current combination is of length k.
Then loop from a starting index to length of nums end. 
It will add the current i int and then call itself again for i+1 to get next ints and complete the combination.
within the for loop after calling itself it will then "backtrack" and pop off the end element.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

backtrack(first = 0, cur = []):
    check if current combination is of length k
        append to output
        return
        
    loop through range of ints from first to n
        append current int to current combination curr
        
        use next int to complete combination by calling backtrack i + 1
        
        #backtrack
        pop from cur
        

# Setup
out = []

for k in range n_+ 1
    backtrack
    
return out

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, cur = []):
            if len(cur) == k:
                out.append(cur[:])
                return
            
            # Loop through ints
            for i in range(first, n):
                # Add i to combination
                cur.append(nums[i])
                
                # Add next ints
                backtrack(i + 1, cur)
                
                # backtrack 
                cur.pop()
                
        
        # Setup
        out = []
        n = len(nums)
        
        for k in range(n + 1):
            backtrack()
            
        return out
        