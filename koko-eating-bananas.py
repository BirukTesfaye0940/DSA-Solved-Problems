from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            total_hrs = self.calculateHours(piles, mid)

            if total_hrs <= h:
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans

    def calculateHours(self, piles: List[int], mid: int):
        total_hrs = 0
        for v in piles:
            total_hrs += (v + mid -1) // mid 
        return total_hrs
