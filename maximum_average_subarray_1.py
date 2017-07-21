 #Time complexity : O(n)O(n). We iterate over the given numsnums array of length nn once only.

      #Space complexity : O(1)O(1). Constant extra space is used.

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        cur_sum = sum(nums[:k])
        res = cur_sum
        for i in range(k, len(nums)):
            cur_sum = cur_sum + nums[i] - nums[i - k]
            res = max(cur_sum, res)
        return float(res) / k      #####float
        
       
      
