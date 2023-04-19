'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

[[1,2],[3,5],[6,7],[8,10],[12,16]]

insert = [4,8]

new_start = new_interval[0]
new_end = new_interval[1]

# check to the right for potential merges
for interval in intervals:
    start = interval[0]
    end = interval[1]
    
    # Case 1, no overlap
    if start < new_start and end < new_start:
        continue
    
    # Case 2, old interval start greater than new start
    if start > new_start:


# Second idea 

    check adjacent intervals for potential merge
    if start_index - 1 interval end time is less than greater than new_start, merge
    if end_index + 1 start time is less than or equal to new_end, merge
    
    return merged list

[[1,2],[3,5],[6,7],[8,10],[12,16]]

based on start
             [5,8]
[[1,2],[3,8],     ,[6,7],[8,10],[12,16]]

based on end
                   [4,8]
[[1,2],[3,4],[5,6],     ,[7,10],[12,16]]

insert = [4,8]

start_index = 2
end_index = 4

    start_index = bisect on new_start
    end_index = bisect on new_end 
    
    # Start time
    if start_index >=1:
        prev_interval = intervals[start_index-1]
        prev_start = prev_interval[0]
        prev_end = prev_interval[1]
        
        # Merge previous and new
        if prev_end >= new_start:
            prev_interval[1] = new_interval[0]
    
    # End time
     if end_index <= len(intervals) - 2:
        next_interval = intervals[start_index + 1]
        next_start = prev_interval[0]
        
        if next_start <= new_end:
            prev_interval[1] = next_interval[1]
           
            
    if merged_start and merged_end:
        return intervals
    elif merged_start:
        return intervals[:start_index]
    

2. Design a Solution / Template / Runtime and Space Complexity
    if not intervals:
        return newInterval

3. Write the Code And Pass Test Cases.
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        
        for i in range(len(intervals)):
            # Current interval strictly before new
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            
            # Current interval strictly after new
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = intervals[i] 
            
            # Overlap
            elif intervals[i][1] >= newInterval[0] or intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # last interval
        ans.append(newInterval) 
        return ans