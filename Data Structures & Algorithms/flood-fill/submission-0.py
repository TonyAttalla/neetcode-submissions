class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        # if len(image == 0):
        #     return image
        if original_color == color:
            return image
        def dfs(sr,sc):
            
            if 0 <= sr < len(image) and 0<=sc<len(image[0]) and image[sr][sc] == original_color:
                # if image[sr][sc] == color:
                #     return image
                image[sr][sc] = color
                # recursively flood fill all 4 directions
                dfs( sr-1, sc)
                dfs( sr+1, sc)
                dfs( sr, sc-1)
                dfs(sr, sc+1)
        dfs(sr,sc)
        return image


        
        