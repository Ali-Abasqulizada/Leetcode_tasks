import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        check = {}
        for i in s:
            check[i] = check.get(i, 0) + 1
        heap = [[-count, ele] for ele, count in check.items()]
        heapq.heapify(heap)
        prev = None
        ans = ""
        while prev or heap:
            if prev and not heap:
                return ""
            count, ele = heapq.heappop(heap)
            ans += ele
            count += 1
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            if count != 0:
                prev = [count, ele]
        return ans