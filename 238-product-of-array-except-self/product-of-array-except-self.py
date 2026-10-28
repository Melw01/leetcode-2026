class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        right_arr = [0] * n # product of all num RIGHT OF N
        left_arr = [0] * n # product of all num LEFT OF N
        right_arr[0] = 1
        left_arr[-1] = 1
        curr_r_product = 1
        curr_l_product = 1
        # [1,  1,  2, 6]
        # [24, 12, 4, 1]


        for i in range(len(nums)):
            j = -i - 1
            right_arr[j] = curr_r_product
            left_arr[i] = curr_l_product
            curr_r_product *= nums[j]
            curr_l_product *= nums[i]
 
        
        return [l*r for l, r in zip(right_arr, left_arr)]
        
        
