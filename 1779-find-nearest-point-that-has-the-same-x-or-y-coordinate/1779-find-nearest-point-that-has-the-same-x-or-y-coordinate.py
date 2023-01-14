class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        
        minDistance = float('+inf')
        minIndex = -1
        for i in range(len(points)):
            xi, yi = points[i]
            if xi == x or yi == y:
                d = abs(x - xi) + abs(y - yi)
                if d < minDistance:
                    minDistance = d
                    minIndex = i
        return minIndex