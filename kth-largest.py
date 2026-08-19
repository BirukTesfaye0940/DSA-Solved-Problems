from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            print("min_heap:",min_heap)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                print("heapq.heappop(min_heap):",min_heap)

        return min_heap[0]

sol = Solution()
print("Kth largest element:", sol.findKthLargest([3,2,1,5,6,4], 2))