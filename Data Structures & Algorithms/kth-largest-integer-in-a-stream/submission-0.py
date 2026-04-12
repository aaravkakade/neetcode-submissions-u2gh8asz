class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # pop elements while len is > k
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # push to heap and then pop if len is greater than k after
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
