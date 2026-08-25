class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = nums.copy()
        right_product = nums.copy()[::-1]
        for idx in range(1, len(nums)):
            left_product[idx] *= left_product[idx - 1]
            right_product[idx] *= right_product[idx - 1]
        right_product = right_product[::-1]
        left_product = [1] + left_product[:-1]
        right_product = right_product[1:] + [1]
        return [left_product[i] * right_product[i] for i in range(len(nums))]

        
    
