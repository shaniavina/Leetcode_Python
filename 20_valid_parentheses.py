class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        goodPair = {"(":")","[":"]","{":"}"}
        for c in s:
            if c in ['[','(','{']:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    b = stk.pop()     ### before pop(), have to consider if it is null or not
                    if goodPair[b] != c:
                        return False
        return len(stk) == 0
