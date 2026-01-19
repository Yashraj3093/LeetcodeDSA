class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        ps = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                ps[i][j] = (
                    mat[i][j]
                    + (ps[i - 1][j] if i > 0 else 0)
                    + (ps[i][j - 1] if j > 0 else 0)
                    - (ps[i - 1][j - 1] if i > 0 and j > 0 else 0)
                )
        
        def getSum(i, j, size):
            return(
                ps[i + size][j + size]
                - (ps[i - 1][j + size] if i > 0 and j + size < m else 0)
                - (ps[i + size][j - 1] if i + size < n and j > 0 else 0)
                + (ps[i - 1][j - 1]if i > 0 and j > 0 else 0)
            )

        result = 0

        for i in range(n):
            for j in range(m):
                for k in range(result, min(n - i, m - j)):
                    current = getSum(i, j, k)
                    if current <= threshold: result = k + 1
                    else: break

        return result