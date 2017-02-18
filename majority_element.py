class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, count = 0,1
        
        for i in range(1, len(nums)):
            if nums[idx] == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    idx = i
                    count = 1
        return nums[idx]
if __name__ =="__main__":
    print(Solution().majorityElement([1,2,2,2,2,2,2,2,2,2,3,4,5]))
                    
#####second solution

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        for key in count:
            if count[key] >= (len(nums) + 1) / 2:
                return key
      
