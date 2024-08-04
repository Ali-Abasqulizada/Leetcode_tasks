class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        ans = [None] * len(people)
        people.sort(key = lambda x : (x[0], x[1]))
        for h, o in people:
            i, j = 0, -1
            while i < len(people):
                if not ans[i] or ans[i][0] == h:
                    j += 1
                if j == o:
                    break
                i += 1
            ans[i] = [h, o]
        return ans