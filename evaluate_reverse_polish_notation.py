import operator

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        nums = []
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        for token in tokens:
            if token not in operators:
                nums.append(int(token))   ###make sure that every element of nums is an integer, not string
            else:
                y, x = nums.pop(), nums.pop()
                nums.append(int(operators[token](x * 1.0, y)))   ###have to get into float
        return nums.pop()
        
        
