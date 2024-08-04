class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        ans = []
        def find(word, i):
            nonlocal ans
            if i >= len(s):
                ans.append(word[:-1])
                return
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    find(word + w + " ", i + len(w))
        find("", 0)
        return ans