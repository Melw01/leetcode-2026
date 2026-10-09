class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        l_array = [0] * n # each item is the product of all items from the left of num
        r_array = [0] * n # each item is the product of all items from the right of num

        l_multiplier = 1
        r_multiplier = 1

        for i in range(n):
            j = -i - 1
            
            # from left to right : [1, 1, 2, 6]
            l_array[i] = l_multiplier
            l_multiplier *= nums[i]
            
            
            # from right to left : [24, 12, 4, 1]
            r_array[j] = r_multiplier
            r_multiplier *= nums[j]
            
        return [l*r for l, r in zip(l_array, r_array)]

       