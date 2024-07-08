class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for i in s:
            if i in "({[":
                check.append(i)
            elif not check:
                return False
            elif i == ")" and check[-1] != "(":
                return False
            elif i == "}" and check[-1] != "{":
                return False
            elif i == "]" and check[-1] != "[":
                return False
            else:
                check.pop()
        return False if check else True