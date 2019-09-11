class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # iterate for (n - 1) times
        s = '1'
        for i in range(n - 1):
            count = 1
            temp = []
            for idx in range(1, len(s)):
                if s[idx] == s[idx - 1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[idx - 1])
                    count = 1 ### key point!!
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s
