
'''
1. Make Sure You Understand the Problem
nums = [1] -> check if equal to k 

nums = [0,-1,2,1], k = 0 -> 1

nums = [1,2,1,2,1] k = 3 -> 4

nums = [2,1,3] k = 4

nums = [4,-1,1,1] k = 2

2. Design a Solution / Runtime and Space Complexity
Store a map of seen prefix sums and their count to find values that sum to k. 
If we find a prefix_sum - k that is in our map, then we know we have found a subarray sum equal to k


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
prefix_sum map

# Add 0:1 to map for case when prefixsum == k
prefix_sum add (0,1)
Loop through the array checking
    if prefix_sum - k in map
        add answer to total
    else increment prefix sum count 
    
return answer


4. Write the Code And Pass Test Cases.
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_sum map
        prefix_sums = {}
        # Need to add 0:1 to map for prefix_sum == k case
        prefix_sums[0] = 1

        # Return answer
        total = 0
        
        prefix = 0
        for num in nums:
            prefix += num

            if prefix - k in prefix_sums:
                total += prefix_sums[prefix - k]

            # Update prefix count in map
            prefix_sums[prefix] = prefix_sums.get(prefix, 0) + 1

        return total
            
            
            
            
            
            
            
            
            
        