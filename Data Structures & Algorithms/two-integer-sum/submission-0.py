class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        builder_dict = {}
        for idx in range(len(nums)):
            if nums[idx] in builder_dict:
                return [builder_dict[nums[idx]], idx]
            builder_dict[target - nums[idx]] = idx