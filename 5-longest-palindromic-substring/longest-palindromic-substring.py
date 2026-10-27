class Solution:
    def longestPalindrome(self, s: str) -> str:
            # expand from center approach 
            # odd:(L and R start at same index, move outwards)
            # even: (same letter as center, L and R starts from the left and right of center)
        
        # Odd: l = i, r = i
        # Even: l = i, r = i + 1

        def match_expand(l, r, s):
            n = len(s)
            ret_indices = (0, 0)
            W = 0

            while l >= 0 and r < n and s[l] == s[r]:
                # matching values inbound
                ret_indices = (l,r)
                W = r - l + 1
                l -= 1
                r += 1
            return ret_indices, W

        n = len(s)
        if n == 0: return ''

        longest_length = 0
        longest_indices = (0,0)
        for i in range(n):
            # Odd
            best_indices, W = match_expand(i, i, s)
            if W > longest_length: 
                longest_indices, longest_length = best_indices, W

            # Even
            best_indices, W = match_expand(i, i+1, s)
            if W > longest_length: 
                longest_indices, longest_length = best_indices, W
        
        start, end_inclusive = longest_indices
        return s[start: end_inclusive+1]
            


