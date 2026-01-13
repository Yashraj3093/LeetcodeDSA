class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        maxY, totalArea = 0,0
        for x,y, l in squares:
            totalArea += l**2
            maxY = max(maxY, y + l)

        def check(limit_Y):
            area = 0
            for x,y,l in squares:
                if y < limit_Y:
                    area += l * min(limit_Y - y,l)
            return area >= totalArea / 2

        lo, hi = 0, maxY
        eps = 1e-5
        while abs(hi - lo) > eps:
            mid = (hi + lo) / 2
            if check(mid):
                hi = mid
            else:
                lo = mid

        return hi 