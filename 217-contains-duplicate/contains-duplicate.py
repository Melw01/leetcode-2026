class Solution:
    #TC: O(N), N = length of nums
    #SC: O(N) for the set we created, worst case no duplicates and all N items are put into the set
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


        