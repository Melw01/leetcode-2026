class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0

        map = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in map:
                result += map[prefix_sum - k]
            map[prefix_sum] = map.get(prefix_sum, 0) + 1
        return result