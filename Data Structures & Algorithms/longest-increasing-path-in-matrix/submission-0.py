class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp[i][j] represents the length of the longest increasing path starting at coord i,j
        dp = {}
        n = len(matrix)
        m = len(matrix[0])
        def dfs(i,j,max_so_far):
            lip_at_ij = 0
            if  i<0 or i>=n or j<0 or j>=m or matrix[i][j] <= max_so_far :
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
           
            lip_at_ij = 1
            # lip_at_ij = max(lip_at_ij, 1 + dfs(i + 1, j, matrix[i][j]))
            # lip_at_ij = max(lip_at_ij, 1 + dfs(i - 1, j,  matrix[i][j]))
            # lip_at_ij = max(lip_at_ij, 1 + dfs(i, j + 1,  matrix[i][j]))
            # lip_at_ij = max(lip_at_ij, 1 + dfs(i, j - 1,  matrix[i][j]))
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for d in directions:
                new_x = d[0]
                new_y = d[1]
                
                current_longest_increasing_path = 1 + dfs(i + new_x,j + new_y, matrix[i][j])
                lip_at_ij = max(lip_at_ij,current_longest_increasing_path)
            dp[(i,j)] = lip_at_ij
            return lip_at_ij
        for i in range(n):
            for j in range(m):
                dfs(i,j,-1)
        print(dp)
        return max(dp.values())


             

        