class Solution:

    def encode(self, strs: List[str]) -> str:
        return "./. ".join(strs) if strs else "/./."

    def decode(self, s: str) -> List[str]:
        if "/./." in s:
            return []

        words = s.split(" ")
        current_words = []
        result = []
        for word in words:
            if "./." in word:
                removed = word[:-3]
                current_words.append(removed)
                result.append(" ".join(current_words))
                current_words = []
            else:
                current_words.append(word)
        
        result.append(" ".join(current_words))

        
        return result

                