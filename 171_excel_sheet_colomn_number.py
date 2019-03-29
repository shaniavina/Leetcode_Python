class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for char in s:
            res *= 26
            res += ord(char) - ord('A') + 1
        return res
if __name__ == "__main__":
    print Solution().titleToNumber("AA")
