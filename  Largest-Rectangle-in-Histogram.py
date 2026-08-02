from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        biggestArea = 0
        for i, _ in enumerate(heights):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w =  i if not stack else i - stack[-1] - 1
                biggestArea = max(biggestArea, h * w)
            stack.append(i)
        return biggestArea