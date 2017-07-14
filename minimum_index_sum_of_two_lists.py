class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
#         lookup1 = {}
#         res = {}
#         result = []
#         index_sum = 0
#         min_sum = float('inf')
#         for i, string in enumerate(list1):
#             lookup1[string] = i
#         for i, string in enumerate(list2):
#             if string in lookup1:
#                 index_sum = lookup1[string] + i
#                 res[string] = index_sum
#                 min_sum = min(index_sum, min_sum)
#         for key in res:
#             if res[key] == min_sum:
#                 result.append(key)
        
#         return result    
        
    
    
    ######better
        lookup = {}
        min_sum = float('inf')
        result = []
        for i, s in enumerate(list1):
            lookup[s] = i
        for j, s in enumerate(list2):
            if j > min_sum:
                break
            if s in lookup:
                if j + lookup[s] < min_sum:
                    result = [s]
                    min_sum = j + lookup[s]
                elif j + lookup[s] == min_sum:
                    result.append(s)
        return result
      
