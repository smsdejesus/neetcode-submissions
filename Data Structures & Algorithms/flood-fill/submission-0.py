class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sColor = image[sr][sc]
        ROWS,COLS = len(image),len(image[0])
        visit = set()
        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or image[r][c] != sColor:
                return
            image[r][c] = color
            visit.add((r,c))
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r, c + 1)
        dfs(sr,sc)
        return image