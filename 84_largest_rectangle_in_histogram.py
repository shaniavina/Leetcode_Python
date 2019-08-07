class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stk = [-1]
        res = 0
        for i in range(len(heights)):
            while heights[i] < heights[stk[-1]]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1
                res = max(res, h * w)
            stk.append(i)
        heights.pop()     
        return res
    
    
