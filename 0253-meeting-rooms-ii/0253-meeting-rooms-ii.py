'''
Workflow Timestamps
1. 0:00 - 8:15 Make Sure You Understand the Problem
2. 8:15 - 10:40 Design a Solution / Runtime and Space Complexity
3. 10:40 - 14:25 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[[0,20], [5, 10], [5, 30]] -> 3

[[0,1], [0,1]] -> 2

[[0, 10], [1, 30], [15, 20]] -> 
2. Design a Solution / Runtime and Space Complexity
rooms count variable, and occupied rooms list

Sort by start time
Place first intervals end time in occupied rooms list

Loop through meetings starting at index 1
    get current meeting start

    if start <= occupied rooms last element
        increment room count 
        add current end time to occupied rooms
        sort occupied rooms in reverse order 
    else 
        set occupied rooms last element to cur_end

Runtime: 
Space: 

3. Write a Template for Code in Logical Blocks. Aka Pseudocode

rooms count variable, and occupied rooms list

Sort by start time
Place first intervals end time in occupied rooms list

Loop through meetings starting at index 1
    get current meeting start

    if start <= occupied rooms last element
        increment room count 
        add current end time to occupied rooms
        sort occupied rooms in reverse order 
    else 
        set occupied rooms last element to cur_end
    
4. Write the Code And Pass Test Cases.
'''

'''
occupied_rooms = [15,29]
[[2,15],[36,45],[9,29],[16,23],[4,9]]
[[2,15], [4,9], [9,29], [16,23], [36,45]]
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 1
        # Stores end time of meetings in # of rooms 
        occupied_rooms = []
        intervals.sort()
        
        # Store first meetings end time in occupied room 
        occupied_rooms.append(intervals[0][1])
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]

            if start < occupied_rooms[-1]:
                rooms += 1
                occupied_rooms.append(intervals[i][1])
                occupied_rooms.sort(reverse=True)
            else: 
                occupied_rooms[-1] = intervals[i][1]
                occupied_rooms.sort(reverse=True)
       
        return rooms