class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]

        # count freq with hashmap
        # bucket sort, bucket = freq
        # iterate backwards range(k)

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                if len(res) != k:
                    res.append(num)

        return res

        



            



            