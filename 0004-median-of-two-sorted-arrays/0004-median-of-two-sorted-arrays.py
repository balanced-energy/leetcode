'''
Workflow Timestamps
1. 0:00 - 2:20 Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem

[1,2,5,6,7,8,9,10]
median = 6.5 


a = [1,2,|9,10] -> aleft[1,2] aright[9,10,]
b =  [5,6,|7,8] -> bleft[5,6] bright[7,8]

2. Design a Solution / Runtime and Space Complexity
We find the length of both arrays. We want to perform binary search on the shorter array. 
To find split in second longer array we subtract first arrays split from total length of both.


We are searching for a split in each array where the condition aleftmax <= brightmin and bleftmax <= arightmin is found
once found we then check if odd or even and calculate mid

else we need to check which half of array to cut off by comparing 
aleftmax > brightmin: move to left half
or if bleftmax > arightmin move to right half

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
check which is longer
set shorter array as nums1 

m,n length of num1 and num2

total_size = (m + n + 1)//2

start = 0
end = m 
while start <= end:
    get a split
    get b split
    
    aleftmax = float("-inf") if a_part == 0 else nums1[a_part - 1]
    arightmin = float("inf") if a_part == m else nums1[a_part]
    bleftmax = float("-inf") if b_part == 0 else nums2[b_part - 1]
    brightmin = float("inf") if b_part == n else nums2[b_part]
    
    aleftmax <= brightmin and bleftmax <= arightmin
        # We have correct split
        # m + n is even
        if even:
            return max((aleftmax, bleft,max) + min(arightmin, brightmin))/2

        else:
            return max(aleftmax, bleftmax)

    elif aleftmax > brightmin:
        end = a_part - 1
    elif bleftmax > arightmind:
        start = a_part + 1
        
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        lower = 0
        higher = len(nums1) - 1

        while True:
            a_part = (lower + higher) // 2
            b_part = half - a_part - 2

            a_left_max = nums1[a_part] if a_part >= 0 else float("-infinity")
            a_right_min = nums1[a_part + 1] if (a_part + 1) < len(nums1) else float("infinity")
            b_left_max = nums2[b_part] if b_part >= 0 else float("-infinity")
            b_right_min = nums2[b_part + 1] if (b_part + 1) < len(nums2) else float("infinity")

            if a_left_max <= b_right_min and b_left_max <= a_right_min:
                if total % 2:
                    return min(a_right_min, b_right_min)
                return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2
            elif a_left_max > b_right_min:
                higher = a_part - 1
            else:
                lower = a_part + 1
                
                
            