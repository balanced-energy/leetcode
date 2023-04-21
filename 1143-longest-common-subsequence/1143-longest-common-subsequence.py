'''
Mock - 45m
Workflow Timestamps
1. 2:00 Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

1. Make Sure You Understand the Problem
seq = 1
'abcde' , 'ace'

     a c e
  [0,0,0,0]
 a[0,1,0,0]
 b[0,0,0,0]
 c[0,0,1,0]
 d[0,0,0,0]
 e[0,0,0,1]

traversing cells 
prev_match = (r,c)
if current r,c greater then last matched char, add to seq
seq += 1

'aefc' , 'acef'

     a c e f
  [1,0,0,0,0]
 a[0,1,0,0,0]
 e[0,0,0,1,0]
 f[0,0,0,0,1]
 c[0,0,1,0,0]

seen = (1,1)

Cases:
The first letter of each string is the same.
The first letter of each string is different.

2. Design a Solution / Template / Runtime and Space Complexity
setup m, n matrix where m is length of text1 and n is length of text2
traverse cells, checking if chars match
if match, save r,c and only add to sequence for r,c greater then last match


rows = len(text1)
n = len(text2)


3. Write the Code And Pass Test Cases.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same.
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different
                # Check each case without using character from each string
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        return dp_grid[0][0]