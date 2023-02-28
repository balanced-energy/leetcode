'''
Workflow Timestamps
1. 0:00 - 3:35 Make Sure You Understand the Problem
2. 3:40 - 23:40 Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[-1,0,1,2,-1,-4]
[-4,-1,-1,0,1,2]
2. Design a Solution / Runtime and Space Complexity
i + j = -num
Using twosum solution to solve this by finding complement of first num and then running twosum on rest of list with target of complement
store a complement set for ones we've already seen

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Two sum function
# Target is a sorted array 
twosum(arr, target, out):
start = 0
end = len(arr) - 1

# num1 = arr[num1] likewise for num2
for num in arr:
    if num1 + num2 = target:
        return append to output
    check if num1 + num2 < target:
        increment start
    else 
        decrement end
return  

#threesum
triplets = []
complements = set

sorted_nums = sort(sums)

for num in nums:
    find compliment of num
    check if in complements set
    twosum(sorted_nums, compliment, triplets)  

return triplets

[3,0,-2,-1,1,2] -> [[-2,-1,3],[-2,0,2],[-1,0,1]]
[-2,-1,1,0,2,3]
#-3
[-2,-1,0,1,2] -> [[-2,-1,3]]
#0
[-2,-1,1,2,3] -> [[-2,0,2]]
#1
[-2,0,1,2,3] -> [[-2,-1,3]]
4. Write the Code And Pass Test Cases.
'''
# Two sum function
# Target is a sorted array 
def twosum(arr, target, out):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        if arr[start] + arr[end] == target:
            print(f'com:{target}')
            out.append([arr[start], arr[end], -target])
            # Increment start while it's the same value
            start += 1
            while arr[start] == arr[start - 1] and start < end:
                start += 1
        
        if arr[start] + arr[end] < target:
            start += 1
        else:
            end -= 1
            
    return 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        complements = set()
        nums.sort()

        for idx, num in enumerate(nums):
            complement = -1 * num    
            if complement not in complements:
                twosum(nums[idx+1:], complement, triplets)
                complements.add(complement)
            
               
        return triplets