class Solution:
    


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # returns the area of the island connected to i,j
    # and marks i,j as visited
        length = len(grid)
        width = len(grid[0])
        def dfs(i,j):
            if i >= length or j>=width or i<0 or j<0 or grid[i][j] != 1:
                return 0
            d = [(0,1), (1,0), (0, -1), (-1,0)]
           
            grid[i][j] = -1
            area = 1
            for direction in d:
                area += dfs( i + direction[0], j + direction[1] )
            return area
        
    
        max_area = 0
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    print(area)
                    max_area = max(area, max_area)
        return max_area
    
        