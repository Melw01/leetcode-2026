from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
  
        
        # can't use a mutable to be a key (e.g. dictionary, array) it must be hashable
        # -> use an array first then convert to a TUPLE (immutable)

        # then use a frequency count using dictionary (instead of sorting since sorting takes a long time)

        anagrams_dict = defaultdict(list) # when you add a new key, defaultdict will auto create an empty list for you 

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams_dict[tuple(count)].append(s)

        return list(anagrams_dict.values())


