class Solution:
    def word_pattern(self, pattern: str, char: str) -> bool:
        words = char.split()

        if not len(words) == len(pattern):
            return False

        ch_to_word = {}
        word_to_ch = {}

        for ch,word in zip(pattern, words):
            if ch not in ch_to_word:
                if word in word_to_ch:
                    return False
                else:
                    ch_to_word[ch] = word
                    word_to_ch[word] = ch
            else:
                if ch_to_word[ch] != word:
                    return False
        return True


sol = Solution()
print(sol.word_pattern("abaa", "dog dog dog dog"))