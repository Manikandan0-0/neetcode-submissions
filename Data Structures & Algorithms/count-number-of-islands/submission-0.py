class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        if not grid:
            return
        rows,cols=len(grid),len((grid)[0])
        islands=0
        def dfs(r:int,c:int)->None:
            
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c]=='0':
                return
            grid[r][c]='0'

            # Explore all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    islands+=1
                    dfs(r,c)
        return islands