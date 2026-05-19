class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # movement      Up,  Down, Left,  Right
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        #Rows and col Maxes
        ROWS,COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r,c):
            # ocean check do nothing we done
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            
            # island turn water
            grid[r][c] = "0";
            # move all posible directions
            for dr,dc in directions:
                dfs(r + dr, c + dc)


        #traverse the whole grid
            # island found
                # when island DFS the whole island and remove from posibilities,
                # add 1
        for r in range(ROWS):
            for c in range(COLS):
                
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
            
        