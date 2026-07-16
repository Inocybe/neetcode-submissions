class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sorted_key = "".join(sorted(s))

            if sorted_key in anagrams:
                anagrams[sorted_key].append(s)
            else:
                anagrams[sorted_key] = [s]
        
        return list(anagrams.values())