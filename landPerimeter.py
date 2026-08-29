from ast import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
               if grid[r][c] == 1:
                if r -1 < 0 or grid[r-1][c] == 0:
                    perimeter += 1
                if r + 1 >= rows or grid[r+1][c] == 0:
                    perimeter += 1
                if c - 1 < 0 or grid[r][c-1] == 0:
                    perimeter += 1
                if c + 1 >= cols or grid[r][c+1] == 0:
                    perimeter += 1
                
        return perimeter