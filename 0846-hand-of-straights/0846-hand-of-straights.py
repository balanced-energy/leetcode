'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

[7,1,3,2,2,3,4,6,8]
{6:1, 7:1, 8:1}

seq_length {7:2, 3:2}

2. Design a Solution / Template / Runtime and Space Complexity

#### FAILED IDEA - focused too much on reducing runtime
- Preprocess a frequency map. 
- Store a seq_length map when processing nums

# Can't make enough groups of size groupSize
if len(hand) % groupSize != 0:
    return False
    
for each num in hand we check
    if num+1 in seq_length map
        # Check if can create full groupsize sequence
        if num+1 value in seq_length map equals groupsize goal
            if new count in freq_map of num or num+1 is 0 
                remove proper num from maps 
    else 
        # Find length of potential sequence 
        pot_seq = find_sequence(num, freq_map, groupsize)
        if pot_seq == groupsize:
            reduce counts of every num in freq_map and seq_length
            if new count is zero delete from map
        else:
            seq_length[num] = pot_seq
    
    
find_sequence(num, freq_map, groupsize):
    size = 0
    while num in freq_map and size < groupsize
        size += 1
        num = num + 1
    return size


    
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Can't make enough groups of size groupSize
        if len(hand) % groupSize != 0:
            return False

        # Create frequency map
        frequencies = Counter(hand)

        # Sort keys and traverse through them starting from min
        for num in sorted(frequencies):
            # Check all occurencies of lowest num
            while frequencies[num] > 0:       
                # Check sequence exists up to group size
                for x in range(num, num + groupSize):
                    frequencies[x] -= 1

                    if frequencies[x] < 0:
                        return False
        
        return True