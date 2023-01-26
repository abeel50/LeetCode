class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDistance = float('+inf')
        minIndex = -1
        for i in range(len(points)):
            xi, yi = points[i]
            if xi == x or yi == y:
                d = abs(x - xi) + abs(y - yi)
                if d < minDistance:
                    minDistance = min(d, minDistance)
                    minIndex = i
        return minIndex