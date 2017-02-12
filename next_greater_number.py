class Solution(object):
    def nextGreaterElement(self, findNums, nums):
      
      ret = []
        index_map = {}
        for i in range(len(nums)):
            index_map[nums[i]] = i
        
        for i in range(len(findNums)):
            num1 = findNums[i]
            found = False
            for j in range(index_map[num1] + 1, len(nums)):
                if num1 < nums[j]:
                    ret.append(nums[j])
                    found = True
                    break
            
            if not found:
                ret.append(-1)
        return ret  
        
        
##solution 2
        d = {}
        ##stack
        st = []
        ret = []
        
        for x in nums:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)
        for x in findNums:
            ret.append(d.get(x, -1))
        return ret
