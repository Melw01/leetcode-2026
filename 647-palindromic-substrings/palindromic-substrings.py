class Solution:
    def countSubstrings(self, s: str) -> int:
        def match_expand(l, r, s):
            subtotal = 0
            n = len(s)
            while l >= 0 and r < n and s[l] == s[r]:
                subtotal += 1
                l -= 1
                r += 1
            return subtotal


        total = 0
        n = len(s)

        for i in range(n):
            #Odd
            total += match_expand(i, i, s)
            #Even
            total += match_expand(i, i+1, s)
        return total


            

