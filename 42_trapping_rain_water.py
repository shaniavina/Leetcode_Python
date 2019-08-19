def trap(self, height: List[int]) -> int:
        res, stk = 0, []
        for i in range(len(height)):
            while stk and height[i] > height[stk[-1]]:
                h = height[stk.pop()]
                if stk:
                    minH = min(height[stk[-1]], height[i])
                    res += (minH - h) * (i - stk[-1] - 1)
            stk.append(i)
        return res
        
       
