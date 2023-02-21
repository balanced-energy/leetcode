'''
Workflow Timestamps
1. 0:00 - 5:10 Make Sure You Understand the Problem
2. 5:10 - 10:19 Design a Solution / Runtime and Space Complexity
3. 10:19 - 13:15 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. 13:15 - 31:18 Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
2. Design a Solution / Runtime and Space Complexity
- Traverse row and columns identifying land (1). 
- If we find land, it's starting perimter is 4
- Check valid positions for row above/below and columns left/right
    - if we find land substract a side from perimter, perimter - 1

Runtime: O(N*M) row length = N, column length = M
Space = O(1)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
total_perimeter = 0
# Traverse grid row x column
for each row:
    for each col:
        if pos is land:
            cur_perimeter = 4
            check valid adjacent cells and subtract 1 from perimter
            total_perimeter += cur_perimeter

return total_perimeter
4. Write the Code And Pass Test Cases.
'''


class Solution:
        # Returns the number of adjacent land cells
    def adjacent_land(self, row, col, grid):
        num_land = 0
        # Check row above
        if row - 1 >= 0:
            if grid[row - 1][col] == 1:
                num_land += 1
        # Check row below
        if row + 1 < len(grid):
            if grid[row + 1][col] == 1:
                num_land += 1
        # Check left column 
        if col - 1 >= 0:
            if grid[row][col - 1] == 1:
                num_land += 1
        # Check right column
        if col + 1 < len(grid[0]):
            if grid[row][col + 1] == 1:
                num_land += 1
        
        return num_land

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_perimeter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Check for land 
                if grid[row][col] == 1:
                    # Check adjacent cells for land
                    num_adj_land = self.adjacent_land(row, col, grid)
                    #print(f'pos:{row}:{col} adj_land = {num_adj_land}')
                    # Land perimter starts at 4
                    total_perimeter += 4 - num_adj_land
        
        return total_perimeter
