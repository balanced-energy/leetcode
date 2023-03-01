
'''
1. Make Sure You Understand the Problem
nums = [2,3] -> [3,2]


[1,3,6,10]
2. Design a Solution / Runtime and Space Complexity
Populate prefix and suffix product arrays.
Prefix array will start from left and move to end of array calculating product of
elements up to that index. Product[i-1] * i
Suffix will start from right and work to beginning of array 

Loop through the arrays and multiply positions to produce output array. 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

# Initialize first and last elements as 1 since any number times 1 is itself 
pref_product = [0] * len(nums)
suff_product = [0] * len(nums)
answer = [0] * len(nums)
pref_product[0] = 1 
suff_product[-1] = -1

for i in range(len(nums)):
    calculate prefix product and save at i = i-1 * i
    
for i in reversed(nums):
    calculate prefix product and save at i = i-1 * i
    
# Loop through nums and output to answer array 
for i in range(len(nums))
    answer[i] = pref_product * suf_prod

return answer

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize first and last elements as 1 since any number times 1 is itself 
        pref_prod, suf_prod, answer = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        pref_prod[0] = 1 
        suf_prod[-1] = 1
        
        for i in range(1, len(nums)):
            pref_prod[i] = nums[i - 1] * pref_prod[i-1]

        for i in reversed(range(len(nums)-1)):
            suf_prod[i] = nums[i + 1] * suf_prod[i + 1]
        
       
        # Loop through nums and output to answer array 
        for i in range(len(nums)):
            answer[i] = pref_prod[i] * suf_prod[i]

        return answer