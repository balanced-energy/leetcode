'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
[[0,30],[5,10],[15,20]]


min_heap = [5,30]

[[0,12],[5,10],[11,20],[13,14]]

min_heap = [12,20]
2. Design a Solution / Template / Runtime and Space Complexity
sort by intervals by start times
initialize a minheap with first interval end time

for each interval
    if start time of current interval is less than top element of minheap (next available rooms end time)
        push current interval end time to heap
    else
        replace current interval end time with top element and re-heapify

return len(min_heap)

3. Write the Code And Pass Test Cases.
'''
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        # Create rooms list with first interval in first room 
        rooms = [intervals[0][1]]
        
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            
            # Get room end time
            next_room_end = rooms[0]        
        
            if cur_start < next_room_end:
                heapq.heappush(rooms, cur_end)
            else:
                heapq.heapreplace(rooms, cur_end)
       
        return len(rooms)