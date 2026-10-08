class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num_islands = 0 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # mark this one and explore its neighbours, mark them as well
        def dfs(i,j):
            grid[i][j] = "-1"
            for direction in directions:
                x = direction[0]
                y = direction[1]
                if 0 <= i+x < n and 0<= j+y < m and grid[i+x][j+y] == "1" :
                    dfs(i+x,j+y)

        # use -1 to mark seen
        for i in range(n):
            for j in range(m):
                # new island we havent seen yet
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i,j)

        
       

        return num_islands


        