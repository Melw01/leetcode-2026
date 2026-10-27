class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} #dict of number: index

        for i, num in enumerate(nums):
            counterpart = target - num

            if counterpart in seen:
                return [i, seen.get(counterpart)]
            
            seen[num] = i

        return []