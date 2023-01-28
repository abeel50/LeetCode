class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # if there are only two pints they always connect by staright line
        if len(coordinates) == 2: return True
        
        # difference of first 2 points
        # cause if points lie on same line their distance ratio will be same
        dx = coordinates[0][0] - coordinates[1][0]
        dy = coordinates[0][1] - coordinates[1][1]
        
        for i in range(2, len(coordinates)):
            dx1 = coordinates[0][0] - coordinates[i][0]
            dy1 = coordinates[0][1] - coordinates[i][1]            
            if (dx1 * dy != dy1 * dx):
                return False
        return True