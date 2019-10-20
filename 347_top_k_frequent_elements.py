import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frq = collections.defaultdict(list)
        for key, cnt in collections.Counter(nums).items():
            frq[cnt].append(key)
        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k:
                return res[:k]
        return res[:k]
