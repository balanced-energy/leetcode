'''
Mock - 45m
Workflow Timestamps
1. 2:30 Make Sure You Understand the Problem
2. 17:52 Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
have keys map holding key:[times] and times:value map

keys {'foo':[1,3]}
times {1:'bar', 3:'bar2'}

init:
    keys = defaultdict(list)
    times = {}
    
set:
    keys[key].append(timestamp)
    times[timestamp] = value
        
    
get(key, timestamp):
    if key not in keys:
        return ""
    
    # Get most recent time for key
    times = keys[key]
    
    last_valid_time = 0
    for time in range(len(times),-1,-1):
        if time <= timestamp
            last_time = time
            break
    
    # last_valid_time is set, get from times map
    return times[last_valid_time]


3. Write the Code And Pass Test Cases.

["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

keys {love:[10,20]}
times {10:high, 20:low}
'''
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)
        self.times = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""

        # Get most recent time for key
        key_times = self.keys[key]

        last_valid_time = 0
        for i in range(len(key_times)-1,-1,-1):
            if key_times[i] <= timestamp:
                last_valid_time = key_times[i]
                break
        
        if last_valid_time == 0:
            return ''

        # last_valid_time is set, get from times map
        return self.times[last_valid_time]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)