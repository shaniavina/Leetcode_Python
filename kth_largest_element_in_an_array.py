class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ###quick select: O(n)
        nums.sort()
        return nums[len(nums) - k]
        # return self.findKthLargestRecu(nums, len(nums) - k, 0, len(nums))
    def findKthLargestRecu(self, nums, rank, start, end):
        while start < end:
            pivot = nums[start]
            p2 = start + 1
            for p1 in range(start + 1, end):
                if nums[p1] < pivot:
                    nums[p2], nums[p1] = nums[p1], nums[p2]
                    p2 += 1
            nums[start], nums[p2 - 1] = nums[p2 - 1], nums[start]

            if p2 - 1 == rank:
                return nums[rank]
            elif p2 - 1 > rank:
                end = p2 - 1
            else:
                start = p2
        return nums[start]
