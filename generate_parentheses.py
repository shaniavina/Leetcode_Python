class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateParenthesisRecu(res, '', n, n)
        return res
    def generateParenthesisRecu(self, res, current, left, right):
        if left == 0 and right == 0:
            res.append(current)
        if left > 0:
            self.generateParenthesisRecu(res, current + '(', left - 1, right)
        if left < right:
            self.generateParenthesisRecu(res, current + ')', left, right - 1)
