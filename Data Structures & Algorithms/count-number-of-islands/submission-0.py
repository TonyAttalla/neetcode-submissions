class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run dfs from each land tile, marking it as visited with an id
        # at the end, count the number of ids

        n = len(grid)
        m = len(grid[0])

        # modify island
        def dfs(i,j, island_id) -> None:
            if 0<=i<n and 0<=j<m and grid[i][j] == "1":
                grid[i][j] = island_id
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for direction in directions:
                    dfs(i+direction[0], j+direction[1], island_id)
        

        current_id = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i,j,current_id)
                    current_id+=1
        return current_id - 2



        