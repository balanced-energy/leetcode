'''
Workflow Timestamps
1. 0:00 - 6:20 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

[1,2,3,2,1] = 0
[0,0,2,1,0] = 0
[1,2] = 0
[0,2,1,0,1]
[4,3,0,1,2]
[1,1,2,3,1,2,4]

# Walkthrough pseudocode 
[0,1,0,2,1,0,1,3,2,1,2,1]

left = [0,0,1,2,2,2,2,3,3,3,3,3]
right =[3,3,3,3,3,3,3,3,2,2,2,1]
2. Design a Solution / Runtime and Space Complexity
The ith bar can trap water if there is a bar with greater height on the left and the right.
    Pre-compute the highest left and right bars for the ith bar by 
    looping through array and tracking heighest left and right bars for that current index.

Once we have our max height arrays, loop through the array and check 
if the min(max_left, max_right) is greater than our ith bar
    we add the water level minus the height of the ith bar

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize max height arrays 
n = length of height array
left, right = 0 * n

# Compute max left
for i in left from 1 to n
    left[i] = max(height[i - 1], left[i-1])
    
# Compute max right starting from end 
for i in range n-2 to -1 
    right[i] = max(height[i+1], right[i+1])
    
# Check ith bar against max left and right
for i in range n
    water_level = min(left[i], right[i])
    
    if water_level > height[i]
        trapped_water += water_level - height[i]
        
return trapped_water
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        # Intitialize max bar arrays
        max_left = [0] * n
        max_right = [0] * n
        
        trapped_water = 0
        
        # Compute max_left array
        for i in range(1, n):
            max_left[i] = max(height[i - 1], max_left[i-1])
        
        # Compute max_right array
        for i in range(n-2, 0, -1):
            max_right[i] = max(height[i+1], max_right[i+1])
            
        
        # Check each ith bar vs max_left and max_right
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            
            if water_level > height[i]:
                trapped_water += water_level - height[i]
                
        return trapped_water