'''
Workflow Timestamps
1. 0:00 5:00 Make Sure You Understand the Problem
2. 5:00 - 40:30 Design a Solution / Runtime and Space Complexity
3. 40:30 - 52:45 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
[0, 10], [0, 10]

  l                  m                  r
  l       m          r    
          lm          r  
[0, 5], [9, 13], [16, 20],[21, 25] [25, 30] book [14, 15]


 l                  m                  r 
                    l         m        r
                              lm       r
[0, 5], [9, 13], [14, 15] [16, 20], [25, 30] book [21, 25]

   l     m    r
[0,5],[6,8],[10,15] book [7,9]
2. Design a Solution / Runtime and Space Complexity
Store bookings in a SortedList container 

# Booking function
Retrieve the first index where index start > target start using calendar.bisect_right((start, end))
    Then if index is not first element, if index - 1 end time > target start 
    OR 
    if index within len(bookings) and index start < target end
    return false
    
    # Otherwise valid booking
    add to sorted list bookings with calendar.add((start, end))
    
    return True
    
    
3. Write a Template for Code in Logical Blocks. Aka Pseudocode
from sortedcontainers import SortedList
# Create calendar
self.calendar = SortedList()


# Booking function
# Get index of first booking with a start time greater than target start
idx = bisect and get index

If index is not first element, and previous elements end time > target start
OR 
if index < len(calendar) and index start < target end
return False

# Valid booking
calendar.add((start,end))
    
return True
4. Write the Code And Pass Test Cases.

[0, 5], [9, 13], [14, 15] [16, 20], [25, 30] book [20, 25]


 l,m, r        r
[10,20],[20,30] book [20, 25] 

    lm       r
    lmr
[[33,41],[47,50],] book [25,32] should be true
'''
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        # Return index of first booking where index start time is greater than target start time
        idx = self.calendar.bisect_right((start, end))
            
        # check if previous element end time overlaps start or idx start time overlaps target end
        if idx > 0 and self.calendar[idx-1][1] > start or idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
        
        # Valid Booking
        self.calendar.add((start, end))
        
        return True
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)