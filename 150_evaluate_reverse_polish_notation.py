class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(r + l)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    stack.append(int(float(l) / float(r)))
        return stack.pop()
