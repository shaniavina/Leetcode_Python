# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        #####using stk of tuple
        if not nestedList:
            return 0
        stk, res = [], 0
        for n in nestedList:
            stk.append((n, 1))
        while stk:
            next, d = stk.pop(0)
            if next.isInteger():
                res += d * next.getInteger()
            else:
                for i in next.getList():
                    stk.append((i, d + 1))
        return res
##time:o(n)
##space:o(h)
    #############recursion
    def NestedListWeightSum(self, input_list):
        return self.CountHelper(1, input_list)
    
    def CountHelper(self, weight, input_list):
        sum = 0
        for ele in input_list:
            if isinstance(ele, list):
                sum += self.CountHelper(weight + 1, ele)
            else:
                sum += weight * ele
        return sum
    
slt = Solution()
print(slt.NestedListWeightSum([[1,1],2,[1,1]]))
print(slt.NestedListWeightSum([1,[4,[6]]]))
