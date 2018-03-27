# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def getSlope(self, numerator, denominator):
        if numerator == 0:
            return (0, 1)
        sign = 1
        if numerator / denominator < 0:
            sign = -1
        
        def getGcd(a, b):
            if b == 0:
                return a
            else:
                return getGcd(b, a % b)
        gcd = getGcd(abs(numerator), abs(denominator))
        return (sign * abs(numerator) // gcd, abs(denominator) // gcd)
    
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_points = 0
        for i, start in enumerate(points):
            slope_count, same = {}, 1
            for j in xrange(i + 1, len(points)):
                end = points[j]
                if start.x == end.x and start.y == end.y:
                    same += 1
                else:
                    slope = (1, 0)
                    if start.x - end.x != 0:
                        slope = self.getSlope((start.y - end.y), (start.x - end.x)) ####can not just save slope as keys, might hit the precision limit of floating numbers when we have pretty big denominator and numerator
                    if slope not in slope_count:
                        slope_count[slope] = 0
                        
                    slope_count[slope] += 1
            
            current_max = same            
            for slope in slope_count:
                current_max = max(current_max, slope_count[slope] + same)
                
            max_points = max(max_points, current_max)
            
        return max_points
