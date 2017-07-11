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
            
###second           
       class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
#         if m == 0:
#             nums1 = nums2
       
        # i, j = 0, 0
        # while i < m and j < n:
        #     if nums1[i + j] >= nums2[j]:
        #         nums1 = [nums2[j]] + nums1
        #         j += 1
        #     else:
        #         i += 1
        # if j < n:
        #     nums1 += nums2[j:]
        
        
        ####beautiful code   ####from the end
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

            
