from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def find(i, j):
            if i >= len(word1):
                return len(word2) - j
            elif j >= len(word2):
                return len(word1) - i
            elif word1[i] == word2[j]:
                return find(i + 1, j + 1)
            return 1 + min(find(i, j + 1), find(i + 1, j), find(i + 1, j + 1))
        return find(0, 0)