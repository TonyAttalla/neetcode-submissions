class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647 
        rows = len(grid)
        cols = len(grid[0])
        q = deque([])
        # add all treasure chests to q 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row,col,0))
        # if not q:
        #     return
        directions = [(0,-1), (1,0), (-1,0), (0,1)]
        while q:
            print("q EXISTS")
            (row, col, dist) = q.popleft()
            print(row,col,dist)
            if grid[row][col] >= dist:
                print("UPDATING")
                grid[row][col] = dist
                
                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1]
                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] != -1:
                        q.append((new_row,new_col, dist+1))
        return 