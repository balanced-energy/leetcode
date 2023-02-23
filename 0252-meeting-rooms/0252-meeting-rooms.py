'''
Workflow Timestamps
1. 0:00 - 6:05 Make Sure You Understand the Problem
2. 6:05 - 8:02 Design a Solution / Runtime and Space Complexity
3. 8:02 - 12:34 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 12:34 - 14:39 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
intervals = [] -> true 

intervals = [1,8], [0, 1] -> True
intervals = [1,5], [5,7] -> True
2. Design a Solution / Runtime and Space Complexity
Sort by start time, then loop through checking each end time is less than next start time.

Runtime: O(N logN)
Space: O(1)
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# First sort intervals by start time
inetervals.sort(key= lambda k[0])

for index, meet in intervals:
    # Check current meeting end time is less than next meeting start
    if intervals[index][1] >= intervals[index + 1][0]:
        return false

return True
4. Write the Code And Pass Test Cases.
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # First sort intervals by start time
        intervals.sort()

        for i in range(len(intervals) - 1):
            # Check current meeting end time is less than next meeting start
            if intervals[i][1] > intervals[i + 1][0]:
                return False

        return True