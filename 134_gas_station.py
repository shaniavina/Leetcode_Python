class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        start, total, mini = 0, 0, float('inf')
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < mini:
                start = (i + 1) % len(gas)
                mini = total
        return start
            
