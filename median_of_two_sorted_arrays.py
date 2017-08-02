class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)   ###nums2 is the shorter one
        lo, hi = 0, n2 * 2
        while lo <= hi:
            mid2 = (lo + hi) / 2   ###try cut2
            mid1 = n1 + n2 - mid2
            l1 = float('-inf') if mid1 == 0 else nums1[(mid1-1)/2]
            l2 = float('-inf') if mid2 == 0 else nums2[(mid2-1)/2]
            r1 = float('inf') if mid1 == n1 * 2 else nums1[mid1/2]
            r2 = float('inf') if mid2 == n2 * 2 else nums2[mid2/2]
            
            if l1 > r2:
                lo = mid2 + 1
            elif l2 > r1:
                hi = mid2 - 1
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        
        
# #my Generic solution.
#         def next(p1, p2, nums1, nums2):
#             if p1 >= len(nums1):
#                 res = nums2[p2]
#                 p2 += 1
#                 return p1, p2, res
#             if p2 >= len(nums2):
#                 res = nums1[p1]
#                 p1 += 1
#                 return p1, p2, res
#             if nums1[p1] > nums2[p2]:
#                 res = nums2[p2]
#                 p2 += 1
#                 return p1, p2, res
                
#             else:
#                 res = nums1[p1]
#                 p1 += 1
#                 return p1, p2, res

    
#         len1, len2 = len(nums1), len(nums2)
#         p1, p2, val = 0, 0, 0
#         for i in range((len1 + len2) / 2 + 1):
#             p1, p2, val = next(p1, p2, nums1, nums2)
#         if (len1 + len2) % 2:
#             return val
#         else:
#             p1, p2, new_val = next(p1, p2, nums1, nums2)
#             return (val + new_val) / 2.0
