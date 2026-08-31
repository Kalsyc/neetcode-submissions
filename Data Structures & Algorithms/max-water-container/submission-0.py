class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left_ptr, right_ptr = 0, len(heights) - 1
        while left_ptr < right_ptr:
            result = max(result, min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr))
            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
        return result