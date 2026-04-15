class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = {}

        for task in tasks:
            count[task] = 1 + count.get(task, 0)

        maxHeap = []
        for task, cnt in count.items():
            heapq.heappush(maxHeap, [-cnt, task])

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt, task = heapq.heappop(maxHeap)
                cnt += 1

                if cnt != 0:
                    q.append([cnt, task, time + n])

            if q and q[0][2] == time:
                heapq.heappush(maxHeap, [q[0][0], q[0][1]])
                q.popleft()

        return time



        


        



