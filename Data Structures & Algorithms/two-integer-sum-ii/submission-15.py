class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr, right_ptr = 0, len(numbers) - 1
        while True:
            if numbers[left_ptr] + numbers[right_ptr] == target:
                return [left_ptr + 1, right_ptr + 1]
            if numbers[right_ptr] + numbers[left_ptr] > target:
                right_ptr -= 1
            else:
                left_ptr += 1