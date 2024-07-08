class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        count = 1
        preorder = preorder.split(",")
        for i in preorder:
            count -= 1
            if count < 0:
                return False
            elif i != "#":
                count += 2
        return count == 0