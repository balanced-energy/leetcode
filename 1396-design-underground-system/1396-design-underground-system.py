
'''
Workflow Timestamps
1. 0:00 - 6:25 Make Sure You Understand the Problem
2. 6:25 - 10:12 Design a Solution / Runtime and Space Complexity
3. 10:12 - 13:00 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 13:00 - 30:56 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
- Initialize with customer id and checkin location map {id:check in}
- When checking out get the start location and create a string start-end saved in a location map with time of travel, start_end: [times].
- Get average will average the start_end path list of times.

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
# Intialize maps
id:start location map
travel time of path map

# checkin
update id and check in location to map

# checkout 
get checkin location from map
create string of start to end location 
if start_end string in travel_times map
    append to values 
else:
    create new key start_end path and add to times value list

# Get average
get start_end path and average list 

4. Write the Code And Pass Test Cases.
'''
import statistics
class UndergroundSystem:

    def __init__(self):
        # Inialize customer id and check in location map, travel times map
        self.id_checkin = {}
        self.travel_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.id_checkin[id] = (stationName, t)
      
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Get customer's check in location
        start_location, start_time = self.id_checkin[id]
        
        # Create string travel path using append vs + for O(N) time vs O(N^2)
        full_path = list(start_location)
        full_path.append('+')
        for c in stationName:
            full_path.append(c)
        travel_path = ''.join(full_path)
        
        if travel_path in self.travel_times:
            self.travel_times[travel_path].append(t - start_time)
        else:
            self.travel_times[travel_path] = [t - start_time]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Create string travel path using append vs + for O(N) time vs O(N^2)
        full_path = list(startStation)
        full_path.append('+')
        for c in endStation:
            full_path.append(c)
        travel_path = ''.join(full_path)

        times_list = self.travel_times[travel_path]

        return statistics.mean(times_list)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)