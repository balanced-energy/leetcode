'''
Mock - 45m
Workflow Timestamps
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.

[1]

[1,2]
[3,4]

[3,1]
[4,2]

[1,2,3]
[4,5,6]
[7,8,9]

Traverse cells using formula with r,c,n

for r in row
    for c in col
                  
first row: matrix[n-1 - r-1][c] = matrix[n-1 + c-1][n-1]


1(0,0) -> (0)(n-1)
2(0,1) -> (1)(n-1)
3(0,n-1) -> (n-1)(n-1)


second row: matrix[n-1 - r-1][n-1] = matrix[n-1 + c-1][n-1 - r-1]
4(1, 0) -> (0, 1)
5() 
6(1,n-1) -> (n-1,1)

7(n-1,0) -> (0,0)
8(n-1,1) -> (1,0)
9(n-1,n-1)-> (n-1, 0)

[7,4,1]
[8,5,2]
[9,6,3]


for r in row
    for c in col
    
1. Make Sure You Understand the Problem
2. Design a Solution / Template / Runtime and Space Complexity
3. Write the Code And Pass Test Cases.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for r in range(n // 2 + n % 2):
            for c in range(n // 2):
                tmp = matrix[n - 1 - c][r]
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - c - 1]
                matrix[n - 1 - r][n - c - 1] = matrix[c][n - 1 - r]
                matrix[c][n - 1 - r] = matrix[r][c]
                matrix[r][c] = tmp
        