class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split('(\D)', input)
        nums = map(int, tokens[::2])
        ops = map({'+':operator.add, '-':operator.sub, '*':operator.mul}.get, tokens[1::2])
        lookup = [[None for i in range(len(nums))] for i in range(len(nums))]
        
        def diffWaysToComputeRecu(left, right):
            if left == right:
                return [nums[left]]
            if lookup[left][right]:
                return lookup[left][right]
            lookup[left][right] = [ops[i](x, y) for i in range(left, right) for x in diffWaysToComputeRecu(left, i) for y in diffWaysToComputeRecu(i + 1, right)]
            return lookup[left][right]
        return diffWaysToComputeRecu(0, len(nums) - 1)
            
