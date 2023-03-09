
'''
1. Make Sure You Understand the Problem
 1.)
 l     m       r 
         l m   r
             lm r
[5,6,7,0,1,2,3,4] target = 3

2.)
 l       m       r
 l m   r 
    lm r
[5,6,7,8,0,1,2,3,4] target = 7

3.)
 l     m     r
 l m r
 lr
[2,5,6,0,0,1,2] target = 5

4.)
 l m r 
[3,5,1] target = 1

5.)
lm r
[3,1] target = 1


# Duplicates 
 l             m         r
         l     m         r
[1,1,1,1,2,3,1,1,1,1,1,1,1] target = 2

 l         m             r   
[1,1,1,1,1,1,1,1,2,3,1,1,1] target = 2

2. Design a Solution / Runtime and Space Complexity
Use Binary Search with modified cases.
Initialize pointers left and right

while left <= right
calculate  mid 
check if mid is target 

# Handle Duplicates 
while nums[left] = nums[mid] and left != mid:
    left += 1

# Find which half of array is still sorted
# First half still sorted
If nums[left] < nums[mid]. Then check for target in first half sorted range 
    If target in range, set right to be mid - 1
    else left = mid + 1
# Second half sorted
if nums[mid] < nums[right]. Then check for target in second half sorted range
    If target in range, set left to be mid + 1
    else right = mid - 1

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Initialize pointers 
left, right = 0, len arr - 1

while left <= right
calculate mid and check if target

# Find sorted half
# First half sorted
if nums[left] <= nums[mid]:
    if nums[left] <= target < nums[mid]
        right = mid - 1
    else 
        left =  mid + 1

elif nums[mid] <= nums[right]:
    if nums[mid] < target <= nums[right]:
        left = mid + 1

    else:
        right = mid - 1

return False
4. Write the Code And Pass Test Cases.


 l     m     r
         l m r
[4,5,6,7,0,1,2] target = 0

'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Skip through duplicates
            while left != mid and nums[left] == nums[mid]:
                left += 1

            # Find which half of array is still sorted
            # Left half sorted 
            if nums[left] <= nums[mid]:
                # Target in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # Second half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid - 1
        return False
            