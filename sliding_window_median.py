from heapq import heappush, heappop, heapify
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        min_heap = []
        max_heap = []
        res = []
        for i in range(len(nums)):
            if not max_heap or nums[i] > -max_heap[0]:
                heappush(min_heap, nums[i])
                if len(min_heap) > len(max_heap) + 1:
                    heappush(max_heap, -heappop(min_heap))
            else:
                heappush(max_heap, -nums[i])
                if len(max_heap) > len(min_heap):
                    heappush(min_heap, -heappop(max_heap))
            if i >= k - 1:
                if k % 2:
                    res.append(min_heap[0])
                else:
                    med = (-max_heap[0] + min_heap[0]) / 2.0
                    res.append(med)
                toBeRemove = nums[i - k + 1]
                if toBeRemove <= -heappop(max_heap):
                    max_heap.remove(toBeRemove)
                    heapify(max_heap)
                else:
                    min_heap.remove(toBeRemove)
                    heapify(min_heap)
                if len(min_heap) > len(max_heap) + 1:
                    heappush(max_heap, -heappop(min_heap))
                if len(max_heap) > len(min_heap):
                    heappush(min_heap, -heappop(max_heap))
        return res
            
