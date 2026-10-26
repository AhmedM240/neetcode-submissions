import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []

        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for key, value in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))
        
        return [h[1] for h in heap]
        