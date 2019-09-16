class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # If the given array is not sorted and the memory is unlimited.
# Time:  O(m + n)
# Space: O(min(m, n))
# Hash solution.
#         lookup = {}
#         result = []
        
#         for num in nums1:
#             if num in lookup:
#                 lookup[num] += 1
#             else:
#                 lookup[num] = 1
                
#         for num in nums2:
#             if num in lookup and lookup[num] > 0:
#                 result.append(num)
#                 lookup[num] -= 1
#         return result
    
    
    
    # If the given array is already sorted, and the memory is limited, and (m << n or m >> n).
# Time:  O(min(m, n) * log(max(m, n)))
# Space: O(1)
# Binary search solution.
        
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

    
        nums1.sort(), nums2.sort()  # Make sure it is sorted, doesn't count in time.

        res = []
        left = 0
        for i in nums1:
            left = self.binary_search(nums2, left, len(nums2), i)
            if left < len(nums2) and nums2[left] == i:
                res += i,
                left += 1
        
        return res
    
    def binary_search(self, nums, left, right, target):
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left



# If the given array is not sorted, and the memory is limited.
# Time:  O(max(m, n) * log(max(m, n)))
# Space: O(1)
# Two pointers solution.

# If the given array is already sorted, and the memory is limited or m ~ n.
# Time:  O(m + n)
# Soace: O(1)
# Two pointers solution.

#         nums1.sort(), nums2.sort()  # O(max(m, n) * log(max(m, n)))

#         res = []
        
#         it1, it2 = 0, 0
#         while it1 < len(nums1) and it2 < len(nums2):
#             if nums1[it1] < nums2[it2]:
#                 it1 += 1
#             elif nums1[it1] > nums2[it2]:
#                 it2 += 1
#             else:
#                 res.append(nums1[it1])
#                 it1 += 1
#                 it2 += 1
        
#         return res
