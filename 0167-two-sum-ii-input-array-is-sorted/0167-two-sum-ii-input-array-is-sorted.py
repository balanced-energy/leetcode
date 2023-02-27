'''
Workflow Timestamps
1. 0:00 - 2:20 Make Sure You Understand the Problem
2. 2:20 - 4:55 Design a Solution / Runtime and Space Complexity
3. 4:55 - 7:10 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
Two pointers, start and end
Loop through the nums and check start + end value.
If the value is greater than the target, decrement end
else increment start. 
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Pointers
start = 0
end = len(numbers) - 1
indices = []

while start < end
    if start + end = target
        return [start+1, end+1]
    
    if start+end < target
        increment start
    else 
        decrement end
    
return indices 
4. Write the Code And Pass Test Cases.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Pointers
        start = 0
        end = len(numbers) - 1
        indices = []

        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]

            if numbers[start] + numbers[end] < target:
                start += 1
            else: 
                end -= 1
        
        return indices