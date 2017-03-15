class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        goodPair = {"(":")","[":"]","{":"}"}
        for l in s:
            if l == "(" or l == "[" or l == "{":
                stack.append(l)
            else:
                if len(stack) == 0:
                    return False
                else:
                    b = stack.pop()
                    if goodPair[b] != l:
                        return False
        return len(stack) == 0    ####you have to use stack, since no other kind of bracket inside
