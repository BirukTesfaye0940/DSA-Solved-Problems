from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr = {0:1}
        current_prefix = 0
        ans = 0
        n = len(nums)
        for num in nums:
            current_prefix += num
            if current_prefix - k in arr:
                ans += arr[current_prefix - k]
            if current_prefix in arr:
                arr[current_prefix] += 1
            else:
                arr[current_prefix] = 1
        return ans

          