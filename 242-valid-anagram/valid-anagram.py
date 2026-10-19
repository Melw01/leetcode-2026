class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tally = [0] * 26

        for char_s in s:
            index = self.getIndex(char_s)
            tally[index] += 1
        
        for char_t in t:
            index = self.getIndex(char_t)
            if tally[index] == 0:
                return False
            tally[index] -= 1
        
        for item in tally:
            if item != 0:
                return False
            
        return True
    

    def getIndex(self, c: char) -> int:
        return ord(c) - ord('a')