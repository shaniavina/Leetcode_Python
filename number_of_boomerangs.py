class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            count = {}
            for j in range(len(points)):
                if j == i:
                    continue
                dis = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if dis in count:
                    count[dis] += 1
                    res += 2 * (count[dis] - 1)
                else:
                    count[dis] = 1
        return res
        
        
        
           
