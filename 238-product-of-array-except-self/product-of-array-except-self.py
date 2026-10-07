class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # core idea: have 2 auxiliary arrays: l_array and r_array, where 
            # l_array contains the products of all numbers to the left of nums[i]
            # r_array contains the products of all numbers to the right of nums[i]

            # for the first and last index, the leftest and rightest number is 1

        l_multiplier = 1
        r_multiplier = 1

        n = len(nums)

        l_array = [0] * n
        r_array = [0] * n

        for i in range(n):
            j = -i - 1

            l_array[i] = l_multiplier 
            r_array[j] = r_multiplier 

            l_multiplier *= nums[i]
            r_multiplier *= nums[j]

        return [l*r for l, r in zip(l_array, r_array)]