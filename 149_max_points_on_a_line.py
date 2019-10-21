class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # O(n ** 2) have to calculate all slopes btw 2 points
        
        # greastest common divisor
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        res = 0
        for i in range(len(points)):
            table = {'90': 1}
            samePoint = 0
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    samePoint += 1
                    continue
                if points[i][0] == points[j][0]:
                    angle = '90'
                else:
                    temp = gcd(points[i][1] - points[j][1], points[i][0] - points[j][0])
                    angle = ((points[i][1] - points[j][1]) / temp, (points[i][0] - points[j][0]) / temp)
                if not table.has_key(angle):
                    table[angle] = 1
                table[angle] += 1
            res = max(res, max(table.values()) + samePoint)
        if len(points) == 0:
            return 0
        return res
                    
