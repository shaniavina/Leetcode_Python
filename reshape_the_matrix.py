class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # if not nums:
        #     return None
        # row = len(nums)
        # col = len(nums[0])
        
        # if (row * col) != (r * c):
        #     return nums
        
        # database = []
        # for i in range(row):
        #     for j in range(col):
        #         database.append(nums[i][j])
        
        # k = 0
        # mat = [[0 for i in range(c)] for j in range(r)]
        # while k < len(database):
        #     for i in range(r):
        #         for j in range(c):
        #             mat[i][j] = database[k]
        #             k += 1
        # return mat
        
        
        
        ####second
        if not nums or r * c != len(nums) * len(nums[0]):
            return nums
        count = 0
        mat = [[0 for i in range(c)] for j in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                mat[count / c][count % c] = nums[i][j]
                count += 1
        return mat
