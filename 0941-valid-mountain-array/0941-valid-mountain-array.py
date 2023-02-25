'''
Workflow Timestamps
1. 0:00 - 2:50 Make Sure You Understand the Problem
2. 2:50 - 12:50 Design a Solution / Runtime and Space Complexity
3. 12:50 - 21:55 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

[0,5,6,7,4] = True
2. Design a Solution / Runtime and Space Complexity
confirm length is at least 3 elements 
Loop throug each element in array. Have an increasing and decresing flag
for first element 
    confirm next is strictly greater, flag increasing
    continue
if increasing 
    if next element is not strictly greater
        flag decreasing
    
if decreasing 
    if next element is not strictly decreasing
        return false

if increasing and decreasing
    return True
    
return False
3. Write a Template for Code in Logical Blocks. Aka Pseudocode

if length array less than 3:
    return False
    
# Intitialize flags
increasing = False
decreasing = False

# Loop through length array - 1
for num in arr - 1:
    if num == arr[0]:
        if next element is strictly greater
        increasing is True
        continue
    if increasing 
        if next element is strictly less than current element
            # Handles last element being only decreasing value 
            if next element is last in array 
                return True
            flag decreasing
            

    if decreasing 
        if next element is not strictly decreasing
            return false

if increasing and decreasing
    return True
return False

'0,1,2,1,2'
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        # Intitialize flags
        increasing = False
        decreasing = False

        # Loop through length array - 1
        for idx in range(len(arr) - 1):
            cur_num = arr[idx]
            next_num = arr[idx + 1]
            
            # Not strict increase or decrease
            if cur_num == next_num:
                return False
            # Handle strictly increasing beginning
            if idx == 0:
                # Make sure we have strictly increasing beginning
                if cur_num < next_num:
                    increasing = True
                    continue

            if increasing and not decreasing: 
                if cur_num > next_num:
                    # Handle if last element is only decreasing value
                    if next_num == arr[-1]:
                        return True
                    # Start decreasing check
                    decreasing = True
                # Next number is not strictly increasing
              
                
            if decreasing: 
                if cur_num < next_num:
                    return False
               

        if increasing and decreasing:
            return True
        
        return False
