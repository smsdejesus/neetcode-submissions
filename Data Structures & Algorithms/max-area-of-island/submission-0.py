class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visit = set() 
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or grid[r][c] == 0 or (r,c) in visit:
                return 0

            visit.add((r,c))
            area = 1
            for dr,dc in directions:
                area += dfs(r + dr, c + dc)
            return area


        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and not (r,c) in visit:
                    area = dfs(r,c)
                    maxArea = max(maxArea,area)
        
        return maxArea