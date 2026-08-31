class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        nums.sort()
        for i in range(len(nums) - 2):
            left_ptr, right_ptr = i + 1, len(nums) - 1
            while left_ptr < right_ptr:
                triplet = (nums[left_ptr], nums[right_ptr], nums[i])
                if nums[left_ptr] + nums[right_ptr] == 0 - nums[i] and triplet not in result:
                    result[triplet] = True
                elif nums[left_ptr] + nums[right_ptr] > 0 - nums[i]:
                    right_ptr -= 1
                else:
                    left_ptr += 1
        result = list(map(lambda x: list(x),result.keys()))
        return result