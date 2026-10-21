class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # how to determine if a substring is valid:
            # 
        l = 0
        max_len = 0
        freq = [0] * 26

        for r in range(len(s)):
            freq[ord(s[r]) - 65] += 1
            while (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - 65] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len