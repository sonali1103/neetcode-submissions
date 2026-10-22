class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            x = heights[l]
            y = heights[r]
            area = (r - l) * min(x,y)
            max_area = max(max_area, area)
            if x < y:
                l += 1
            else:
                r -= 1
        return max_area
        