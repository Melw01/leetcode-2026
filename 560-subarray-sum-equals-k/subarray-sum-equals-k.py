class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0 # sum of a previous prefix array
        result = 0

        map = { 0 : 1 }

        for num in nums:
            prefix += num
            if prefix - k in map: 
                result += map[prefix - k]
            map[prefix] = map.get(prefix, 0) + 1
        return result



#[1, -1, 2, -1, 3].   k = 2.     result: [1, -1, 2], [2], [-1, 3] = 3


# prefix = 1

# prefix - k = -1       
                            # map:   {0, 1}
                                   # {}
                                   # {}
                                   # {}
                                   # {}
                                   # {}

# result = 0





# TC: O(N)
# SC: O(N)