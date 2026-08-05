class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxVal =0

        left = 0
        right = len(heights)-1

        while left < right:

            height =  min(heights[left],heights[right])
            storage = height * abs(left-right) 
            maxVal = max(maxVal,storage)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxVal            
