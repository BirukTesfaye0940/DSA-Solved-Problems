class Solution:
    def rob(self, nums: list[int]) -> int:
        tot1, tot2 = 0, 0
        for num in nums:
            temp = max(tot2, num + tot1)
            tot1 = tot2
            tot2 = temp
        return tot2
            
