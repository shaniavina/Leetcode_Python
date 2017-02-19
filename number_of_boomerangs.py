class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        pos_map = [{} for i in range(len(points))]
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if j == i:
                    continue
                distance_square = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if distance_square not in pos_map[i]:
                    pos_map[i][distance_square] = 1
                else:
                    pos_map[i][distance_square] += 1
                if distance_square not in pos_map[j]:
                    pos_map[j][distance_square] = 1
                else:
                    pos_map[j][distance_square] += 1   
        for i in range(len(points)):
            for dis in pos_map[i]:
                if pos_map[i][dis] > 1:
                    ret += pos_map[i][dis] * (pos_map[i][dis] - 1)
        return ret
        
        
        
           
