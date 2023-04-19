'''
Mock - 45m
Workflow Timestamps
1. 18:00 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
Number can be repeated more then once


[1,2,3,?]
length = 4
range = 1 -> (length - 1) = [1,3]
sum = 8

1,1,1,3 = 6
1,1,2,3 = 7
1,2,2,3 = 8
2,2,2,3 = 9
1,1,2,2 = 6
1,1,3,3
2,2,3,3
3,3,1,2
3,3,1,1
3,3,1,2
3,3,3,1
3,3,3,2
3,3,3,3

[3,1,3,4,2]
range = [1,n]
length = n + 1
If length is 5 we know numbers containing are 1 -> 4. 


[1,3,4,2,2]

[1,2,3,4,5,5]


2. Design a Solution / Template / Runtime and Space Complexity
Using the element at nums[i] we traverse through nums until we find a cycle.



3. Write the Code And Pass Test Cases.
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        
        # Find intersection of pointers to detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if fast == slow:
                break
                
        # Find beginning of cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast