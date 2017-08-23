class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_num, max_num = [], []
        for i in range(len(arrays)):
            min_num.append((arrays[i][0], i))
            max_num.append((arrays[i][-1], i))
        min_num.sort(key = lambda x: x[0])
        max_num.sort(key = lambda x: x[0])
        if min_num[0][1] == max_num[-1][1]: ###have to make sure their id is not the same
            return max(max_num[-1][0] - min_num[1][0], max_num[-2][0] - min_num[0][0])
        else:
            return max_num[-1][0] - min_num[0][0]
        
      
