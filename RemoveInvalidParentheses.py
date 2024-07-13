class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = set()
        check = -1
        def find(cur, i, l, r):
            nonlocal ans, check
            if i >= len(s):
                if l == r:
                    if len(cur) > check:
                        check = len(cur)
                        ans = set()
                        ans.add("".join(cur))
                    elif len(cur) == check:
                        ans.add("".join(cur))
            else:
                if s[i] == "(":
                    find(cur, i + 1, l, r)
                    cur.append(s[i])
                    find(cur, i + 1, l + 1, r)
                    cur.pop()
                elif s[i] == ")":
                    find(cur, i + 1, l, r)
                    if l > r:
                        cur.append(s[i])
                        find(cur, i + 1, l, r + 1)
                        cur.pop()
                else:
                    cur.append(s[i])
                    find(cur, i + 1, l, r)
                    cur.pop()
        find([], 0, 0, 0)
        return ans