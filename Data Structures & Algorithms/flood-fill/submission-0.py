class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        
        row_len, col_len = len(image), len(image[0])

        def dfs(r,c):
            if r<0 or r>=row_len or c<0 or c>=col_len or image[r][c]!=orig:
                return 
            image[r][c] = color
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        dfs(sr,sc)
        return image