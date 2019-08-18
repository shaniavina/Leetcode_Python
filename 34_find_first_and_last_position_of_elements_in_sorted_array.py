class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchLeft(l, r):
            while l < r:
                mid = l + (r - l) / 2
                if target == nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l
        def searchRight(l, r):
            while l <= r:
                mid = l + (r - l) / 2
                if target == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return r
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return [searchLeft(l, mid), searchRight(mid, r)]
            
        return [-1, -1]
    
    
    
    
