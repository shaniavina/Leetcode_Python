class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        ret = []
        while i < m or j < n:
            if j == n or (i < m and nums1[i] < nums2[j]):
                ret.append(nums1[i])
                i += 1
            else:
                ret.append(nums2[j])
                j += 1
        for i in range(len(ret)):
            nums1[i] = ret[i]
