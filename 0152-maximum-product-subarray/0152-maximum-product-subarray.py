'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
[2,3,-2,4]


one or odd negative numbers
[2,-3,-2,4]
max = 2
negatives = 0
cur_prod = 48

[-2,0,-1]
max_product = nums[0]
negs = 1
cur_product = -2


2. Design a Solution / Template / Runtime and Space Complexity
- create negatives number count variable 
- traverse array calculating product
    - negative number 
        - decrement count
    - num is 0 or negative and no more negatives
        - compare current product 
        
    calculate product
    
    if num < 0:
        negative_nums -= 1

    if num == 0 or num < 0 and negative_nums == 0:
        compare current product to max
        if idx + 1 < len(nums) - 1 and:
            cur_product = nums[idx+1]
        continue 
        
    cur_product *= num
           
        
    
    
    
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def get_max(numbers):
            largest_prod = -inf
            current_prod = 1
        
            for num in numbers:
                current_prod *= num
                largest_prod = max(current_prod, largest_prod)
                
                # Reset if 0 is seen
                if current_prod == 0: 
                    current_prod = 1
            
            return largest_prod
        
        return max(get_max(nums), get_max(reversed(nums)))
            