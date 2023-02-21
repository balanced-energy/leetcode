'''
1. Make Sure You Understand the Problem
input [[1]] -> 1

input [1,2]
      [3,4]
row_start = 0, 1
row_end = 2, 1
col_start = 1
col_end = 2, 1

input: [1, 2, 3]
       [4, 5, 6] - > [1,2,3,6,5,4]
       
input [1]
      [2]
      [3]
      [4] -> [1,2,3,4]?
      
row_start = 1
row_end = 4
col_start = 0
col_end = 0
      
      1, 2, 3, 4
      5, 6, 7, 8
      9, 10,11,12
      13,14,15,16 -> 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10

row_start = 0, 1, 2
row_end = 4, 3, 2
col_start = 0, 1
col_end = 4, 3, 2
                  
      
2. Design a Solution / Runtime and Space Complexity
Track row and column start and endpoints. 
- While row_start not equal to row_end or col_start not equal to col_end
- Right move from col_start to col_end (first row) appendind elements. At end of row, increment row_start.
    Check row_start not equal to row_end or col_start not equal to col_end
- Down move from row_start to row_end (last column) appending elements. At end of col decrement col_end.
    Check row_start not equal to row_end or col_start not equal to col_end
- Left move from col_end to col_start (last row) appending elements. At end of row decrement row_end.
    Check row_start not equal to row_end or col_start not equal to col_end
- Up move from row_end to row_start (first column) appending elements. At end increment col_start.
    Check row_start not equal to row_end or col_start not equal to col_end


3. Write a Template for Code in Logical Blocks. Aka Pseudocode
While row_start != row_end or col_start != col_end:
    # Move right
        append values from grid[row_start][col_start] - grid[row_start][col_end]
        adjust pointer
        check start_end pointers aren't equal
        
    # Move down
        append values moving down
        adjust pointer
        check start_end pointers aren't equal
    # Move Left
        append values moving left
        Adjust pointer
        check start_end pointers aren't equal
    # Move Up
        append values moving up
        adjust pointer
        check start_end pointers aren't equal
4. Write the Code And Pass Test Cases.
'''

'''
123
456
789
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Initialize output list
        spiral_nums = []
        
        row_start = 0
        col_start = 0
        row_end = len(matrix)
        col_end = len(matrix[0])
        
        while row_start != row_end or col_start != col_end:
            # Move right
            
            for i in range(col_start, col_end):
                spiral_nums.append(matrix[row_start][i])
            row_start += 1
            # Check rows left to traverse
            if row_start == row_end:
                return spiral_nums
            
            # Move down
            for i in range(row_start, row_end):
                spiral_nums.append(matrix[i][col_end - 1])
            col_end -= 1
            # Check columns left to traverse
            if col_start == col_end:
                return spiral_nums
            
            # Move left
            for i in range(col_end - 1, col_start - 1, -1):
                spiral_nums.append(matrix[row_end - 1][i])
            row_end -= 1
            # Check rows left to traverse
            if row_start == row_end :
                return spiral_nums
            
            # Move up
            for i in range(row_end - 1, row_start - 1, -1):
                spiral_nums.append(matrix[i][col_start])
            col_start += 1
            # Check columns left to traverse
            if col_start == col_end:
                return spiral_nums
         
        return spiral_nums
            
        