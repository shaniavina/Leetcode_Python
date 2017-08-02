
from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = list(self.nums)    ####you dont want to change self.nums, list() == deep copy
        for i in range(len(n)):
            j = randint(i, len(n) - 1)
            n[i], n[j] = n[j], n[i]    ####shuffle the rest of nums
        return n


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
