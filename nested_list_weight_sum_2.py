
class Solution(object):
    def nestedWeightSum(self, nestedls):
        weighted, unweighted = 0, 0
        while nestedls:
            nextLevel = []
            for ele in nestedls:
                if not isinstance(ele, list):
                    unweighted += ele
                else:
                    nextLevel += ele
            weighted += unweighted
            nestedls = nextLevel
        return weighted
slt = Solution()
print(slt.nestedWeightSum([[1,1],2,[1,1]]))
print(slt.nestedWeightSum([1,[4,[6]]]))


##second
class Solution(object):
    def depthSumInverse(self, nestedls):
        self.res = []
        for ele in nestedls:
            self.depthSumInverseHelper(ele, 0)
        sum = 0
        for i in reversed(range(len(self.res))):
            sum += self.res[i] * (len(self.res) - i)
        return sum
    def depthSumInverseHelper(self, ls, depth):
        if len(self.res) < depth + 1:
            self.res.append(0)
        if ls.isInteger():
            self.res[depth] += ls.getInteger()
        else:
            for l in ls.getList():
                self.depthSumInverseHelper(l, depth + 1)
