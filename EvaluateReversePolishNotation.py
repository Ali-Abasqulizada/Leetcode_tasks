class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        check = []
        for i in tokens:
            if i not in "+-*/":
                check.append(int(i))
            else:
                num1 = check.pop()
                num2 = check.pop()
                if i == "+":
                    check.append(num1 + num2)
                elif i == "-":
                    check.append(num2 - num1)
                elif i == "*":
                    check.append(num1 * num2)
                else:
                    check.append(int(num2 / num1))
        return check[0]