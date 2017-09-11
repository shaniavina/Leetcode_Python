class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(M, x_min, x_max, y_min, y_max):
            cnt = 0
            total = 0
            for i in range(x_min, x_max):
                for j in range(y_min, y_max):
                    total += M[i][j]
                    cnt += 1
            return int(total / cnt)
    
    
        if not M or not M[0]:
            return
        res = []
        
        for i in range(len(M)):
            tmp = []
            for j in range(len(M[0])):
                avg = helper(M,max(i-1,0),min(i+1,len(M)-1)+1,max(j-1,0),min(j+1,len(M[0])-1)+1)
                tmp.append(avg)
            res.append(tmp)
        return res
    
    
        
   
        
