class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])

        result = set()

        for i in range(n):
            for j in range(m):
                result.add(grid[i][j])

                s = 1
                while i - s * 2 >= 0 and j - s >= 0 and j + s < m:
                    acc = (
                        grid[i][j]
                        + grid[i - s * 2][j]
                        + grid[i - s][j - s]
                        + grid[i - s][j + s]
                    )

                    for step in range(1,s):
                        acc += (
                            grid[i - step][j - step]
                            + grid[i - step][j + step]
                            + grid[i - s * 2 + step][j - step]
                            + grid[i - s * 2 + step][j + step]
                        )

                    result.add(acc)
                    s += 1

        result = list(result)
        result.sort(reverse = True)
        return result[:3]