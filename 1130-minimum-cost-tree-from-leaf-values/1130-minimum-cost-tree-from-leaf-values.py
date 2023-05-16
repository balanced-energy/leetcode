'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem

Each node has either 0 or 2 children
leaf nodes in-order

6,2,4
12 + 24 = 36
6*2 + 6*4

8 + 24 = 36
2*4 + 6*4 


2,3,5

6 + 15 = 21
2*3 + 3*5

10 + 15 = 25
2*5 + 3*5


3,1,5

7,
2,1,4

  28
7    8
    2  4
   2 1



2. Design a Solution / Template / Runtime and Space Complexity
- Compute product of two highest values
- Compute which end leaf node to leave out
- compute product of leaf node pairs
- if only one leaf node left stop

3. Write the Code And Pass Test Cases.
'''
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        arr = [float('inf')] + arr + [float('inf')]
        n = len(arr)
        total_sum = 0

        while n > 3:
            lo = min(arr)
            idx = arr.index(lo)

            if arr[idx - 1] < arr[idx + 1]:
                total_sum += arr[idx - 1] * arr[idx]
            else:
                total_sum += arr[idx + 1] * arr[idx]

            arr.remove(lo)
            n = len(arr)

        return total_sum