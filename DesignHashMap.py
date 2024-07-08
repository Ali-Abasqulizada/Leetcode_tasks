class MyHashMap:

    def __init__(self):
        self.check = {}
    def put(self, key: int, value: int) -> None:
        self.check[key] = value
    def get(self, key: int) -> int:
        return self.check.get(key, -1)
    def remove(self, key: int) -> None:
        if key in self.check:
            self.check.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)