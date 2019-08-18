class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #time: O(log(m+n))
#         1) len(left_part) == len(right_part)
# 2) max(left_part) <= min(right_part)

# (1) i + j == m - i + n - j (or: m - i + n - j + 1)
#     if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
# (2) B[j-1] <= A[i] and A[i-1] <= B[j]

        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, nums2, (len1 + len2) / 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (len1 + len2) / 2 + 1) + self.getKth(nums1, nums2, (len1 + len2) / 2)) * 0.5
    def getKth(self, nums1, nums2, k):
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.getKth(nums2, nums1, k)
        left, right = 0, m
        while left < right:
            mid = left + (right - left) / 2
            if 0 <= k - 1 - mid < n and nums1[mid] >= nums2[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1
        nums1_i = nums1[left - 1] if left - 1 >= 0 else float('-inf')
        nums2_j = nums2[k - 1 - left] if k - 1 - left >= 0 else float('-inf')
        return max(nums1_i, nums2_j)
