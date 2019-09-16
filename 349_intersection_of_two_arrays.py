class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lookup = {}
        for num in nums1:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        res = []
        for num in nums2:
            if num in lookup and lookup[num] > 0:
                res.append(num)
                lookup[num] = 0
        return res
