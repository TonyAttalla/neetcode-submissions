class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # run bfs from rotten fruit to every other fruit
        # queue up all our rotten fruit
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        visited = set()
        coords_to_rot_time = {}
        # q will have (i,j, time_to_rot)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        # run bfs 
        while q:
            i,j, time_to_rot = q.popleft()
            if (i,j) in visited:
                continue
            coords_to_rot_time[(i,j)] = time_to_rot
            visited.add((i,j))
            # rot up, down, left, and right and add them to queue
            directions = [(0,-1), (0,1), (1,0), (-1,0)]
            for direction in directions:
                new_row = i+direction[0]
                new_col = j+direction[1]
                if 0<=i+direction[0]<n and 0<=j+direction[1]<m and grid[new_row][new_col] != 0:
                    q.append((new_row, new_col, time_to_rot+1))
        
        max_rot_time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i,j) not in coords_to_rot_time:
                    return -1
                else:
                    if grid[i][j] == 1:
                        max_rot_time = max(max_rot_time,coords_to_rot_time[(i,j)]) 
                        
        return max_rot_time

    
        # iterate through grid one more time to check to see if all fruit are rotten, and if not return 0