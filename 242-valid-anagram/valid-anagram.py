class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tally = [0] * 26

        for char_s in s:
            tally[ord(char_s) - ord('a')] += 1
        
        for char_t in t:
            index = ord(char_t) - ord('a')
            if tally[index] == 0:
                return False
            tally[index] -= 1
            
        return True
