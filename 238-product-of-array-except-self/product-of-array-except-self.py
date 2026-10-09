class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        l_array = [0] * n # auxiliary array, same size of nums, will contain products of all left items of i
        r_array = [0] * n # auxiliary array, same size of nums, will contain products of all right items of i
        
        l_multiplier = 1 
        r_multiplier = 1 

        # expectation
        # l_array =                              [1,   1, 2, 6]
        # r_array = [1, 4, 12, 24] in reverse -> [24, 12, 4, 1]
        # answer:                                [24, 12, 8, 6]

        for i in range(n):
            j = -i - 1

            # populate l_array
            l_array[i] = l_multiplier
            l_multiplier *= nums[i]

            #populate r_array
            r_array[j] = r_multiplier
            r_multiplier *= nums[j]

        return [l*r for l, r in zip(l_array, r_array)]

    # TC: O(N) , N is the size of the array
    # SC: O(1)