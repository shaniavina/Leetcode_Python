from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()   ###both direction
        max_numbers = []
        for i in range(len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:   ###delete all the in-window smaller numbers
                dq.pop()
            dq.append(i)
            if i >= k and dq and dq[0] <= i - k:    ####if the first element is out of sliding window, remove it
                dq.popleft()
            if i >= k - 1:
                max_numbers.append(nums[dq[0]])
        return max_numbers
