class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_area = area if max_area < area else max_area

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return max_area