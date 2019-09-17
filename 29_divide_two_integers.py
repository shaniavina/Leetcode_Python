class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # keep substracting the new divisor div from the remaining left and then doubling div. if left < div, start from the orginal divisor.
        neg = (dividend < 0) != (divisor < 0)
        dividend = left = abs(dividend)
        divisor = div = abs(divisor)
        Q = 1
        res = 0
        while left >= div:
            left -= div
            res += Q
            div += div
            Q += Q
            if left < div:
                div = divisor
                Q = 1
        if neg:
            return max(-2 ** 31, -res)
        else:
            return min(2 ** 31 - 1, res)
