class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tally = [0] * 26

        for char_s in s:
            index = ord(char_s) - ord('a')
            tally[index] += 1
        
        for char_t in t:
            index = ord(char_t) - ord('a')
            if tally[index] == 0:
                return False
            tally[index] -= 1
        
        for item in tally:
            if item != 0:
                return False
            
        return True