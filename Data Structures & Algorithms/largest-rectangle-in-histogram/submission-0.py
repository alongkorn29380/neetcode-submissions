class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                popped_start, popped_height = stack.pop()
                area = popped_height * (i - popped_start)
                maxArea = max(maxArea, area)
                start = popped_start
            stack.append((start, h))
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))
        return maxArea