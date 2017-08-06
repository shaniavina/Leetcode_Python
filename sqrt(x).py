class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x in (0, 1):
            return x
        left, right = 1, x / 2   ####a half is okay
        while left <= right:
            mid = left + (right - left) / 2   ####write in this way: overflow!
            if mid > x / mid:      ###overflow!
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
    
    
    
#     // Newton's method
# class Solution {
# public:
#     int sqrt(int x) {
#         if (x == 0) return 0;
#         double res = 1, pre = 0;
#         while (res != pre) {
#             pre = res;
#             res = (res + x / res) / 2;
#         }
#         return int(res);
#     }
# };
