class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx, end_idx = 0, len(nums) - 1
        while start_idx < end_idx:
            pointer = (start_idx + end_idx) // 2
            if nums[pointer] == target:
                return pointer
            elif nums[pointer] > target:
                end_idx = pointer - 1
            else:
                start_idx = pointer + 1
        if nums[start_idx] == target:
            return start_idx
        return -1


        