class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # stack
        # space: O(1)
        
        stack = []
        lookup = {'(':')', '[':']','{':'}'}
        for char in s:
            if char in lookup:
                stack.append(lookup[char])
            else:
                if len(stack) != 0:
                    top_element = stack.pop() ### before pop(), have to consider if it is null or not
                    if char != top_element:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(stack) == 0
            
