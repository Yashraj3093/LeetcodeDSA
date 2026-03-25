class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        total = sum(grid[i][j] for j in range(m) for i in range(n))

        current = 0
        for i in range(n):
            for j in range(m): current += grid[i][j]
            if total - current == current: return True

        current = 0
        for j in range(m):
            for i in range(n): current += grid[i][j]
            if total - current == current: return True

        return False