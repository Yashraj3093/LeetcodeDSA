class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points) - 1):
            currentX, currentY = points[i]
            targetX, targetY = points[i + 1]
            result += max(abs(targetX - currentX), abs(targetY - currentY))

        return result