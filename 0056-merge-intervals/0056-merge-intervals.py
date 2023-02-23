
'''
1. Make Sure You Understand the Problem

intervals = [1,3], [1,2], [3,5], [4,7] = [1,7]
2. Design a Solution / Runtime and Space Complexity
- Create merged_intervals 
- Sort intervals. 
- while index < len(intervals) - 1:
    cur_interval = intervals[index]
 
    - if merged_intervals and merged_intervals[-1][1] >= cur_interval[0]:
        merged_intervals[-1][1] = max(merged_intervals[-1][1])
        increment index
        continue does it recheck index for while loop
        
    - comparing cur_interval end time is greater than or equal next_interval start time. 
    - if overlap keep cur_interval start and whichever interval has later start time
        - increment index by 2
        - add to merged_intervals
    - otherwise add cur_interval to merged_intervals
    - increment index by 1
    

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Create merged_intervals 
merged_intervals = []
intervals.sort() 
- while index < len(intervals):
    cur_interval = intervals[index]
    
    # We've merged and last merge end time is greater than cur_intervals start
    - if merged_intervals and merged_intervals[-1][1] >= cur_interval[0]:
        # Make last merged max of cur_interval end and last merged end time
        merged_intervals[-1][1] = cur_interval[1]
        increment index
        continue 
    
    - if index =! len(intervals) - 1
        - comparing cur_interval end time is greater than or equal next_interval start time. 
        - if overlap keep cur_interval start and set end max of the two end times
            - increment index by 2
            - add to merged_intervals
            continue
    # Handle last element
    - else merged_intervals[-1][1] >= cur_interval[0]
        - merge 
    - otherwise add cur_interval to merged_intervals
    - increment index by 1

4. Write the Code And Pass Test Cases.
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Create merged_intervals 
        merged_intervals = []
        intervals.sort() 
        index = 0
        
        # Only one interval
        if len(intervals) == 1:
            return intervals
        
        while index < len(intervals):
            cur_interval = intervals[index]
        
            if merged_intervals and merged_intervals[-1][1] >= cur_interval[0]:
                merged_intervals[-1][1] = max([merged_intervals[-1][1], cur_interval[1]])
                index += 1
                continue 
            
            # If we're not on second to last index and the intervals overlap
            if index != len(intervals) - 1 and cur_interval[1] >= intervals[index+1][0]:    
                end_time = max(cur_interval[1], intervals[index+1][1])
                merged_intervals.append([cur_interval[0], end_time])
                index += 2
        
            # Otherwise append cur_interval to merged_intervals  
            else:
                merged_intervals.append(cur_interval)
                index += 1
                    

        return merged_intervals