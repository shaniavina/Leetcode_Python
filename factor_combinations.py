###backtracking
# Time:  O(nlogn)
# Space: O(logn)
class Solution(object):
    # @param {integer} n
    # @return {integer[][]}
    def getFactors(self, n):
        self.res = []
        self.getFactorsRecu(n, [])
        return self.res
    def getFactorsRecu(self, n, factors):
        if factors is None:
            i = 2
        else:
            i = factors[-1]
        while i <= n / i:
            if n % i == 0:
                factors.append(i)
                factors.append(n / i)
                self.res.append(list(factors))
                factors.pop()
                self.getFactorsRecu(n / i, factors)
                factors.pop()
            i += 1
