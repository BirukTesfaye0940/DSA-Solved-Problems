import heapq
from ast import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        n = len(nums)
        for i in range(n):
            count[nums[i]] = count.get(nums[i], 0) + 1
        min_heap = []
        for key, value in count.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [item[1] for item in min_heap]

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
