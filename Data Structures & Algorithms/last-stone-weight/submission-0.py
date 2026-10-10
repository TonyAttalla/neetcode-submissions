class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for stone in stones:
            heapq.heappush(hp, -1 * stone)
        while (len(hp) > 1):
            stone_1 = -1 *  heapq.heappop(hp)
            stone_2 =  -1 * heapq.heappop(hp)
            if (stone_1 == stone_2):
                continue
            else:
                stone_1 = stone_1 - stone_2
                heapq.heappush(hp, -1 * stone_1)
        if len(hp) == 1:
            return -1 * heapq.heappop(hp)
        return 0
        