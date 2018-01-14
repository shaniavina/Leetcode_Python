from scipy.constants.constants import electron_mass
class Solution(object):
    def nestedWeightSum(self, nestedList):
        weighted, unweighted = 0, 0
        while nestedList:
            nextLevel = []
            for ele in nestedList:
                if not isinstance(ele, (list)):
                    unweighted += ele
                else:
                    nextLevel.append(ele)
            weighted += unweighted
            nestedList = nextLevel
        return weighted
slt = Solution()
print(slt.nestedWeightSum([[1,1],2,[1,1]]))
print(slt.nestedWeightSum([1,[4,[6]]]))


###second
class Solution(object):
    def depthSumInverse(self, nestedList):
        self.res = []
        for ele in nestedList:
            self.depthSumInverseHelper(ele, 0)
        
        sum = 0
        for i in reversed(range(len(self.res))):
            sum += self.res[i] * (len(self.res) - i)
        return sum
    def depthSumInverseHelper(self, list, depth):
        if len(self.res) < depth + 1:
            self.res.append(0)
        if list.isInteger():
            self.res[depth] += list.getInteger()
        else:
            for l in list.getList():
                self.depthSumInverseHelper(l, depth + 1)
            
        


